import requests
import matplotlib.pyplot as plt

API_KEY = "b1a599019f38e7d7acf0bb4d3724b64c"

# 🔹 Get cities from user input (comma-separated)
user_input = input("Enter city names separated by commas (e.g., Mumbai, Pune, Delhi): ")
cities = [city.strip() for city in user_input.split(",")]

def fetch_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"❌ Could not fetch data for {city}. Check spelling or try again.")
        return None

# 🔁 Loop through user-entered cities
for city in cities:
    data = fetch_weather_data(city)
    if data is None:
        continue  # Skip to next city if API failed

    dates = []
    temperatures = []
    humidities = []
    wind_speeds = []

    # Limit to next 8 time slots (~24 hours)
    for forecast in data['list'][:8]:
        dates.append(forecast['dt_txt'])
        temperatures.append(forecast['main']['temp'])
        humidities.append(forecast['main']['humidity'])
        wind_speeds.append(forecast['wind']['speed'])

    # 📊 Plotting
    plt.figure(figsize=(16, 5))
    
    # Temperature
    plt.subplot(1, 3, 1)
    plt.plot(dates, temperatures, marker='o', color='orange')
    plt.title(f"{city} - Temp (°C)")
    plt.xticks(rotation=45)
    plt.xlabel("Time")
    plt.ylabel("°C")

    # Humidity
    plt.subplot(1, 3, 2)
    plt.plot(dates, humidities, marker='s', color='blue')
    plt.title(f"{city} - Humidity (%)")
    plt.xticks(rotation=45)
    plt.xlabel("Time")
    plt.ylabel("%")

    # Wind Speed
    plt.subplot(1, 3, 3)
    plt.plot(dates, wind_speeds, marker='^', color='green')
    plt.title(f"{city} - Wind (m/s)")
    plt.xticks(rotation=45)
    plt.xlabel("Time")
    plt.ylabel("m/s")

    plt.suptitle(f"Weather Forecast - {city}", fontsize=16)
    plt.tight_layout()
    plt.show()
