import tweepy
import time
import requests
# Twitter API credentials
from keys import consumer_key, consumer_secret, access_token, access_token_secret
# Authenticate to Twitter
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Weather Report script
import requests

API_ROOT = "https://api.openweathermap.org/data/2.5/weather?q="
API_USER = "&appid=708e504faa095594df27be91c839e83d&units=metric"


def fetch_location(city_name):
    full_api = API_ROOT + city_name + API_USER
    return requests.get(full_api).json()

def print_weather(weather_data):
    city = weather_data["name"]
    main_weather = weather_data["weather"][0]["description"]
    temp = weather_data["main"]["temp"]
    feels_like = weather_data["main"]["feels_like"]
    temp_min = weather_data["main"]["temp_min"]
    temp_max = weather_data["main"]["temp_max"]
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"] * 1.944

    message = (f"Today in {city} we have {main_weather} with a median temperature of {temp}°C. "
               f"The minimum temperature is {temp_min}°C and the maximum is {temp_max}°C.\n"
               f"It feels like {feels_like}°C and the humidity is {humidity}%.\n"
               f"Windspeed: {wind_speed:.2f} knots.")
    
    if wind_speed >= 15:
        message += " Time to go Kiting!"
    else:
        message += " No kiting today :("

    if "snow" in weather_data:
        snow = weather_data["snow"].get("1h", 0)
        message += f" Snowfall: {snow} mm/h"
    
    return message



def post_weather_update(weather_data):

    try:
        client.create_tweet(text=weather_data)
        print("Weather update posted successfully!")
    except tweepy.TweepyException as e:
        print(f"Error posting tweet: {e}")

if __name__ == "__main__":
    while True:
        weather_data = fetch_location("Frankfurt")
        post_weather_update(print_weather(weather_data))
        time.sleep(1800)  # Sleep for 30 minutes
