Directory Contents: 
  
- 00_uber_data_exploration.ipynb: Initial exploration with PySpark, shows the schema for the Uber 2014 data vs. Uber 2015 data.   
- 01_initial_processing_get_zones.ipynb: Converts lat/long coordinates (used in 2014 data) into locationIDs (used in 2015 data). Richard completed this transformation in QGIS as the code scaled poorly to the entire dataset.   
- 02_final_processing.ipynb: Converts individual csv files exported from QGIS into a single csv (with a unified schema) for the 2014 and 2015 Uber data. The output of this notebook is used for future processing.    
- 03_analysis.ipynb: Analyzes daily 2014-2015 Uber ridership conditioning on borough and weather. The scatter plots indicate how Uber ridership is impacted by weather, holidays, and events.

/scatterplots_daily_ridership:
- scatterplot_zones.html: Interactive Plotly graph to illustrate daily ridership by borough. This plot was used for outlier analysis.   
- scatterplot_rain.html:  Plotly graph to visualize how rain influences daily ridership.   
- scatterplots_cold.html: Plotly graph to demonstrate that wind chill advisory has no influence on daily ridership.   
- scatterplots_cold.html: Plotly graph to demonstrate that high temperatures do not influence daily ridership.   