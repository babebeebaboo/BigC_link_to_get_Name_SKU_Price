import requests
import time
from bs4 import BeautifulSoup
def get(file):
    link = input()
    session_requests = requests.session()
    #print("LINK: "+ link)

    result = session_requests.get(link)
    #print(result.text)
    
    soup = BeautifulSoup(result.text,"html.parser")
    #print(soup.text)
    
    
    title = soup.find("h1", {"class": "h1"}).text
    #title = title.split("ซื้อ")[1]
    #title = title.split("ราคาถูก")[0]
    #print(title+"\t")
    title = title.replace("\n","")
    file.write(title+"\t")

    
    sku = soup.find("span", {"class": "sku-product"}).text
    sku = sku.split(":")[1]
    sku = sku.replace(" ","")
    sku = sku.replace("\n","")
    file.write(sku+"\t")

    price = soup.find("span", {"class": "price"}).text
    price = price.replace("฿","")
    price = price.replace("\n","")
    file.write(price+"\n")

    
    

def main():
    m = int(input())
    f = open("output.txt","a")
    for i in range(0,m):
        get(f)

if __name__ == '__main__':
    main()
    
