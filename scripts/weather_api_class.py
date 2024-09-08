import requests

# Define the custom exception class
class WeatherAPIError(Exception):
    """Custom exception for errors related to the WeatherAPI."""
    def __init__(self, message):
        super().__init__(message)

# Define the WeatherAPI class
class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5"

    def fetch_data(self, url):
        """
        Fetch data from the provided URL.

        Args:
            url (str): The URL to fetch data from.

        Returns:
            dict: The data fetched from the URL in JSON format.

        Raises:
            WeatherAPIError: If there is an issue with the API request.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            raise WeatherAPIError(f"Failed to fetch data: {e}")

    def fetch_weather_data(self, location):
        """
        Fetch current weather and forecast data for a given location.

        Args:
            location (str): The location (city name) to fetch weather data for.

        Returns:
            tuple: A tuple containing two elements:
                - dict or None: The current weather data.
                - dict or None: The weather forecast data.

        Raises:
            WeatherAPIError: If there is an issue with fetching the weather data.
        """
        try:
            current_url = f'{self.base_url}/weather?q={location}&appid={self.api_key}'
            current_data = self.fetch_data(current_url)

            forecast_url = f'{self.base_url}/forecast?q={location}&appid={self.api_key}'
            forecast_data = self.fetch_data(forecast_url)

            return current_data, forecast_data
        except WeatherAPIError as e:
            print(f"An error occurred while fetching weather data: {e}")
            return None, None

# Example usage:
api = WeatherAPI("f217e635c0a1f3a54dae14ffbc07da98")
try:
    current_data, forecast_data = api.fetch_weather_data("New York")
    if current_data and forecast_data:
        print("Weather data fetched successfully!")
        # Process the data as needed
    else:
        print("No data returned.")
except WeatherAPIError as e:
    print(f"An error occurred: {e}")

