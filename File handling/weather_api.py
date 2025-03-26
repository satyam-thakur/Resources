import requests

def get_weather_data(api_endpoint, api_key, city_name, units='metric'):
    complete_url = f"{api_endpoint}?q={city_name}&appid={api_key}&units={units}"
    response = requests.get(complete_url)
    return response.json()

# Example usage
api_endpoint = "http://api.openweathermap.org/data/2.5/weather"
api_key = "your_api_key_here"
city_name = "London"

weather_data = get_weather_data(api_endpoint, api_key, city_name)

if weather_data["cod"] == 200:
    main = weather_data["main"]
    print(f"Temperature: {main['temp']}°C")
    print(f"Humidity: {main['humidity']}%")
    print(f"Pressure: {main['pressure']} hPa")
    print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    print(f"Description: {weather_data['weather'][0]['description']}")
else:
    print(f"Error: {weather_data['message']}")

