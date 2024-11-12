# Name: Alexis Tipkemper-Sparks
# email:  Tipkemam@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 11/14/2024
# Course #/Section:  IS 4010
# Semester/Year:  Fall 2024
# Brief Description of the assignment: Using python and API data to retrieve information and put into CSV form
# Brief Description of what this module does: Practice python and using API data and keys
# Citations:
# Anything else that's relevant:

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
