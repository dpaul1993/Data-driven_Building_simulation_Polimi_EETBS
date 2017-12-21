import pandas as pd, matplotlib.pyplot as plt
pd.set_option('mode.chained_assignment', None)  #---Just to supress copy warning---
DataFolderPath="C:/Users/Debayan/Dropbox (Personal)/Data-driven_Building_simulation_Polimi_EETBS/Data"
ConsumptionFileName= "consumption_5545.csv"
ConsumptionFilePath=DataFolderPath+"/"+ConsumptionFileName
DF_consumption=pd.read_csv(ConsumptionFilePath,sep=",",index_col=0)
previousIndex=DF_consumption.index
ParsedIndex=pd.to_datetime(previousIndex)
DF_consumption.index=ParsedIndex
DF_consumption.head(24)
#Let's take just a part of it
#Since I am interesed in the cooling season

DF_myChosenDates=DF_consumption["2014-07-01 00:00:00" :"2014-07-03 23:00:00" ]  #includes last also
DF_myChosenDates.head(10)
DF_myChosenDates.describe()         #Gives a brief description
plt.close('all')
plt.figure()
DF_myChosenDates.plot()
plt.xlabel('Time')
plt.ylabel('AC Power[W]')

#Now import weather data
weatherSourceFileName="Austin_weather_2014.csv"
weatherSourceFilePath=DataFolderPath+"/"+weatherSourceFileName
DF_weatherSource=pd.read_csv(weatherSourceFilePath,sep=";",index_col=0)
parsedIndex1=pd.to_datetime(DF_weatherSource.index)
DF_weatherSource.index=parsedIndex1

#we usually do this
series_temperature=DF_weatherSource['temperature']

#I would prefer to have it as a dataframe with one column
DF_temperature=DF_weatherSource[['temperature']]

#let's do the same for irradiation
IrradianceSourceFileName="irradiance_2014_gen.csv"
IrradianceSourceFilePath=DataFolderPath+"/"+IrradianceSourceFileName
DF_irradiancesource=pd.read_csv(IrradianceSourceFilePath,sep=";",index_col=1)
DF_irradiancesource.head(5)
parsedIndex2=pd.to_datetime(DF_irradiancesource.index)
DF_irradiancesource.index=parsedIndex2

#If I want to take just the column "gen" as a dataframe with a single column
DF_irradiance=DF_irradiancesource[["gen"]] #to take it as a DF
DF_irradiance[DF_irradiancesource[["gen"]]<0]=0   #setting negative values to zero using index array

DF_joined=DF_consumption.join([DF_temperature,DF_irradiance])
DF_joined.head(30)
DF_joined.dropna()   #drop nan values
