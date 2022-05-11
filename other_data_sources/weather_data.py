# Imports

import pandas as pd
import numpy as np
import matplotlib

#Weather
from meteostat import Stations, Daily,  units, Hourly #, Point
from datetime import datetime

# Geo processing
import shapely
#import geopandas as gpd
from shapely.geometry import Polygon, LineString, Point

def c_to_f(x):
    return(x*1.8+32)

def kph_to_mph(x):
    return(x*1.609344)

def kph_to_mps(x):
    return(x/3.6)

def heat_index(T,RH):
    #Useful ranges from https://www.weather.gov/safety/heat-index
    if T<27 or RH<40:
        return(T)
    T=c_to_f(T)
    
    #From https://www.wpc.ncep.noaa.gov/html/heatindex_equation.shtml
    HI = -42.379 + 2.04901523*T + 10.14333127*RH - .22475541*T*RH - .00683783*T*T - .05481717*RH*RH + .00122874*T*T*RH + .00085282*T*RH*RH - .00000199*T*T*RH*RH
    return(HI)
    
def heat_advisory(hi):
    #For NY only. https://www.weather.gov/bgm/heat
    #Takes heat index as input.  Note that this requires a 2+ hour duration for an official announcement.
    if hi > 95:
        return(True)
    else:
        return(False)

def wind_chill(T,wspd):
    #Input: temperature in celsius, wspd in KPH
    #Output: Wind Chill
    
    #From https://www.weather.gov/epz/wxcalc_windchill
    #Note: due to rounding, this number is _slightly_ off.  
        #wc of 25 should be achieved at -2 degrees C, 5 KPH wind
        #This calculator sets wc of 25 at 0 degrees C, 5 KPH wind
    
    if T>10 or wspd<4.8:
        return(T)
    T=c_to_f(T)
    wspd=kph_to_mph(wspd)
    wspd=wspd**0.16
    wcf = 35.74+(.6215*T)-(35.75*wspd)+(.4275*T*wspd)
    return(wcf)

def wind_chill_advisory(wc):
    #National. From https://www.weather.gov/okx/wwa_definitions
    if wc<-25:
        return(True)
    else:
        return(False)

def is_raining(x):
    #Input: hourly precipitation in mm.
    #Output: if precipitation greater than 0.
    print('precipitation',x)
    print(type(x))
    
    if np.isnan(x) or x==0:
        return(False)
    else:
        return(True)
                

def get_weather_stations(min_lat,min_lon,max_lat,max_lon):
    ###NEEDS FUNCTION TO GET TAXI ZONES###
    #Gets a dataframe of weather stations in a grid based on min/max latitude/longitude values.
    
    #Input: min and max latitude/longitude
    
    #Output: a dataframe with the following columns:
        #id:        object      id number of weather station.
        #latitude:  float       latitude of station.
        #longitude: float       longitude of station.
        #point:     object      lat/lng of station as object.

    #Retrieves a list of weather stations.(id,latitude,longitude)
    df_stations = Stations().bounds((max_lat,min_lon),(min_lat,max_lon)).fetch()[['latitude','longitude']]        
    #Point function from shapely package.
    df_stations["point"] = df_stations[["longitude", "latitude"]].apply(Point, axis=1) 
    ###FUNCTION TO GET TAXI ZONES GOES HERE###


    return(df_stations)

def get_data_simple(df_stations,startDate,endDate):
    
    
    #Input: start & end dates as datetime, min/max latitude/longitude in degrees.
    
    #Output: Dataframe with the following columns:
        #station:   object      ID number of the weather station.
        #time:      datetime    Time of reading.  Precipitation is for the preceding hour.
        #temp:      float       Temperature in degrees celsius.
        #rhum:      float       Relative humidity.
        #prcp:      float       Precipitation in mm.  Does not include snow, but may include snowmelt.
        #wspd:      float       Average wind speed in kph.
        #point:     object      lat/lng of station as object.
    
    #Retrieves weather data for stations in df_stations.
    df_weather_data = Hourly(df_stations.index.tolist(),startDate,endDate).fetch()[['temp','rhum','prcp','wspd']]
    
    #Merge Datasets
    #weather data has a multi-level index.  Reset so we don't have to deal with it.
    df_stations.reset_index(inplace=True)
    df_weather_data.reset_index(inplace=True)
    df_weather_data = pd.merge(df_weather_data,
                               df_stations,
                               left_on='station',
                               right_on='id').drop(['id','latitude','longitude'],axis=1)

    return(df_weather_data)

def get_expanded_data(df_weather_data):
    #Input: Weather dataframe from get_data_simple
    #Output: Dataframe with the following columns:

    #df_weather_data["heat_index"] = df_weather_data[["temp", "rhum"]].apply(heat_index, axis=1) 
    #df_weather_data["heat_advisory"] = df_weather_data[["heat_index"]].apply(heat_advisory, axis=1) 
    #df_weather_data["wind_chill"] = df_weather_data[["temp", "wspd"]].apply(wind_chill, axis=1) 
    #df_weather_data["wind_chill_advisory"] = df_weather_data[["wind_chill"]].apply(wind_chill_advisory, axis=1) 
    df_weather_data["is_raining"] = df_weather_data[["prcp"]].apply(is_raining, axis=1) 

    return(df_weather_data)

startDate = datetime(2014, 2, 1, 1, 1)
endDate = datetime(2014,2,28,23,59)
#endDate = datetime(2015, 6, 30, 23, 59)

#x/y coord
min_lat = 40.1067
min_lon = -74.929
max_lat = 41.3225
max_lon = -71.1801

df_stations = get_weather_stations(min_lat,min_lon,max_lat,max_lon)
df_weather_data = get_data_simple(df_stations,startDate,endDate)
df_weather_expanded = get_expanded_data(df_weather_data)


#Get weather stations within requested bounds


#Get corresponding locationID for each weather station.  
#Dataset contains <100 weather stations, so if we determine zone before matching with hourly data, this should scale fine.
#df_stations['locationID'] = df_stations['point'].apply(lambda x: coord_to_zone(x))

#Get relevent weather data
#.drop(['dwpt','wdir','wpgt','pres','coco','snow','tsun'],axis=1)

#Merge Datasets
#weather data has a multi-level index.  Reset so we don't have to deal with it.


#Insert discomfort indecies here
    #Windchill
    #Heat Equivalent
    
#Group by locationID