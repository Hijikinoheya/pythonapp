import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        return f"Weather in {city}: {weather_description}, Temperature: {temperature}°C, Humidity: {humidity}%, Wind Speed: {wind_speed} m/s"
    else:
        return f"Failed to retrieve weather information for {city}"

if __name__ == "__main__":
    api_key = "YOUR_API_KEY"  
    city = input("Enter city name (e.g., Japan,Tokyo): ").strip()
    print(get_weather(api_key, city))
