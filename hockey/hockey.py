import requests 
from bs4 import BeautifulSoup
from csv import DictWriter

def raw_data(url):
    response=requests.get(url)
    return response.content.decode()

def parsed_data():
    base_url="https://scrapethissite.com/pages/forms/?page_num="
    teams_info=[]
    for i in range(1,25):
        page_url=(str(i))      
        print(page_url)
        while True:
            response=raw_data(base_url+page_url)
            soup=BeautifulSoup(response,"html.parser")
            teams=soup.select(".team")    
            for team in teams:  
                name=team.select_one(".name").text.strip()
                year=team.select_one(".year").text.strip()
                wins=team.select_one(".wins").text.strip()
                losses=team.select_one(".losses").text.strip()
                goal_for=team.select_one(".gf").text.strip()
                goal_against=team.select_one(".ga").text.strip()
                teams_info.append({"name":name,"year":year,"wins":wins,"losses":losses,"goal_for":goal_for,"goal_against":goal_against}) 
            break
    return teams_info
        
def main():
    parsed=parsed_data()
    with open("hockey.csv","w") as file:
        writer= DictWriter(file,fieldnames=["name","year","wins","losses","goal_for","goal_against"])
        writer.writeheader()
        for i in parsed:
            writer.writerow(i)
if __name__ == "__main__":
    main()