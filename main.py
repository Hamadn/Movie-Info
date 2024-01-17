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
