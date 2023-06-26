# This is a practice project for learning the basics of web scraping from https://realpython.com/beautiful-soup-web-scraper-python/
# The program scrapes a fake jobs website and generates only the title of the position, the company's name, the location and a link to apply to the job
# Mazen Meziad
import requests
from bs4 import BeautifulSoup

# website being scraped
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# storing the entire html into a BeatifulSoup object
soup = BeautifulSoup(page.content, "html.parser")

# Filtering to leave only the "cards of information" as displayed in the website
results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="card-content")

# filtering to find all job postings with "python" in their position title
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
                               )

# grabbing the 3rd parents of the divs that contain "python in their position title
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

# stripping and printing only the title, company, location and link to the job application
for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    link_url = job_element.find_all("a")[1]["href"]
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print(f"Apply here: {link_url}\n")
    print()



# print(len(python_jobs))

# for job_element in python_job_elements:
#     link_url = job_element.find_all("a")[1]["href"]
#     print(f"Apply here: {link_url}\n")

        # for job_element in python_job_elements:
        #     links = job_element.find_all("a")
        #     for link in links:
        #         link_url = link["href"]
        #         print(f"Apply here: {link_url}\n")


        # if link.__contains__("Apply"):
        #     print(f"Apply here: {link_url}\n")
        # else:
        #     print(f"Learn here: {link_url}\n")

#

# print(results.prettify())
# print(location_element, end="\n")
