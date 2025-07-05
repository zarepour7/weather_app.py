import requests

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/3.0/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric',
        'lang': 'en'
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    
    if data.get('cod') != 200:
        print("City not found.")
        return

    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    print(f"\n🌆 City: {city_name}")
    print(f"🌤 Weather: {weather}")
    print(f"🌡 Temperature: {temp}°C")
    print(f"💧 Humidity: {humidity}%")
    print(f"🌬 Wind Speed: {wind_speed} m/s")

if __name__ == "__main__":
    api_key = "8996fe0b7764198a8d84477bd85dd968"
    city = input("Enter city name: ")
    get_weather(city, api_key)
