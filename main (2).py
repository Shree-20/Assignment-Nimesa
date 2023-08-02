import requests

API_KEY = "b6907d289e10d714a6e88b30761fae22"
BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast"


def get_weather_data():
  url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
  # url=f"{BASE_URL}/hourly?q={city}&appid={API_KEY}"
  response = requests.get(url)
  return response.json()


def get_weather_by_date(data, date):
  for forecast in data["list"]:
    if forecast["dt_txt"] == date:
      return forecast["main"]["temp"]
  return None


def get_wind_speed_by_date(data, date):
  for forecast in data["list"]:
    if forecast["dt_txt"] == date:
      return forecast["wind"]["speed"]
  return None


def get_pressure_by_date(data, date):
  for forecast in data["list"]:
    if forecast["dt_txt"] == date:
      return forecast["main"]["pressure"]
  return None


if __name__ == "__main__":
  # city_name = input("Enter the city name (e.g., London,us): ")
  print("\nFetching weather data...\n")
  weather_data = get_weather_data()

  while True:
    print("\nOptions:")
    print("1. Get weather")
    print("2. Get Wind Speed")
    print("3. Get Pressure")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
      date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
      temperature = get_weather_by_date(weather_data, date)
      if temperature is not None:
        print(f"\nTemperature on {date}: {temperature} K")
      else:
        print("Data not available for the provided date.")
    elif choice == "2":
      date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
      wind_speed = get_wind_speed_by_date(weather_data, date)
      if wind_speed is not None:
        print(f"\nWind Speed on {date}: {wind_speed} m/s")
      else:
        print("Data not available for the provided date.")
    elif choice == "3":
      date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
      pressure = get_pressure_by_date(weather_data, date)
      if pressure is not None:
        print(f"\nPressure on {date}: {pressure} hPa")
      else:
        print("Data not available for the provided date.")
    elif choice == "0":
      print("\nExiting the program.\n")
      break
    else:
      print("Invalid choice. Please try again.")
