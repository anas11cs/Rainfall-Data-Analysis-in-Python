import pandas as pd
# A key:value collection of series below
# This static data is to populate dataframe for testing
# pandasVaribale.Series(Parameters)
data = {'Month':pd.Series(['January','Fberuary','March','April','May','June','July'
,'August','September','October','November','December']),'Rainfall':pd.Series([1.65,1.25,1.94,2.75,2.75,3.65,5.05,1.50,1.33,0.07,0.50,2.30]),}

# ============= READING DATA ===============

#Creatingdata frame from the above data
## df=pd.DataFrame(data)

#CreatingData frame from csv fil data
## dfc=pd.read_csv(r'./rain.csv') #Here r is 'raw' so that we can skip escpare character(backslash[/])

#CreatingData frame from json file data
dfj=pd.read_json(r'./data.json')
print("Data Frame : ")
print(dfj,"\n")

# ============= CLEANING DATA ===============

# Nan=NotANumber values-being set to 0
## dfzero=dfj.fillna(0)
## print("NaN Values set to zero\n",dfzero)

# Remove rows that have invalid(missing) data
dfClean = dfj.dropna(0)
print ("Neat Data\n",dfClean)

# ============= DATA ANALYSIS ===============
print("Mean of a data is\n")
print(dfClean.mean())
print("\nMedian of data is\n")
print(dfClean.median())
print("\nStandard Deviation of data from Means is\n")
print(dfClean.std())

# ============= DATA SUBSET AND ANALYSIS ===============
## Rainfall for 1st six months of year and the average rainfall in those months
rainfall=dfClean['Rainfall'][0:6]
print("Rainfall for 1st six months of year is Below\n",rainfall)
print("\nAverage of 1st six months rainfall is : ",rainfall.mean())
## Rainfall and Temperature for 1st six months of year and the average-Rainfall and average-Temperature
temp_rain=dfClean['Temperature','Rainfall'][0:6]
print("Rainfall and Corresponding Temperature for 1st six months is Below\n",temp_rain)
print("\nAverage of 1st six months' Temperature and Rainfall is Below",temp_rain.mean())
## Find the temperature and rainfall for the month of June
forJune=dfClean['Month'] #Selected column of month
forJuneIndex=dfClean.set_index(forJune) #Assigned a label to it
# .loc() requires proper index
print("\nThe temperature and rainfall for the month of June : ",forJuneIndex.loc['March'])