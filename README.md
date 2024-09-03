# Weather Report Twitter Bot

This Python script fetches weather data for a randomly selected city, does a google image search with the selected city, downloads that image and posts a weather update along with said image to Twitter, repeating the process every 30 minutes.

## Features

- **Random City Selection**: Fetches weather information for a randomly selected city.
- **Weather Data Fetching**: Retrieves current weather data using the OpenWeatherMap API.
- **Image Download**: Downloads an image related to the city by doing a google image search and choosing the first picture.
- **Twitter Integration**: Posts a weather update along with the image to Twitter.
- **Scheduled Execution**: Runs every 30 minutes to provide regular updates.

## Prerequisites

<<<<<<< HEAD
Before running the script, make sure you have:

- **Python 3.x** installed.
- **Required Python packages**: `tweepy`, `requests`, `os`, `time`.
- **Twitter Developer Credentials**: You need Twitter API keys and tokens.
- **SERAPI API Key**: Required for fetching google search and retrieving image url.
- **OpenWeatherMap API Key**: Required for fetching weather data.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/weather-twitter-bot.git
   cd weather-twitter-bot
   ```

2. **Install Required Packages**:
   ```bash
   pip install tweepy requests
   ```

3. **Setup Configuration**:
   - Create a `keys.py` file in the root directory with the following content:
     ```python
     consumer_key = 'your_consumer_key'
     consumer_secret = 'your_consumer_secret'
     access_token = 'your_access_token'
     access_token_secret = 'your_access_token_secret'
     serpapi_key = 'your_serapi_key'
     weather_api = 'your_openweathermap_api_key'
     ```


4. **Provide Supporting Modules**:
   - Implement `select_random_city` in `random_city.py` to return a random city name.
   - Implement `get_first_image_url` in `first_image_url.py` to return a URL of an image related to the city.

## Usage

To run the script, execute:

```bash
python twitter_botV2.py
```

The script will run indefinitely, performing the following actions every 30 minutes:

1. Select a random city.
2. Fetch weather data for the selected city.
3. Download an image related to the city.
4. Post a weather update and the image to Twitter.
5. Delete the local image file.

## Code Explanation

- **Authentication**: Authenticates with Twitter using `tweepy`.
- **fetch_location**: Fetches weather data from OpenWeatherMap.
- **print_weather**: Formats weather data into a message.
- **PostIMG**: Uploads the image and posts the message to Twitter.
- **download_image**: Downloads an image from a URL.
- **delete_image**: Deletes the image file after posting.
