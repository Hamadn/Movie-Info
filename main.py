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
