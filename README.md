# Python Job Scraper
### Streamlining Your Job Search with Automated Python Web Scraping

## Overview
This Python script is a lightweight and straightforward tool for scraping Python-related job listings from TimesJobs. It retrieves job postings that have been updated recently, extracts key details like company name, skills required, and a direct link to the job posting, and saves this information to a CSV file.

## Features
- **Fetch and Parse:** Utilizes `requests` and `BeautifulSoup` to fetch and parse job data from TimesJobs.
- **Filter Recent Listings:** Only includes job listings that have been updated 'recently', to ensure the relevance of the search.
- **CSV Output:** Outputs the scraped job details into a `TimesJob_scrap.csv` file, making it easy to browse and analyze the data offline.

## Requirements
To run this script, you will need the following:
- Python 3.x
- `requests` library
- `beautifulsoup4` library

Install the required libraries using pip:
```console
foo@bar:~$ pip install requests beautifulsoup4
```

## Usage
To use this scraper, simply run the script:
```console
foo@bar:~$ python scraping.py
```


The script will automatically fetch the latest Python-related job postings and save them to a file named `TimesJob_scrap.csv` in your working directory.

## Customization
You can customize the search query by modifying the `Base_URL` in the script to include different keywords or locations as per your specific requirements.

## Contributing
Feel free to fork this project and submit pull requests or suggest new features by opening issues.

## License
This project is open-sourced under the MIT License.




