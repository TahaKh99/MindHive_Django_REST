import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MindHive.settings')
django.setup()

from geopy.geocoders import Nominatim
from main.models import Outlet
from time import sleep

def geocode_address(geolocator, address):
    address_parts = address.split(',')
    for i in range(len(address_parts)):
        try:
            simplified_address = ','.join(address_parts[i:]).strip()
            location = geolocator.geocode(simplified_address, timeout=10)  # Increased timeout
            if location:
                return location.latitude, location.longitude
        except Exception as e:
            print(f"Error during geocoding: {e}")
            continue
    return None, None

def geocode_using_name(geolocator, name):
    try:
        location = geolocator.geocode(name, timeout=10)
        if location:
            return location.latitude, location.longitude
    except Exception as e:
        print(f"Error during geocoding by name: {e}")
    return None, None

def geocode_outlets():
    geolocator = Nominatim(user_agent="geocodingAgent")
    outlets = Outlet.objects.filter(latitude__isnull=True, longitude__isnull=True)

    for outlet in outlets:
        latitude, longitude = geocode_address(geolocator, outlet.address)
        if not latitude or not longitude:
            print(f"Address-based location not found for: {outlet.address}. Trying by name.")
            clean_name = outlet.name.replace('ZUS Coffee – ', '').strip()
            latitude, longitude = geocode_using_name(geolocator, clean_name)

        if latitude and longitude:
            outlet.latitude = latitude
            outlet.longitude = longitude
            outlet.save()
            print(f"Geocoded: {outlet.name}")
        else:
            print(f"Location not found for: {outlet.name}")

        sleep(1)  # To avoid hitting request limits

if __name__ == "__main__":
    geocode_outlets()
