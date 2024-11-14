# Name: Alexis Tipkemper-Sparks / Quynh Doan
# email:  Tipkemam@mail.uc.edu / doanqb@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 11/14/2024
# Course #/Section:  IS 4010-001
# Semester/Year:  Fall Semester 2024
# Brief Description of the assignment: Using python and API data to retrieve information and put into CSV form
# Brief Description of what this module does: This module is the main entry point for retrieving and saving weather data. It initializes the WeatherAPIClient with a specified city, fetches real-time weather information from the OpenWeatherMap API, and processes the JSON data to extract relevant details such as temperature and humidity. Finally, it saves the processed data to a CSV file, ensuring data is stored only if successfully retrieved.
# Citations: W3Schools / Geeks4Geeks / In Class Assignment
# Anything else that's relevant: N/A

from WeatherClientAPIPackage.WeatherAPIClient import WeatherAPIClient

if __name__ == "__main__":
    
    city = "London"  # Specify the city you want to retrieve data for
    client = WeatherAPIClient(city)  # Instantiate the client

    # Fetch data from the OpenWeatherMap API
    data = client.fetch_data()

    # Process the fetched JSON data
    weather_info = client.process_data(data)

    # Check if data was successfully retrieved and processed
    if weather_info:
        print("Weather Information:", weather_info)  # Print the weather data
        client.save_to_csv(weather_info)  # Save the data to a CSV file
    else:
        print("No data available to save.")  # If no data, show error message
