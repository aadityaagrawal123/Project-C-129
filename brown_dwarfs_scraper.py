from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

source_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

browser = webdriver.Chrome("chromedriver.exe")
browser.get(source_url)

time.sleep(10)

scraped_data = []
stars_data = []

def scrape():

    page = requests.get("https://en.wikipedia.org/wiki/List_of_brown_dwarfs")

    soup = BeautifulSoup(page.content, "html.parser")

    temp_list = []
    for tr_tag in soup.find_all("table"):
        tr_tags = tr_tag.find_all("tr")

    for td_tag in tr_tags:
        td_rows = td_tag.find_all('td')
        row_data = td_rows.strip()
        print(row_data)
        temp_list.append(row_data)
    
    scraped_data.append(temp_list)


    for i in range(0, len(scraped_data)):
        Star_names = scraped_data[i][1]
        Radius = scraped_data[i][9]
        Mass = scraped_data[i][8]
        Distance = scraped_data[i][6]

        required_data = [Star_names, Radius, Mass, Distance]
        stars_data.append(required_data)

scrape()
headers = ["Star_names", "Radius", "Mass", "Distance"]
stars_data_file = pd.DataFrame(stars_data, columns=headers)
stars_data_file.to_csv('stars_scraped_data.csv', index=True, index_label="id")