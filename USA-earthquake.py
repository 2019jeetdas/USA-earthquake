# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

df = pd.read_excel('/home/jeet/Desktop/USA_earthquake.xlsx')

# converting excel file to csv file 

df.to_csv("/home/jeet/Desktop/USA_earthquake.csv", encoding='utf-8',sep=',',index=False)

print("\n------- output data :-----------\n")
print("USA Earthquake data analysis:")
print("\n-----------------------------------\n")


df=pd.read_csv("/home/jeet/Desktop/USA_earthquake.csv", encoding='utf-8')

#------------ Operations : ------------------------

#-------- Question-00 --------------------

# Question – A : get row and column numbers 

print('---------------------------------------------')
print("Dimension of the data frame = ",df.shape)
print('---------------------------------------------')

# Question – B : print column names :

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")


#------------ Question -01 ------------------------
#----- Yearwise number of Earthquakes & total no. -----

df_yearwise = df.groupby(['YEAR'])[['MONTH']].count()
print(df_yearwise)
print("--------------------------------------\n")
print("Total number of Earthquake = \n",sum(df_yearwise))

plt.title("[Question-01] Number of Earthquakes yearwise ")
plt.xlabel("Year --->")
plt.ylabel("No. of Earthquakes ---->")
plt.plot(df_yearwise)
plt.show()

#---- Question-02-- Earthquake date and time ------

year = df['YEAR'].replace(np.nan,0)
month = df['MONTH'].replace(np.nan,0) 
day = df['DAY'].replace(np.nan,0)

hour = df['HOUR'].replace(np.nan,0)
minute = df['MINUTE'].replace(np.nan,0)
sec = df['SECOND'].replace(np.nan,0)

print("\t Earthquake Date and Time : \n")
print("---------------------------------------------------------------")

for i in range(4001,8001):
    print("Earthquake = [ ",i," ]\tYear = ",
           int(year[i]),"\tMonth = ",int(month[i]),"\tDay = ",int(day[i]),
            "------>",
        int(hour[i])," Hour \t",int(minute[i])," Minute\t",int(sec[i])," Sec.")
    

#------- Question-03 : Source [latitude & longitude]------


lat = df['LATITUDE'].replace(np.nan,0)
lon = df['LONGITUDE'].replace(np.nan,0)

plt.title("[ Question - 03 ] : Earthquake source plotting")
plt.xlabel("latitude --->")
plt.ylabel("longitude --->") 
plt.scatter(lat,lon)
plt.show()

#--------- Question-04 : Epic distance and city(latitude & longitude)----

print("\tPrint Epic Distance :\n-------------------------------------------\n")
epic = df['EPIDIST'].replace(np.nan,0)

for i in range(0,157015):
    print("Earthquake = [ ",i," ] ----> Epic Distance = ",epic[i])

plt.title("[ Question - 04 ] : Earthquake Epic Distance plotting")
plt.xlabel("sl. no --->")
plt.ylabel("Epic Distance --->") 
plt.plot(epic)
plt.show()

#-------- Question-05 : Earthquake City position plotting [where observed] ------

c_lat = df['CITY_LAT'].replace(np.nan,0)
c_lon = df['CITY_LON'].replace(np.nan,0)

plt.title("[ Question - 05 ] : Earthquake City position plotting")
plt.xlabel("latitude --->")
plt.ylabel("longitude --->") 
plt.scatter(c_lat,c_lon)
plt.show()

#------ Question-06 : Earthquake address---

city = df['CITY']
state = df['STATE']
country = df['COUNTRY']

print("Earthquake information :\n----------------------------")

for i in range(0,4500):
    print("Earthquake = [ ",i," ]\n")
    print("City = ",city[i])
    print("State = ",state[i])
    print("Country = ",country[i])
    print("----------------------------\n")


