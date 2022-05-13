weather_data.py is meant to generate .csv files using the meteostat library.

It contains the following:

A number of small functions (c_to_f down to is_raining) that convert units and calculate measures.
	
get_weather_stations: retrieves a list of weather stations from meteostat, based on a set of lat/lon coordinates.

get_data_simple: Retrieves temperature, humidity, precipitation, and windspeed for a list of weather stations.

get_data_expanded: This adds all the subjective comfort measures we used (heat index, wind chill, rain), as well as converting from UTC to US/Eastern.

hourly_to_daily: aggregates from hourly to daily

worst_three_days: returns the hottest, coldest, and rainiest days of the year.  precipitation numbers DO NOT aggregate correctly, so we used individual station numbers once we found the day.

driver code: Runs the above and returns .csv's.  Only addition is a groupby to average all station results; this was a late addition.

