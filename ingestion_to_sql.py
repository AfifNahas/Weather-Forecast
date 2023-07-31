import mysql.connector
import pandas as pd
import time

host = 'localhost'
user = 'root'
password = 'root'
database = 'weather_api'


def load_to_db():

    try:
        connection = mysql.connector.connect(host=host, user=user, password=password, database=database)

        if connection.is_connected():
            print("Connected to the MySQL server.")
            cursor = connection.cursor()

            df = pd.read_csv('weather_forecast.csv', encoding='latin-1')

            for index, row in df.iterrows():
                date_time = row['Date and Time']
                temperature = row['Temperature (°C)']
                humidity = row['Humidity (%)']
                weather_description = row['Weather Description']
                wind_speed = row['Wind Speed (m/s)']
                wind_direction = row['Wind Direction (°)']
                clouds = row['Clouds (%)']

                query = "INSERT INTO weather_forecast (dt, temperature, humidity, weather_description, wind_speed, wind_direction, clouds) " \
                        "VALUES (%s, %s, %s, %s, %s, %s, %s)"

                cursor.execute(query, (date_time, temperature, humidity, weather_description, wind_speed, wind_direction, clouds))

            connection.commit()
            print("Data inserted successfully.")
            
            cursor.close()
            connection.close()
            print("Connection to the MySQL server is closed.")
        
    except mysql.connector.Error as e:
        print("Error connecting to MySQL server:", e)



