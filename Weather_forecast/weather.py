class FetchingWeatherData:
  
  def fetch_weather_data(self,city):
    # Simulated function to fetch weather data for a given city
    print(f"Fetching weather data for {city}...")
    # Simulated data based on city
    try:
      weather_data = {
        "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
        "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
        "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
    }
      return weather_data.get(city, {})
    except KeyError:
        print(f"Do not have data for {city}")

class ParsingWeatherData:
  def parse_weather_data(self,data,city_):
    # Function to parse weather data
    if not data:
        return "Weather data not available"
    city = city_
    temperature = data["temperature"]
    condition = data["condition"]
    humidity = data["humidity"]
    return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

class WeatherForecast:
  def __init__(self):
    self.data_fetcher = FetchingWeatherData()
    self.data_parser = ParsingWeatherData()

  def get_detailed_forecast(self, city):
      # Function to provide a detailed weather forecast for a city
      weather_data = self.data_fetcher.fetch_weather_data(city)
      return self.data_parser.parse_weather_data(weather_data,city)

  def display_weather(self, city):
      # Function to display the basic weather forecast for a city
      weather_data = self.data_fetcher.fetch_weather_data(city)
      if not weather_data:
          print(f"Weather data not available for {city}")
      else:
          weather_report = self.data_parser.parse_weather_data(weather_data,city)
          print(weather_report)