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
