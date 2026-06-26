#from click import option
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pandas as pd


website = "https://www.thesun.co.uk/sports/football/"

# Headless mode
options = Options()
options.add_argument("-headless")

# Creating the Driver
driver = webdriver.Firefox(options=options)
driver.get(website)

# Finding the containers that hold the headlines, subtitles, and links
containers = driver.find_elements(by='xpath', value="//div[@class = 'story__copy-container']")


# Extracting the headlines, subtitles, and links from the containers
titles = []
subtitles = []
links = []

for container in containers:
    title = container.find_element(by='xpath', value="./a/p").text
    subtitle = container.find_element(by='xpath', value='./a/h3').text
    link = container.find_element(by='xpath', value='./a').get_attribute('href')

    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)


# Creating a dictionary and converting it to a DataFramer
my_dict = {'titles':titles, 'subtitles':subtitles, 'links':links}

df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv('headline-headless.csv', index=False)

driver.quit()