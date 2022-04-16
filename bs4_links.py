import time
import requests
from bs4 import BeautifulSoup

links=[]

def httplinks():
    for link in links:
        if "http://" in link:
            print(link)
            
def httpslinks():
    for link in links:
        if "https://" in link:
            print(link)    
    
def main():
    response=requests.get("https://www.google.com")
    print("requesting google...")
    time.sleep(2)
    src=response.content
    parsed_content=BeautifulSoup(src,"html.parser")
    for anchor_tag in parsed_content.find_all("a"):
        links.append(anchor_tag.attrs["href"])
    print("\n")
    print("http links")
    time.sleep(2)
    httplinks()
    print("\n")
    print("https links")
    time.sleep(2)
    httpslinks()
    
if __name__=="__main__":
    main()