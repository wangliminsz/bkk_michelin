import requests
from mydata import *

def get_place_details(place_id):
    # Replace 'YOUR_API_KEY' with your actual Google Places API key
    api_key = 'AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    url = f'https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name,website&key={api_key}'
    
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'OK':
        result = data['result']
        name = result['name']
        website = result.get('website')
        return name, website

    else:
        return None, None

def get_lat_lng(location):
    # Replace 'YOUR_API_KEY' with your actual Google Maps API key
    api_key = 'AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={api_key}'
    
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'OK':
        result = data['results'][0]
        lat = result['geometry']['location']['lat']
        lng = result['geometry']['location']['lng']
        place_id = result['place_id']
        # print('location outside----------------->', result)
        # return lat, lng, place_id

        # url01 = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&key={api_key}'
        url01 = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=" + location + "&rankby=distance&key={}&location={},{}".format(api_key,lat,lng)
              
        response01 = requests.get(url01)
        data01= response01.json()

        if data01['results'][0].get("photos") is None:
            return lat, lng, place_id, None
        else:
            print('location pic---------------->', data01['results'][0]['photos'][0]['photo_reference'])
            photo_ref = data01['results'][0]['photos'][0]['photo_reference']
            if photo_ref:
                return lat, lng, place_id, photo_ref
            else:
                return lat, lng, place_id, None
    else:
        return None, None, None, None

def get_image_url(photo_reference):
    # Replace 'YOUR_API_KEY' with your actual Google Places API key
    api_key = 'AIzaSyCATQOeaNUfVnUCoOkr3DE4Ss8pPhtjlkg'
    url = f'https://maps.googleapis.com/maps/api/place/photo?maxwidth=1024&photoreference={photo_reference}&key={api_key}'

    return url


# Example list of location names
# locations = ['Bangkok Patana School', 'NIST International School', 'International School Bangkok']

# Open the text file in write mode
with open('coordinates.txt', 'w') as f:
    for location in locations:
        lat, lng, place_id, photo_ref = get_lat_lng(location)
        if lat and lng and place_id:
            name, website = get_place_details(place_id)
            if website:
                f.write("{\n")
                f.write(f"'Location': '{location}',\n")
                f.write(f"'Latitude': '{lat}',\n")
                f.write(f"'Longitude': '{lng}',\n")
                f.write(f"'Website': '{website}',\n")

                # Retrieve the photo reference for the location
                if photo_ref:
                    photo_url = get_image_url(photo_ref)
                    if photo_url:
                        f.write(f"'Image URL': '{photo_url}'\n")
                
                f.write("},\n")
                f.write('\n')
        else:
            f.write(f"Error: Unable to retrieve coordinates for {location}\n")

print("Coordinates, website URLs, and image URLs written to coordinates.txt file.")



# # ---------------------------

# if nearby_Facility_20[i].get("photos") is None:
#                     resultDict["locPhotoUrl"] = None
# else:
#     resultDict["locPhoto_reference"] = nearby_Facility_20[i]["photos"][0]["photo_reference"]
#     resultDict["locPhoto_width"] = nearby_Facility_20[i]["photos"][0]["width"]
#     resultDict["locPhotoUrl"] = "https://maps.googleapis.com/maps/api/place/photo?key={}&photoreference={}&maxwidth={}".format(GOOGLE_API_KEY,resultDict["locPhoto_reference"], resultDict["locPhoto_width"])
