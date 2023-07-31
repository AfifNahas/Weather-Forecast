import requests
import csv


def run_weather_api():
    
    def get_weather_forecast(lat, lon, api_key):
        base_url = "https://api.openweathermap.org/data/2.5/forecast"
        params = {
            "lat": lat,
            "lon": lon,
            "appid": api_key,
        }

        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status() 

            data = response.json()
            return data

        except requests.exceptions.RequestException as e:
            print("Error making the API request:", e)
            return None

    latitude = 40.7128
    longitude = -74.0060
    your_api_key = "d3489a36e94c0c6e8ca88b42b9f3b55f"

    forecast_data = get_weather_forecast(latitude, longitude, your_api_key)
    #if forecast_data:
    #    print(forecast_data)


    rows = []
    for forecast in forecast_data["list"]:
        dt_txt = forecast["dt_txt"]
        temp_celsius = forecast["main"]["temp"] - 273.15
        humidity = forecast["main"]["humidity"]
        weather_description = forecast["weather"][0]["description"]
        wind_speed = forecast["wind"]["speed"]
        wind_direction = forecast["wind"]["deg"]
        clouds_percent = forecast["clouds"]["all"]

        row = [dt_txt, temp_celsius, humidity, weather_description, wind_speed, wind_direction, clouds_percent]
        rows.append(row)
   

    csv_file = "weather_forecast.csv"

    with open(csv_file, "w", newline="") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(["Date and Time", "Temperature (°C)", "Humidity (%)", "Weather Description", "Wind Speed (m/s)", "Wind Direction (°)", "Clouds (%)"])
        csv_writer.writerows(rows)

    print(f"CSV file '{csv_file}' created successfully.")

'''if __name__ == "__main__":
    file = './weather_forecast.csv'
    run_weather_api()
'''
run_weather_api()
