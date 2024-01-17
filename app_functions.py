# Import necessary libraries and modules
from tmdbv3api import TMDb, Movie
from Key import TMDB_API_Key
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests

# Define a class for movie-related functions


class MovieFunctions:

    # Initialize the movie functions
    def initialize_movie_functions(self):
        self.tmdb = TMDb()  # Create a TMDb object
        self.tmdb.api_key = TMDB_API_Key  # Set the API key for TMDb
        self.movie = Movie()  # Create a Movie object
        self.similar_movies_data = []  # Initialize an empty list for similar movies data

    # Define a function to search for movies
    def search_movies(self):
        try:
            # Search for movies with the name entered by the user
            movies = self.movie.search(self.movie_name_entry.get())
            # Filter out movies without a poster
            movie_list = [m for m in movies if m.poster_path is not None]

            # Clear previous results
            for widget in self.scrollable_frame.winfo_children():
                widget.destroy()

            # Check if no movies found
            if not movie_list:
                # Show an error message
                tk.messagebox.showerror(
                    "No Results", "No movies found. Please try another search.")
                return

            # Display count of all movies found
            count_label = ttk.Label(
                self.scrollable_frame, text=f"Number of movies found: {len(movie_list)}")
            count_label.grid(row=0, column=0, sticky='w', pady=(10, 0))

            # Display search results
            # Note: start index changed to 1
            for idx, m in enumerate(movie_list, start=1):
                self.display_movie(self.scrollable_frame, m,
                                   idx, self.show_similar_movies)
        except requests.exceptions.HTTPError:
            # Show an error message if an HTTP error occurs
            tk.messagebox.showerror(
                "Error", "Invalid API Key or movie name. Please try again.")
        # Handle other exceptions
        except Exception as e:
            tk.messagebox.showerror(
                "Error", f"An unexpected error occurred: Please double check the spelling of the movie name and try again.")
