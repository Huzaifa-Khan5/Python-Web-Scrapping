import requests
from bs4 import BeautifulSoup

def raw_data():
    response=requests.get("https://scrapethissite.com/pages/advanced/?gotcha=csrf")
    return response.content.decode()

def parsed_data(response):
    soup=BeautifulSoup(response,"html.parser")
    csrf=soup.select_one('input[name="csrf"]')["value"]
    return csrf

def main():
    load={"user": "huzaifa",
    "pass": "123456",}
    with requests.session() as s:
        response=raw_data() 
        parsed=parsed_data(response)
        load["csrf"]=parsed
        rett=s.post("https://scrapethissite.com/pages/advanced/?gotcha=csrf",data=load)
        print(rett.content)

if __name__ == "__main__":
    main()