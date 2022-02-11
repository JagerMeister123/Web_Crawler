from bs4 import BeautifulSoup as bs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests






def Job_offers_by_skill(module_name,country) :
    # Getting the URL :
    if country == "maroc" :
        prefix = "ma."
    elif country == "france" :
        prefix = "fr."
    else :
        prefix =""
    URL = f"https://{prefix}indeed.com/jobs?q={module_name}&l={country}"
    print(URL)
    # Get the HTML string from URL :
    HTML = requests.get(URL).text
    # Turn it into a BeautifulSoup string :
    soup = bs(HTML,'lxml')
    # Find the count in the page and split :
    List = soup.find("div", {"id": "searchCountPages"}).text.split()
    try :
        number = int(List[4])
    except :
        if "," in List[3] :
            x = List[3].split(",")
            Count = int(x[0])*1000 +int(x[1]) 
        else :
            Count = int(List[3])
    else :
        Count = int(List[3])*1000 + number
    return Count








def Data_collection(file_of_skills) :
    with open()
