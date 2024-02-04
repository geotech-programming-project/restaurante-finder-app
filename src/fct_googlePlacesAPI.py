import pandas as pd
import googlemaps
from datetime import datetime
import csv


# api_key = 'YOUR_API_KEY'
gmaps = googlemaps.Client(key=api_key)

places_result = gmaps.places(query='restaurants', location=(38.731352, -9.160070), radius=1000)

csv_file_path = 'restaurants_near_novaims.tsv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['Name', 'Address', 'Place_ID', 'Phone_Number', 'Rating', 'Website', 'Price_Level', 'Opening_Hours', 
                  'Types', 'Latitude', 'Longitude', 'User_Ratings_Total', 'Business_Status']
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter='\t')
    
    csv_writer.writeheader()

    # Write place details to CSV
    for place in places_result['results']:
        place_id = place['place_id']
        place_details = gmaps.place(place_id=place_id)['result']
        
        csv_writer.writerow({
            'Name': place['name'],
            'Address': place['formatted_address'],
            'Place_ID': place_id,
            'Phone_Number': place_details.get('formatted_phone_number', 'N/A'),
            'Rating': place_details.get('rating', 'N/A'),
            'Website': place_details.get('website', 'N/A'),
            'Price_Level': place_details.get('price_level', 'N/A'),
            'Opening_Hours': place_details.get('opening_hours', {}).get('weekday_text', 'N/A'),
            'Types': ', '.join(place_details.get('types', [])),
            'Latitude': place_details.get('geometry', {}).get('location', {}).get('lat', 'N/A'),
            'Longitude': place_details.get('geometry', {}).get('location', {}).get('lng', 'N/A'),
            'User_Ratings_Total': place_details.get('user_ratings_total', 'N/A'),
            'Business_Status': place_details.get('business_status', 'N/A')
        })

        print(f"Name: {place['name']}")
        print(f"Address: {place['formatted_address']}")
        print(f"Place ID: {place_id}")
        print(f"Phone Number: {place_details.get('formatted_phone_number', 'N/A')}")
        print(f"Rating: {place_details.get('rating', 'N/A')}")
        print(f"Website: {place_details.get('website', 'N/A')}")
        print(f"Price Level: {place_details.get('price_level', 'N/A')}")
        print(f"Opening Hours: {place_details.get('opening_hours', {}).get('weekday_text', 'N/A')}")
        print(f"Types: {', '.join(place_details.get('types', []))}")
        print(f"Latitude: {place_details.get('geometry', {}).get('location', {}).get('lat', 'N/A')}")
        print(f"Longitude: {place_details.get('geometry', {}).get('location', {}).get('lng', 'N/A')}")
        print(f"User Ratings Total: {place_details.get('user_ratings_total', 'N/A')}")
        print(f"Business Status: {place_details.get('business_status', 'N/A')}")
        print("\n")

print(f"Data has been saved to {csv_file_path}")
