import csv

import requests
from bs4 import BeautifulSoup

Base_URL = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='

source = requests.get(Base_URL).text
soup = BeautifulSoup(source, 'lxml')

jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
for job in jobs:
    updated_time = job.find('span', class_='sim-posted').text.replace(' ', '')
    if 'few' in updated_time:
        comp_name = job.find('h3').text
        skills = job.find('span', class_='srp-skills').text
        more_info = job.find('h2').a['href'].replace(' ', '')
        with open('TimesJob_scrap.csv', mode='w') as csv_file:
            field_names = ["Company", "Required skills", "For more information"]
            writer = csv.DictWriter(csv_file, fieldnames=field_names)
            writer.writeheader()
            writer.writerow({'Company': f'{comp_name}', 'Required skills': f'{skills}', 'For more information': f'{more_info}'})


