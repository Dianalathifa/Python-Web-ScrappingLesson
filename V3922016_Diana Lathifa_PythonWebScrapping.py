#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup as bs

URL = "https://proxyway.com/reviews"

print("\n")
print("Scraping images from:", URL, "\n")

req = requests.get(URL)
soup = bs(req.text, 'html.parser')

images = soup.find_all('img')

for i, image in enumerate(images):
    if 'src' in image.attrs:
        image_url = image['src']
        print(f"Image {i+1}: {image_url}")


# In[3]:


import requests
from bs4 import BeautifulSoup as bs
import csv

URL = "https://proxyway.com/reviews"

print("\n")
print("Scraping images from:", URL, "\n")

req = requests.get(URL)
soup = bs(req.text, 'html.parser')

images = soup.find_all('img')

# Menyiapkan file CSV
csv_file = open('image_urls.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Image', 'URL'])

for i, image in enumerate(images):
    if 'src' in image.attrs:
        image_url = image['src']
        csv_writer.writerow([f"Image {i+1}", image_url])

# Menutup file CSV
csv_file.close()

print("Data telah disimpan ke dalam file image_urls.csv")


# In[ ]:




