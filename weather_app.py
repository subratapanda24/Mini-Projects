import requests

"""
Project: Weather Report App
Author: Subrata Panda

"""

class WeatherApp:

    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://api.openweathermap.org/data/2.5/weather"

    # Fetch weather information from API
    def fetch_weather(self, city):

        # Build API request URL manually
        full_url = f"{self.url}?q={city}&appid={self.api_key}&units=metric"

        print("Connecting to weather server...")

        response = requests.get(full_url)

        # Check if request worked
        if response.status_code == 200:
            data = response.json()     # JSON → Python dictionary
            return data
        else:
            print("❌ Unable to fetch weather data.")
            print("Status Code:", response.status_code)
            return None

    # Display weather
    def display_weather(self, city):

        data = self.fetch_weather(city)

        if data is None:
            print("Please try again with a valid city.")
            return

        main = data["main"]
        wind = data["wind"]
        condition = data["weather"][0]["description"]

        print("\n======= WEATHER REPORT =======")
        print("City:", city)
        print("🌡 Temperature:", main["temp"], "°C")
        print("🤒 Feels Like:", main["feels_like"], "°C")
        print("💧 Humidity:", main["humidity"], "%")
        print("🌬 Wind Speed:", wind["speed"], "m/s")
        print("🌥 Condition:", condition)
        print("👁 Visibility:", data.get("visibility", "N/A"), "meters")
        print("🧭 Pressure:", main["pressure"], "hPa")
        print("================================\n")


# ---------------- MAIN PROGRAM ----------------

API_KEY = "YOUR_API_KEY"

print("Weather Report App")
print("Project by: Subrata Panda")
print("Idea/Suggestion: Beginner API Learning Project\n")

city = input("Enter city name: ")

app = WeatherApp(API_KEY)
app.display_weather(city)

