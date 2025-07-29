# -API-INTEGRATION-AND-DATA-VISUALIZATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: SARA MOMIN

*INTERN ID:* CTO4DH2218

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

##This project demonstrates how to fetch live weather forecast data from the OpenWeatherMap API and visualize it using Python libraries. The user enters one or more city names, and the program displays the temperature, humidity, and wind speed trends for the next 24 hours (based on 3-hour intervals).
Each weather attribute is presented as a line chart, allowing users to easily interpret the short-term forecast for each selected city.

🎯 Purpose of the Project:
*To integrate a real-time public REST API with a Python script.

*To demonstrate data extraction, parsing, and visualization.

*To provide a simple weather dashboard with visual insights into multiple cities.

*To practice modular programming and using libraries effectively.

🛠️ Tools and Libraries Used:

*requests	----Fetching weather data from the OpenWeatherMap API

*matplotlib.pyplot	-------Creating visualizations (line plots)

*Python 3.13	Programming language used

*VS Code	Code --------editor/IDE for writing and running the program

*OpenWeatherMap	--------Free public API for global weather data

💡 Real-World Applications:
✅ Weather Dashboards: A base for building a real-time weather monitoring app.

✅ Educational Projects: Great for students learning API integration and data visualization.

✅ Smart Agriculture: Farmers or systems can use this to track short-term changes in weather.

✅ Travel Planning Tools: Visualize weather for trip planning across multiple cities.

✅ IoT & Home Automation: Can be extended to trigger actions (like closing windows) if storms are forecasted.

🧪 How It Works (Workflow)
>User Input: User enters city names (comma-separated).

>API Request: The script sends an HTTP request to OpenWeatherMap to fetch forecast data.

>Data Extraction: Parses the response JSON to extract temperature, humidity, and wind speed for the next 8 time points (~24 hours).

>Visualization: Uses matplotlib to plot three line charts per city:

Temperature (°C)

Humidity (%)

Wind Speed (m/s)
