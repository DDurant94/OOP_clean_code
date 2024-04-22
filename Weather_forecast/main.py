'''
2. Refactoring a Weather Forecast Application into Classes and Modules
Objective:
The aim of this assignment is to refactor an existing Python script for a weather forecast application into a more structured, 
object-oriented, and modular format. The focus will be on identifying parts of the script that can be encapsulated into classes 
and organizing these classes into appropriate modules to enhance code readability, maintainability, and scalability.

Task 1: Identifying and Creating Classes

Analyze the provided script and identify distinct functionalities that can be encapsulated into classes. Create classes that 
represent different aspects of the weather forecast application, such as fetching data, parsing data, and user interaction.

Problem Statement:

The existing script for the weather forecast application is written in a procedural style and lacks organization.

Code Example:

Expected Outcome:

A main.py script that demonstrates how the different modules and classes come together to form a fully functional weather 
forecast application. The script should exemplify the benefits of using OOP and modular programming in Python.
'''
from weather import WeatherForecast
def main():
    while True:
        weather = WeatherForecast()
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ").title()
        if city.lower() == 'exit':
            break
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        if detailed == 'yes':
            forecast = weather.get_detailed_forecast(city)
        else:
            forecast = weather.display_weather(city)
        print(forecast)

if __name__ == "__main__":
    main()