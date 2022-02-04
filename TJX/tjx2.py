# from urllib import request
# from urllib.request import urlopen as uReq
from urllib.request import CacheFTPHandler
from pandas.core.algorithms import unique
import requests
from bs4 import BeautifulSoup
from pandas.io.html import read_html
import pandas as pd
import lxml
import re
import sys
import csv
from requests.api import head
import urllib.request

def Get_ExcelSheet():
    current_url = "manifest.xlsx"
    manifest = pd.read_excel(current_url) #change this so one can upload a toj file in the future 
    return manifest


def CreateListOfHSCodes(manifest):
    length = (len(manifest["EU_HS_Code"]))
    # print("Number of lines ",length)
    unique_values = (manifest["EU_HS_Code"].unique())
    return unique_values

def GetDutyRate(unique_hs_codes_list):  
    duty_rate_dict = {}
    for HScode in unique_hs_codes_list:
        try:

            # Reading the data inside the xml file to a variable under the name  data
            with open('test.xml.rdf', 'r') as f:
                x = f.read() 
                print(x)

            # # Passing the stored data inside the beautifulsoup parser 
            x = BeautifulSoup(x, 'xml') 
            print(x)

            
            # base_URL_first_part = "https://ec.europa.eu/taxation_customs/dds2/taric/measures.jsp?Lang=en&SimDate=20211121&Area=&MeasType=&StartPub=&EndPub=&MeasText=&GoodsText=&op=&Taric=640110"
            # base_URL_last_part = "&search_text=goods&textSearch=&LangDescr=en&OrderNum=&Regulation=&measStartDat=&measEndDat="
            # base_URL = (base_URL_first_part+ (str(HScode))+base_URL_last_part)
            # #print(base_URL) #funkar, här finns 17,00
            # get_html = requests.get(base_URL)


            # #test code
            # my_request = urllib.request.urlopen(base_URL)
            # my_HTML = my_request.read().decode("utf8")
            # print(my_HTML)




            #print(get_html.text) #funkar ej, här finns inte 17,00
            current_html = BeautifulSoup(get_html.content, features="lxml")
            # x = current_html.find("div", {"id": "div_measures_for_6110309900"})


            #print(current_html)

  
            

        
            # duty_tag = match.find("p").find_next_sibling('p').find_next_sibling("p")
            # duty_rate = (float(duty_tag.find("span").getText()))
            # duty_rate_dict[HScode] = duty_rate/100
        except:
            bajs = 1
            print("Not possible to get duty rate for commodity code; ", HScode)
    print(duty_rate_dict)
    return duty_rate_dict

def MatchCommdityCodewithDutyRate(manifest, duty_rate_dict):
    position = 0
    print("start to match duty")
    for row in range(len(manifest)):
        if manifest.iloc[position,0] in duty_rate_dict: #Här vill jag att den ska slå upp något i dictet vilket den inte verkar kunna göra
            current_key = manifest.iloc[position,0]
            # print(duty_rate_dict[current_key[position]])
            manifest.at[position,"EU_duty_rate"] = duty_rate_dict[current_key] 
        else:
            manifest.at[position,"EU_duty_rate"] = -1
        position = position + 1
    print("this is the length of manifest", len(manifest), "this is the last", row, "this is the lenght of duty rate dict,", len(duty_rate_dict.keys()))


    manifest.to_excel("test.xlsx", index=False)
    print("File saved")




def main():
    print("Main: Start of function")
    manifest = Get_ExcelSheet() #Gets the excelsheet with hs codes
    unique_hs_codes_list =CreateListOfHSCodes(manifest) # Extracts the unique hs codes from manifest
    duty_rate_dict = GetDutyRate(unique_hs_codes_list)  # Gets the duty rate for a all hs codes
    # MatchCommdityCodewithDutyRate(manifest, duty_rate_dict)
    # print("Main: End of function")
    
main()