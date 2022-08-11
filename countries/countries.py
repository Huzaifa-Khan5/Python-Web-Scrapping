import requests 
from bs4 import BeautifulSoup
import csv

def country():
    countries=[]
    for name in names:
        countries.append(name.text.strip())
    return countries

def raw_data():
    response=requests.get("https://scrapethissite.com/pages/simple")
    return response.content.decode()

def parsed_data(url):
    global names,countries
    soup=BeautifulSoup(url,"html.parser")
    names=soup.select(".country-name")
    countries=country()
    countries_info=[]   
    infos=soup.select(".country-info")   
    for info in infos:  
        capital=info.select_one(".country-capital").text
        population=info.select_one(".country-population").text
        area=info.select_one(".country-area").text
        countries_info.append({"capital":capital,"population":population,"area":area})
    return countries_info

def main():
    response=raw_data()
    parsed=parsed_data(response)
    with open("huzaifa.csv","w") as file:
        for coun in countries:
            file.write(coun)
        
    list=[parsed]
    for i in list:
        for j in i:
            print(j)
    
    
    


if __name__ == "__main__":
    main()
    