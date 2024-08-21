import tweepy
import time
import requests
import os
from keys import consumer_key, consumer_secret, access_token, access_token_secret, weather_api
from random_city import select_random_city
from first_image_url import get_first_image_url
# Authenticate to Twitter
client_V2 = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)
client_v1 = tweepy.API(tweepy.OAuth1UserHandler(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret))


# Weather Report script
API_ROOT = "https://api.openweathermap.org/data/2.5/weather?q="
API_USER = f"&appid={weather_api}&units=metric"
file_path = "twitter_test.jpg"

def fetch_location(random_city):
    full_api = API_ROOT + random_city + API_USER
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

    message = (f"Today in {random_city} we have {main_weather} with a median temperature of {temp}°C. "
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

def PostIMG(message, myImg):
    media = client_v1.media_upload(filename=myImg)
    media_id = media.media_id
    response = client_V2.create_tweet(text = message, media_ids = [media_id])



def download_image(image_url, file_path):
    """
    Downloads an image from a URL and saves it to a file.

    Args:
        image_url (str): The URL of the image.
        file_path (str): The file path where the image will be saved.

    Returns:
        bool: True if the image was downloaded successfully, False otherwise.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(image_url, headers=headers)
        if response.status_code == 200:
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f"Image successfully downloaded to {file_path}")
            return True
        else:
            print(f"Failed to download the image. Status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"An error occurred while downloading the image: {e}")
        return False

def delete_image(file_path):
    """
    Deletes a local image file.

    Args:
        file_path (str): The file path of the image to delete.
    """
    if os.path.exists(file_path):
        os.remove(file_path)
        print("Image deleted successfully!")
    else:
        print("Image file does not exist!")
    
if __name__ == "__main__":
    while True:
        random_city = select_random_city()
        image_url=get_first_image_url(random_city)
        download_image(image_url,file_path)
        weather_data = fetch_location(random_city)
        PostIMG(print_weather(weather_data),'twitter_test.jpg')
        delete_image(file_path)
        time.sleep(1800)  # Sleep for 30 minutes