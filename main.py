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
