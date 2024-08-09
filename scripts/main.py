import tkinter as tk
from tkinter import ttk
from create_dashboard import create_dashboard
from weather_api_class import WeatherAPI  # Import the new WeatherAPI class

# Initialize the WeatherAPI with your API key
api_key = "de3ce3c7abaef97cbd6c2bde4e20cc2b"
weather_api = WeatherAPI(api_key)

# Create the main Tkinter window
root = tk.Tk()
root.title("Weather Dashboard")

# Update the create_dashboard function to pass the weather_api instance
create_dashboard(root, weather_api)  # Pass the weather_api instance

# Start the Tkinter event loop
root.mainloop()
