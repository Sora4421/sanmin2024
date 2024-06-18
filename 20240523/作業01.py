# -*- coding: utf-8 -*-
"""
Created on Mon May 27 22:25:14 2024

@author: User
"""

import requests
import json

# Function to fetch bike data
def fetch_bike_data(url):
    response = requests.get(url)
    data = response.text
    bike_data = json.loads(data)
    return bike_data

# Function to get all unique areas from the data
def get_all_areas(bike_data):
    areas = set()
    for item in bike_data:
        areas.add(item.get('sarea', '未知區域'))
    return list(areas)

# Function to filter and display bike data based on the user's choice
def display_filtered_data(bike_data, choice, selected_area):
    for item in bike_data:
        sarea = item.get('sarea', '未知區域')
        if sarea == selected_area:
            if choice == '借車' and int(item['sbi']) > 0:
                print('區域:', sarea)
                print('站名:', item['sna'])
                print('可借:', item['sbi'])
                print('可停:', item['bemp'])
                print()
            elif choice == '還車' and int(item['bemp']) > 0:
                print('區域:', sarea)
                print('站名:', item['sna'])
                print('可借:', item['sbi'])
                print('可停:', item['bemp'])
                print()

# URL for the dataset
url = "https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/json?size=1000"

# Fetch the bike data
bike_data = fetch_bike_data(url)

# Ask user whether they want to borrow or return a bike
choice = input("請問您要借車還是還車? (輸入 '借車' 或 '還車'): ").strip()

# Get all available areas
areas = get_all_areas(bike_data)
print("可選擇的區域有:")
for i, area in enumerate(areas, start=1):
    print(f"{i}. {area}")

# Ask user to select an area
selected_area_index = int(input("請選擇區域 (輸入數字): ")) - 1
selected_area = areas[selected_area_index]

# Display filtered data based on user's choice and selected area
display_filtered_data(bike_data, choice, selected_area)
