import pandas as pd
import numpy as np
from glob import glob
import openpyxl
import os


#Importing TOJ-report#

TOJ_report = sorted(glob("December\*.xls"))
print(TOJ_report)
# length = len(all_csv_sheets)
# print(all_csv_sheets)

# file_names = [os.path.basename(x) for x in glob("Serie_A_raw\*.csv")]
# column_names = [i.strip(".csv") for i in file_names]

# point_system_change = int(input("Which year did the league change from a 2 to three point system? Write in format YYYY: "))

# #print(column_names)

# season_list = []
# for l in range(len(all_csv_sheets)):  #  reading all files in folder tables
#     current_sheet_read = pd.read_csv(all_csv_sheets[l], encoding="latin1")    
#     # current_sheet_read.rename(columns={current_sheet_read.columns[0]:"Team"}, inplace=True)
#     sorted_table = current_sheet_read[["Team","Pts","W"]]
#     sorted_table["Team"] = sorted_table["Team"].apply(str)
#     sorted_table["Pts"] = sorted_table["Pts"].apply(str)
#     sorted_table["W"] = sorted_table["W"].apply(str)
    

#     #print("Loops for the ",i," time")

#     for i in range(len(sorted_table.columns)):
#         for j in range(len(sorted_table.index)):
#             k = 0
#             while k < len(sorted_table.iloc[j,i]):
#                 if sorted_table.iloc[j,i][k]  == "(" or sorted_table.iloc[j,i][k] == "[":
#                     sorted_table.iat[j,i] = sorted_table.iat[j,i][0:k]
#                     k = len(sorted_table.iloc[j,i])+110
#                 if sorted_table.iat[j,i][-1]  == " ":

#                     sorted_table.iat[j,i] = sorted_table.iat[j,i][0:-1]

#                     k = len(sorted_table.iloc[j,i])+110
#                 k = k+1
#     sorted_table["Pts"] = sorted_table["Pts"].apply(float)
#     sorted_table["W"] = sorted_table["W"].apply(float)



#     if int(column_names[l][0:4]) < point_system_change:
#         sorted_table["Pts"] = sorted_table["Pts"] + sorted_table["W"]
#         sorted_table = sorted_table.drop(columns=["W"])
#         sorted_table = sorted_table.rename(columns={"Pts": column_names[l]})
#         print("2 point system")
#     else:
#         print("3 point system")
#         sorted_table = sorted_table.drop(columns=["W"])
#         sorted_table = sorted_table.rename(columns={"Pts": column_names[l]})

#     print(sorted_table)
        

#     season_list.append(sorted_table)




    

# merged_list = season_list[0] #This is a help variable. To be filled in
# for i in range(len(season_list)-1):
#     seasons = pd.merge(merged_list,season_list[i+1], left_index= True, right_index= False, how ="outer", on="Team") 
#     merged_list = seasons
 

# final_merged_list = seasons.fillna(0) #Fills empty cells with 0

# final_merged_list.to_excel("Serie_A_final_all_seasons.xlsx", index = False)
# print("File was successfully saved")