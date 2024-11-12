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

from WeatherClientAPIPackage.WeatherAPIClient import WeatherAPIClient


if __name__ == "__main__":
    
    city = "London"  # Specify the city you want to retrieve data for
    client = WeatherAPIClient(city)  # Instantiate the client with the city name

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
