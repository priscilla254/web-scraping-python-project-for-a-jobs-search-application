from bs4 import BeautifulSoup
import requests
import time

print('put some skill that you are unfamiliar wuth')
unfamiliar_skill=input('>')
print(f'filtering out {unfamiliar_skill}')

def find_jobs():
    html_text=requests.get('https://www.timesjob.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=', verify=False).text
    soup=BeautifulSoup(html_text,'lxml')
    jobs=soup.find_all('li',class_="clearfix job-bx wht-shd-bx")
    for index, job in enumerate(jobs):
        published_date=job.find('span',class_="sim-posted").span.text
        if 'few' in published_date:
            company_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
            skills=job.find('span', class_="srp-skills").text.replace(' ','')
            more_info=job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt','w') as f:

                    f.write(f"Company name: {company_name.strip()}\n")
                    f.write(f"Skills required: {skills.strip()}\n")
                    f.write(f"More info:{more_info}")
                print(f"file saved: {index}")

 if __name__ ==' __main__':
     while True:
        find_jobs()
         time_wait=10
         print(f'waiting {time_wait} minutes.....')
         time.sleep(time_wait)