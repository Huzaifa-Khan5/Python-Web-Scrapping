import requests
from bs4 import BeautifulSoup
from csv import DictWriter
import json

def raw_data(url):
    response=requests.get(url)
    return response.content.decode()

def parsed_data():
    base_url="https://scrapethissite.com/pages/ajax-javascript/#"
    page_url=""
    
    film_data=[]
    response=raw_data(base_url+page_url)
    soup=BeautifulSoup(response,"html.parser")
    years=soup.select(".year-link")
    for year in years:
        base_url="https://scrapethissite.com/pages/ajax-javascript/?ajax=true&year="
        page_url=year.text
        print(page_url)
        response=raw_data(base_url+str(page_url))
     
        films_data=json.loads(response)
        for film in films_data: 
            film_data.append({"title":film['title'],"nomination":film['nominations'],"awards":film['awards'],"year":film["year"]})
    return film_data
    

def main():   
    parsed=parsed_data()
    with open("films.csv","w") as file:
        writer=DictWriter(file,fieldnames=["title","nomination","awards","year"])
        writer.writeheader()
        for i in parsed:
            writer.writerow(i)

if __name__ == "__main__":
    main()