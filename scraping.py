import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MindHive.settings')
django.setup()

import requests
from bs4 import BeautifulSoup
from main.models import Outlet
from django.db.utils import IntegrityError

def scrape_outlets():
    page = 1
    base_url = "https://zuscoffee.com/category/store/melaka/page/"

    while True:
        url = f"{base_url}{page}/"
        response = requests.get(url)

        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.content, 'html.parser')

        outlets = soup.find_all('div', class_='elementor-2883')
        print(len(outlets))

        if not outlets:
            break  

        for outlet in outlets:
            name_container = outlet.find('div', class_='elementor-element-9c1e1c8')
            name = name_container.find('p').get_text(strip=True) if name_container else 'Name not found'

            address_section = outlet.find('section', {'data-id': 'af9e841'})
            address = address_section.find('p').get_text(strip=True) if address_section else 'Address not found'

            print(f"Name: {name}, Address: {address}")  # Debug print

             # Check if the address already exists in the database
            if not Outlet.objects.filter(address=address).exists():
                try:
                    Outlet.objects.create(name=name, address=address)
                    print(f"Added: {name}, Address: {address}")  # Debug print
                except IntegrityError:
                    print(f"Error occurred while adding {name}. Skipping.")
            else:
                print(f"Address already exists: {address}. Skipping.")


        page += 1  # Increment to the next page

if __name__ == "__main__":
    scrape_outlets()
