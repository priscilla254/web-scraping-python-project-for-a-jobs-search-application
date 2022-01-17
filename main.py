from bs4 import BeautifulSoup
import requests

html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

soup=BeautifulSoup(html_text,'lxml')
jobs=soup.find('li',class_="clearfix job-bx wht-shd-bx")
company_name=jobs.find('h3',class_='joblist-comp-name').text.replace(' ','')
print(company_name)

