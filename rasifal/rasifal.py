import requests
from bs4 import BeautifulSoup
import json

data = {}


def get_rasifal():
    html = requests.get('https://www.hamropatro.com/rashifal').text
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='item')
    for item in items:
        data[item.find('h3').text] = item.find('p').text
    return data
