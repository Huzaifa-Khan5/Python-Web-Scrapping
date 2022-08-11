import requests
from bs4 import BeautifulSoup

def raw_data():
    response=requests.get("https://scrapethissite.com/pages/advanced/?gotcha=login")
    return response.content.decode()
    
def main():
    load={"user": "huzaifa",
    "pass": "123456",
    "csrf": "" }
    with requests.session() as s:
        response=raw_data()
        rett=s.post("https://scrapethissite.com/pages/advanced/?gotcha=login",data=load)
        print(rett.content)


if __name__ == "__main__":
    main()