# Movement_NYC

Repository Contents: 

NYC Uber Trips.pptx: PowerPoint Presentation. 
/Melanie Time Series Analysis
- Hourly and Daily Changes of Uber Traffic Data.ipynb: Visualizations of the changes by day and by hour
- Analyzing Weekends vs Weekdays.ipynb: Same as above, but generalized to weekends instead of weekdays
- Analyzing_Weekends_versus_Weekdays_GoogleColab_Scaled.ipynb: some minor corrections to weekends plots with scaling
  - /August2014Pandas: smaller examples of the data analysis using Pandas
    - Peaks in Time By Day August 2014.ipynb: visualization using Pandas on a smaller scale for days
    - Peaks in Time By Hour August 2014.ipynb: visualizations of August 2014's differences by hour
  - /Templates: smaller example of Reading in all the 2014 data.
    - Reading in All the Days: the notebook corresponding to this.
    
/mileva    
- 00_uber_data_exploration.ipynb: Initial exploration with PySpark, shows the schema for the Uber 2014 data vs. Uber 2015 data.   
- 01_initial_processing_get_zones.ipynb: Converts lat/long coordinates (used in 2014 data) into locationIDs (used in 2015 data). Richard completed this transformation in QGIS as the code scaled poorly to the entire dataset.   
- 02_final_processing.ipynb: Converts individual csv files exported from QGIS into a single csv (with a unified schema) for the 2014 and 2015 Uber data. The output of this notebook is used for future processing.    
- 03_analysis.ipynb: Analyzes daily 2014-2015 Uber ridership conditioning on borough and weather. The scatter plots indicate how Uber ridership is impacted by weather, holidays, and events.

/mileva/scatterplots_daily_ridership:
- scatterplot_zones.html: Interactive Plotly graph to illustrate daily ridership by borough. This plot was used for outlier analysis.   
- scatterplot_rain.html:  Plotly graph to visualize how rain influences daily ridership.   
- scatterplots_cold.html: Plotly graph to demonstrate that wind chill advisory has no influence on daily ridership.   
- scatterplots_cold.html: Plotly graph to demonstrate that high temperatures do not influence daily ridership.   

/richard
- QGIS_processing.ipynb: Processes raw input data to output summation of rides from each taxi zone for every month in the data set corrected for overall growth in Uber ridership for the 14 month period of the data set.  The data format is then suitable for joining onto QGIS polygon shapes representing taxi zones throughout the five New York boroughs.  The final output produces choropleths demonstrating shifting monthly trends in ridership concentration.

/other_data_sources (Thomas)
weather_data.py: Generates .csv files using the meteostat library.
It contains the following:

* A number of small functions (c_to_f down to is_raining) that convert units and calculate measures.
* get_weather_stations: retrieves a list of weather stations from meteostat, based on a set of lat/lon coordinates.
* get_data_simple: Retrieves temperature, humidity, precipitation, and windspeed for a list of weather stations.
* get_data_expanded: This adds all the subjective comfort measures we used (heat index, wind chill, rain), as well as converting from UTC to US/Eastern.
* hourly_to_daily: aggregates from hourly to daily
* worst_three_days: returns the hottest, coldest, and rainiest days of the year.  precipitation numbers DO NOT aggregate correctly, so we used individual station numbers once we found the day.
* driver code: Runs the above and returns .csv's.  Only addition is a groupby to average all station results; this was a late addition.
