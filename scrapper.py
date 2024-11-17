import requests
from bs4 import BeautifulSoup


all_jobs = []

# scrap, print list
def html_scrapper(url):
    response = requests.get(url)
    soup = BeautifulSoup(
    response.content,
    "html.parser",
    )

    job_list = soup.find("section", class_="jobs").find_all("li")[1:-1]
    
    for job in job_list:
        job_title = job.find("span", class_="title").text
        job_company, job_position, job_region = job.find_all("span", class_="company")
        job_url = job.find("div", class_="tooltip--flag-logo").next_sibling["href"]

        print(
            "\n",
            "<",job_title,">\n",
            "region : ", job_region.text,"\n",
            "company name : ", job_company.text,"\n",
            "position : ", job_position.text,"\n",
            "url : " , f"https://weworkremotely.com{job_url}","\n"
        )

#check nuber of pages
first_page = requests.get("https://weworkremotely.com/remote-full-time-jobs?page=1")
howmany = BeautifulSoup(
first_page.content,
"html.parser",
)

page_list = howmany.find("div", class_="pagination").find_all("span", class_="page")

# scrape each page
for page in page_list:
    currentpage = str(page_list.index(page) + 1)
    url = "https://weworkremotely.com/remote-full-time-jobs?page=" + currentpage
    print("[page", page_list.index(page)+1 ,"]")
    html_scrapper(url)


# ----------------------------------------------- #
