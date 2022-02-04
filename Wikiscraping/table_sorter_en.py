import pandas as pd
import numpy as np
from glob import glob
import openpyxl
import os


print("starting the porogram")


#Importing all my Excel files#

all_csv_sheets = sorted(glob("British_Premier_Leauge_raw\*.csv"))
length = len(all_csv_sheets)
# print(all_csv_sheets)

file_names = [os.path.basename(x) for x in glob("British_Premier_Leauge_raw\*.csv")]

column_names = [i.strip(".csv") for i in file_names]


#print(column_names)

season_list = []
for l in range(len(all_csv_sheets)):  #  reading all files in folder tables
    current_sheet_read = pd.read_csv(all_csv_sheets[l], encoding="latin1")    
    # current_sheet_read.rename(columns={current_sheet_read.columns[1]:"Team"}, inplace=True)
    sorted_table = current_sheet_read[["Team","Pts","HW", "AW"]]
    sorted_table["Team"].apply(str)
    sorted_table["Pts"] = sorted_table["Pts"].apply(str)
    sorted_table["HW"] = sorted_table["HW"].apply(str)
    sorted_table["AW"] = sorted_table["AW"].apply(str)
    print(sorted_table)
    

    #print("Loops for the ",i," time")

    for i in range(len(sorted_table.columns)):
        for j in range(len(sorted_table.index)):
            k = 0
            while k < len(sorted_table.iloc[j,i]):
                if sorted_table.iloc[j,i][k]  == "(" or sorted_table.iloc[j,i][k] == "[":
                    sorted_table.iat[j,i] = sorted_table.iat[j,i][0:k]
                    k = len(sorted_table.iloc[j,i])+110
                if sorted_table.iat[j,i][-1]  == " ":

                    sorted_table.iat[j,i] = sorted_table.iat[j,i][0:-1]

                    k = len(sorted_table.iloc[j,i])+110
                k = k+1
    sorted_table["Pts"] = sorted_table["Pts"].apply(float)
    sorted_table["HW"] = sorted_table["HW"].apply(float)
    sorted_table["AW"] = sorted_table["AW"].apply(float)



    if int(column_names[l][0:4]) < 1981:
        sorted_table["Pts"] = sorted_table["Pts"] + sorted_table["HW"] + sorted_table["AW"]
        sorted_table = sorted_table.drop(columns=["HW"])
        sorted_table = sorted_table.drop(columns=["AW"])
        sorted_table = sorted_table.rename(columns={"Pts": column_names[l]})
        print("2 point system")
    else:
        print("3 point system")
        sorted_table = sorted_table.drop(columns=["HW"])
        sorted_table = sorted_table.drop(columns=["AW"])
        sorted_table = sorted_table.rename(columns={"Pts": column_names[l]})

    print(sorted_table)
        

    season_list.append(sorted_table)
    print(season_list)




    

merged_list = season_list[0] #This is a help variable. To be filled in
for i in range(len(season_list)-1):
    seasons = pd.merge(merged_list,season_list[i+1], left_index= True, right_index= False, how ="outer", on="Team") 
    merged_list = seasons

final_merged_list = seasons.fillna(0) #Fills empty cells with 0

final_merged_list.to_excel("Premier_league_all_seasons.xlsx", index = False)
print("File was successfully saved")