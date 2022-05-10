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

#date/time

startDate = datetime(2014, 2, 1, 1, 1)
endDate = datetime(2014,2,28,23,59)
#endDate = datetime(2015, 6, 30, 23, 59)

#x/y coord
min_lat = 40.1067
min_lon = -74.929
max_lat = 41.3225
max_lon = -71.1801
top_left = (max_lat,min_lon)
bottom_right = (min_lat,max_lon)

#Get weather stations within requested bounds
df_stations = Stations().bounds(top_left,bottom_right).fetch()[['latitude','longitude']]
#df_stations[[latitude','longitude']]
df_stations["point"] = df_stations[["longitude", "latitude"]].apply(Point, axis=1) #This should work, but doesn't.

#Get corresponding locationID for each weather station.  
#Dataset contains <100 weather stations, so if we determine zone before matching with hourly data, this should scale fine.
#df_stations['locationID'] = df_stations['point'].apply(lambda x: coord_to_zone(x))

#Get relevent weather data
df_weather_data = Hourly(df_stations.index.tolist(),startDate,endDate).fetch()[['temp','rhum','prcp','wspd']]
#.drop(['dwpt','wdir','wpgt','pres','coco','snow','tsun'],axis=1)

#Merge Datasets
#weather data has a multi-level index.  Reset so we don't have to deal with it.
df_stations.reset_index(inplace=True)
df_weather_data.reset_index(inplace=True)
df_weather_data = pd.merge(df_weather_data,
                           df_stations,
                           left_on='station',
                           right_on='id').drop(['id','latitude','longitude'],axis=1)

#Insert discomfort indecies here
    #Windchill
    #Heat Equivalent
    
#Group by locationID