from bs4 import BeautifulSoup
import requests
import time

def find_jobs():
    html_text = requests.get('https://www.indeed.com/q-Python-jobs.html').text
    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.select('div[class*="result job_"]')
    print(len(jobs))


    for index, job in enumerate(jobs):
        job_title = job.select('span[id*="jobTitle-"]')[0].get_text()
        url = "https://www.indeed.com/viewjob?" + job.find('h2', class_ = "jobTitle").a['href'].split("?")[1]
        company_name = job.find('span', class_ = 'companyName')
        if(company_name.find('a') != None):
            company_name = company_name.find('a').text
        else:
            company_name = company_name.text
        
        print(f"Company Name: {company_name}\nJob Title: {job_title}\nURL: {url}")
        with open(f"jobs/{index}.txt", 'w', encoding="utf-8") as f:
            f.write(f"Company Name: {company_name}\nJob Title: {job_title}\nURL: {url}")
        print("File Saved...")    
# Run the code every 10 minutes
if __name__ == '__main__':
    while True:
        find_jobs()
        time.sleep(60)