from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from pandas.io.html import read_html
import pandas
import lxml
import re
import csv




def find_season_table(my_url,next_season_name):
    print("find_season_table: Start of function")
    wikitables= read_html(my_url, index_col=0, attrs={"class": "wikitable"})
    table_found = False
    table_number = 1
    while not table_found:
        if wikitables[table_number].columns[table_number] == "Pld":
            season_table = wikitables[table_number]
            print(season_table)
            table_found = True
        table_number = table_number + 1



    season_table.to_csv(next_season_name+".csv", index=False) #Change the name of the csv file
    print("find_season_table: End of function")


def change_url(season_html):
    print("change_url: Start of function")
    season_infobox =season_html.find(class_="infobox")
    next_season = season_infobox.find_all("a")
    
    next_season_url = next_season[-1].get("href")
    print("File in next_season_url" , "File" in next_season_url)
    if not "%" in next_season_url:
        next_season_url = next_season[-2].get("href")
    if not "%" in next_season_url:
        next_season_url = next_season[-3].get("href")
    if "2021" in next_season_url:
        next_season_url = ""

  
    season_first_year = str(next_season_url[6:10])     # Finds the name of the season***************************************************
    next_season_name = (season_first_year+"-"+(str(int(season_first_year)+1)))
    print(next_season_url)

    print("change_url: End of function")
    return next_season_url, next_season_name

def prepare_data(my_url):
    print("prepare_data: Start of function")
    web_page_url = uReq(my_url)
    web_page_html = web_page_url.read()
    web_page_url.close()
    season_html = soup(web_page_html, "html.parser")
    print("prepare_data: End of function")
    return season_html



def main():
    print("Main: Start of function")
    my_url = "https://en.wikipedia.org/wiki/1937%E2%80%9338_Football_League" #First season 
    print(my_url[30:34])
    find_season_table(my_url,my_url[30:34] ) # This section must be changed to the year of the start
    season_html = prepare_data(my_url)
    next_season_url, next_season_name = change_url(season_html)

    print("Main: Before while-loop")
    while next_season_url: #Loops for all seasons as long as there is a next season
        print("Starting to process season: ", next_season_url)
        my_url = "https://en.wikipedia.org/"
        my_url =  my_url + next_season_url
        find_season_table(my_url, next_season_name)
        season_html = prepare_data(my_url)

        next_season_url = change_url(season_html)

        next_season_url, next_season_name  = change_url(season_html)
        
        
    print("Main: End of function")



main()




# season_infobox = season_html.findAll("table", {"class": "infobox"})

# h_ref_soup_linnea = season_html.find("a",attrs={"href" : re.compile("^http://")})
# print(h_ref_soup_linnea)

# # ***************************************************Finds the url for next season above



# h_ref = read_html(my_url, index_col=0, attrs={"class": "infobox"})

# wikitables= read_html(my_url, index_col=0, attrs={"class": "wikitable"})


#
# print("Extracted {num} wikitables".format(num=len(wikitables)))

# print(wikitables[0])


# # Ladda ner datan frp, webbsodam
# web_page_url = uReq(my_url)
# web_page_html = web_page_url.read()
# web_page_url.close()
# page_soup = soup(web_page_html, "html.parser")
# # print(page_soup.h1) # hämtar headings

# "grabs each table"
# tables = page_soup.findAll("table", {"class": "wikitable"})

# table = (tables[3].shape)µ
# print(table)
# # rows = table.findAll("tr")
# # rows = table.findAll("th")
# # rows = table.findAll("title")

# # print(rows)

# # for row in rows:
# #     team = row.findAll("a")
# #     team = team.find("title")
# #     print(team)