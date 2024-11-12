# Name: 
# email:  
# Assignment Number: Assignment 10
# Due Date:  
# Course #/Section:  
# Semester/Year:  
# Brief Description of the assignment: 
# Brief Description of what this module does: 
# Citations:
# Anything else that's relevant:

#url = "http://api.openweathermap.org/data/2.5/weather?q=London&appid=1cb3c2b82d302ffc5065e91193d228821&units=metric"
#API key: cb3c2b82d302ffc5065e91193d228821

import requests
import csv

class WeatherAPIClient:
    def __init__(self, city):
        self.api_key = "cb3c2b82d302ffc5065e91193d228821"  # Replace with your actual OpenWeatherMap API key
        self.city = city
        self.url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units=metric"

    def fetch_data(self):
        response = requests.get(self.url)
        print("HTTP Status Code:", response.status_code)  # Print status code to debug
        if response.status_code == 200:
            return response.json()  # Return raw JSON response
        else:
            print("Failed to retrieve data:", response.text)  # Display error message from server
            return None

    def process_data(self, data):
        """Process the JSON data to extract relevant weather information."""
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
        """Save extracted weather information to a CSV file."""
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(weather_info.keys())  # Write header (column names)
            writer.writerow(weather_info.values())  # Write the extracted data as a row
        print(f"Data saved to {filename}")



  


