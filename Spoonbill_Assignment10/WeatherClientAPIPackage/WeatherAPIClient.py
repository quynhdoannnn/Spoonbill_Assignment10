# Name: Alexis Tipkemper-Sparks / Quynh Doan
# email:  Tipkemam@mail.uc.edu / doanqb@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 11/14/2024
# Course #/Section:  IS 4010-001
# Semester/Year:  Fall Semester 2024
# Brief Description of the assignment: Using python and API data to retrieve information and put into CSV form
# Brief Description of what this module does: This module defines a WeatherAPIClient class that retrieves, processes, and saves weather data for a specified city using the OpenWeatherMap API. It includes methods to fetch data in JSON format, extract key details (such as temperature, weather conditions, humidity, and wind speed), and save this information to a CSV file. The module streamlines interaction with the weather API and ensures data is saved in a structured format for easy access.
# Citations: W3Schools / Geeks4Geeks / In Class Assignment
# Anything else that's relevant: N/A

import requests
import json
import csv

class WeatherAPIClient:
    """
    A client to interact with the National Weather Service API to fetch and process weather forecast data.
    @param latitude: The latitude of the location.
    @param longitude: The longitude of the location
    """
    def __init__(self, city): #Constructor
        self.parsed_json = None
        self.api_key = "cb3c2b82d302ffc5065e91193d228821"  # Replace with your actual OpenWeatherMap API key
        self.city = city
        self.url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units=metric"
        

    def fetch_data(self):
        """
        Fetches weather forecast data from the National Weather Service API.

        @return: A JSON object containing forecast data if the request is successful, or an empty dictionary if unsuccessful.
        @raises: Exception if there is a network issue or the server is unreachable.
        """
        # Following architecture from InClass
        # Commented out some excessive info
        response = requests.get(self.url)
        json_string = response.content
        self.parsed_json = json.loads(json_string)
        #print("HTTP Status Code:", response.status_code)  # Print status code to debug
        #if response.status_code == 200:
        return response.json()  # Return raw JSON response
        #else:
        #    print("Failed to retrieve data:", response.text)  # Display error message from server
        #    return None


    def process_data(self, data):
        """
        Process the JSON data to extract relevant weather information.
        """
        if data:
            weather_info = {
                "City": data["name"],  # Extract city name
                "Temperature (C)": data["main"]["temp"],  # Extract temperature in Celsius
                "Weather": data["weather"][0]["description"],  # Weather condition
                "Humidity (%)": data["main"]["humidity"],  # Humidity percentage
                "Wind Speed (m/s)": data["wind"]["speed"]  # Wind speed in meters per second
            }
            return weather_info
        else:
            return None

    def save_to_csv(self, weather_info, filename="weather_data.csv"):
        """
        Save extracted weather information to a CSV file.
        """
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(weather_info.keys())  # Write header (column names)
            writer.writerow(weather_info.values())  # Write the extracted data as a row
        #print(f"Data saved to {filename}") 



  


