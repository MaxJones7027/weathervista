import doctest
import scripts.utils
import os

def run_all_doctests():
    doctest.testmod(scripts.utils)

if __name__ == "__main__":
    run_all_doctests()


WEATHER_API_KEY="de3ce3c7abaef97cbd6c2bde4e20cc2b"
api_key = os.getenv("WEATHER_API_KEY")
print(f"My API key is: {api_key}")