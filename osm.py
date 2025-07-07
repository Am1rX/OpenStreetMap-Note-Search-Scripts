import requests
from urllib.parse import quote

def search_osm_notes_by_text(query, limit=25):
    encoded_query = quote(query)
    
    url = f"https://api.openstreetmap.org/api/0.6/notes/search.json?q={encoded_query}&limit={limit}"
    
    print(f"Searching for: '{query}'...")

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get('features', [])
    except requests.exceptions.HTTPError as errh:
        print(f"Http Error: {errh}")
    except requests.exceptions.RequestException as err:
        print(f"An Error Occurred: {err}")
    return None

search_term = input("Word >> ")

found_notes = search_osm_notes_by_text(search_term)

if found_notes is not None:
    if not found_notes:
        print("No notes were found with this term.")
    else:
        print(f"\n--- Found {len(found_notes)} results ---")
        for note_feature in found_notes:
            properties = note_feature.get('properties', {})
            geometry = note_feature.get('geometry', {})
            
            note_id = properties.get('id', 'N/A')
            status = properties.get('status', 'unknown')
            
            comments = properties.get('comments', [])
            description = comments[0].get('text', 'No description found.') if comments else 'No description found.'
            
            coordinates = geometry.get('coordinates', [None, None])
            longitude, latitude = coordinates[0], coordinates[1]
            
            print(f"\nNote ID: {note_id}")
            print(f"Status: {status}")
            print(f"Description: {description.strip()}")
            print(f"Location (Lat, Lon): {latitude}, {longitude}")
            print("-" * 20)
#Am1rX
