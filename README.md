# Movement_NYC

Repository Contents: 

/mileva    
- 00_uber_data_exploration.ipynb: Initial exploration, shows the schema for the Uber 2014 data vs. Uber 2015 data.   
- 01_initial_processing_get_zones.ipynb: Pipeline to convert lat/long coordinates (used in 2014 data) into zones (used in the 2015 data). Richard completed this conversion in QGIS as the code scaled poorly to the entire dataset.   
- 02_final_processing.ipynb: Pipeline to convert the individual csv files exported from QGIS into a single csv (with a unified schema) for all the 2014 and 2015 Uber data. The output of this notebook is used for all future processing.    
- 03_analysis.ipynb: Analyzes daily 2014-2015 uber ridership conditioning on borough and weather conditions. The scatter plots produced highlight days where weather, events, and holidays disrupted normal patterns in uber ridership.  

/richard
- QGIS_processing.ipynb: Processes raw input data to output summation of rides from each taxi zone for every month in the data set corrected for overall growth in Uber ridership for the 14 month period of the data set.  The data format is then suitable for joining onto QGIS polygon shapes representing taxi zones throughout the five New York boroughs.  The final output produces choropleths demonstrating shifting monthly trends in ridership concentration.
