# Import necessary libraries
import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk
from io import BytesIO
from app_functions import MovieFunctions


# Define a class for the movie application
class MovieApp(tk.Tk, MovieFunctions):
    def __init__(self):
        # Initialize the parent classes
        super().__init__()
        # Set the window size
        self.geometry("750x600")
        # Make the window vertically resizable
        self.resizable(False, True)
        # Set the window title
        self.title("MovieInfo")
        # Initialize the movie functions
        self.initialize_movie_functions()
        # Create the widgets
        self.create_widgets()

    def create_widgets(self):

        # Create a notebook with two tabs: Movies and Playlist
        self.notebook = ttk.Notebook(self)

        # Movies tab
        movies_tab = ttk.Frame(self.notebook)
        # Create the movies tab
        self.create_movies_tab(movies_tab)
        # Add the movies tab to the notebook
        self.notebook.add(movies_tab, text='Movies')

        # Playlist tab
        playlist_tab = ttk.Frame(self.notebook)
        # Create the playlist tab
        self.create_playlist_tab(playlist_tab)
        # Add the playlist tab to the notebook
        self.notebook.add(playlist_tab, text='Playlist')
        # Pack the notebook to make it visible
        self.notebook.pack(expand=True, fill='both')

    def create_movies_tab(self, tab):
        # Movie Search Section
        # Create a label for movie name entry
        ttk.Label(tab, text="Enter a movie name:",
                  font="Calibri 10 bold").pack()
        # Create an entry for movie name
        self.movie_name_entry = ttk.Entry(tab, width=50)
        # Pack the entry to make it visible
        self.movie_name_entry.pack()
        # Create a button to search movies
        ttk.Button(tab, text="Search Movies", style="Accent.TButton",
                   command=self.search_movies).pack()

        # Scrolling Canvas for search results and similar movies
        canvas = tk.Canvas(tab)
        # Create a scrollbar for the canvas
        scrollbar = ttk.Scrollbar(tab, orient="vertical", command=canvas.yview)
        # Create a frame inside the canvas to hold the content
        self.scrollable_frame = ttk.Frame(canvas)

        # Configure the canvas to update the scrollregion when the size of the frame changes
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        # Add the frame to the canvas
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        # Configure the canvas to use the scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)

        # Pack the main content
        canvas.pack(side="left", fill="both", expand=True)
        # Pack the scrollbar to the right of the canvas
        scrollbar.pack(side="right", fill='y')

    def create_playlist_tab(self, tab):
        # Playlist Frame
        # Create a frame for the playlist
        playlist_frame = ttk.Frame(tab, width=200)
        playlist_frame.pack(fill='y')

        # Title for the Playlist Frame
        # Create a label for the playlist title
        playlist_title = ttk.Label(
            playlist_frame, text="Your Playlist", font=("Arial", 12, "bold"))
        playlist_title.pack()

        # Frame for the movie entries in the playlist
        self.playlist_movies_frame = ttk.Frame(playlist_frame)
        self.playlist_movies_frame.pack(fill='both', expand=True)

    def update_playlist_display(self):
        # Clear the current content of the movies frame in the playlist
        for widget in self.playlist_movies_frame.winfo_children():
            widget.destroy()

        # Display movies in the playlist
        for movie_info in self.playlist:
            # Create a label for each movie in the playlist, displaying the title and year
            movie_label = ttk.Label(self.playlist_movies_frame, text=f"{
                movie_info['title']} ({movie_info['year']})")
            # Pack the label to make it visible
            movie_label.pack()

    def display_movie(self, parent, movie_data, row, command=None):
        # Create a frame for each movie
        frame = tk.Frame(parent, padx=10, pady=10)
        # Place the frame in the grid
        frame.grid(row=row, column=0, sticky='news', pady=10)

        # Check if the movie has a poster
        if movie_data.poster_path:
            # Construct the URL for the movie poster
            image_url = f"https://image.tmdb.org/t/p/w500{
                movie_data.poster_path}"
            # Send a GET request to the URL
            response = requests.get(image_url)
            # Check if the request was successful
            if response.status_code == 200:
                # Open the image and resize it
                image = Image.open(BytesIO(response.content))
                image = image.resize((100, 150))
                # Create a PhotoImage object for the image
                photo = ImageTk.PhotoImage(image)
                # Create a label for the image and add it to the frame
                image_label = ttk.Label(frame, image=photo)
                # Keep a reference to the image to prevent it from being garbage collected
                image_label.image = photo
                # Place the image label in the grid
                image_label.grid(row=0, column=0, rowspan=4)

        # Create a string for the movie title and year
        title_year = f"{movie_data.title} ({movie_data.release_date[:4]})"
        # Create a label for the title and year and add it to the frame
        ttk.Label(frame, text=title_year, font=("Arial", 12, "bold")).grid(
            row=0, column=1, columnspan=2, sticky='w')

        # Get the TMDb rating of the movie
        tmdb_rating = movie_data.vote_average
        # Create a label for the TMDb rating and add it to the frame
        tmdb_rating_label = ttk.Label(
            frame, text=f"TMDb Rating: {tmdb_rating}")
        tmdb_rating_label.grid(row=1, column=1, columnspan=2, sticky='w')

        # Create a label for the movie overview and add it to the frame
        overview = ttk.Label(frame, text=movie_data.overview,
                             wraplength=600, anchor='w', justify='left')
        overview.grid(row=2, column=1, columnspan=2, sticky='w')

        # Create a button to add the movie to the playlist and add it to the frame
        add_to_playlist_btn = ttk.Button(
            frame, text="Add to Playlist", style="Accent.TButton", command=lambda: self.add_to_playlist(movie_data))
        add_to_playlist_btn.grid(row=4, column=1, columnspan=2, sticky='w')

        # If a command is provided, create a button to show similar movies and add it to the frame
        if command:
            ttk.Button(frame, text="Show Similar", style="Accent.TButton", command=lambda: command(
                movie_data.id)).grid(row=3, column=1, columnspan=2, sticky='w')

        # Configure grid weights for expansion
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(row, weight=1)


# Run the application
if __name__ == "__main__":
    # Create an instance of the MovieApp class
    app = MovieApp()
    # Load the "azure.tcl" theme file
    app.tk.call("source", "azure.tcl")
    # Set the theme to "dark"
    app.tk.call("set_theme", "dark")
    # Start the application's main event loop
    app.mainloop()
