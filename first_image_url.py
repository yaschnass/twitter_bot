# first_image.py
from keys import serpapi_key
from serpapi import GoogleSearch

def get_first_image_url(search_query):
    """
    Fetches the URL of the first image from Google Image Search using SerpAPI.

    Args:
        api_key (str): Your SerpAPI key.
        search_query (str): The query for the image search.

    Returns:
        str: URL of the first image or a message indicating no images found.
    """
    search = GoogleSearch({
        'q': search_query,
        'tbm': 'isch',  # 'tbm=isch' specifies an image search
        'api_key': serpapi_key
    })
    
    results = search.get_dict()
    
    # Check if 'images_results' is in the response
    if 'images_results' in results and len(results['images_results']) > 0:
        first_image = results['images_results'][0]
        return first_image.get('original', 'No URL found')
    else:
        return 'No images found'
