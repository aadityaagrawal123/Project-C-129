from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

source_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome("chromedriver.exe")
browser.get(source_url)

time.sleep(10)

scraped_data = []
stars_data = []

def scrape():
    soup = BeautifulSoup(browser.page_source, "html.parser")

    bright_star_table = soup.find("table", attrs={"class","wikitable"})
    table_body = bright_star_table.find("tbody")
    table_rows = table_body.find("tr")

    for row in table_rows:
               
        columns = row.find_all("td")
        print(columns)

        temp_list = []

        for col_data in columns:
            data = col_data.text.strip()
            print(data)
            temp_list.append(data)

        scraped_data.append(temp_list)


    for i in range(0, len(scraped_data)):
        Star_names = scraped_data[i][1]
        Distance = scraped_data[i][3]
        Mass = scraped_data[i][5]
        Radius = scraped_data[i][6]
        Luminosity = scraped_data[i][7]

        required_data = [Star_names, Distance, Mass, Radius, Luminosity]
        stars_data.append(required_data)

scrape()
headers = ["Star_Name", "Distance", "Mass", "Radius", "Luminosity"]
data_file = pd.DataFrame(stars_data, columns=headers)
data_file.to_csv('bright_stars_data.csv', index=True, index_label="id")