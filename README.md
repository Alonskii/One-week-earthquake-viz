# One-week-earthquake-viz

This is a python project done by Collins Emmanuel. 

It is a one week data visualization of earthquake occurence around the globe. 

The JSON data set was downloaded from https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php 

First, I started by importing the necessary Libraries for the visualization, then I proceeded 
by opening the JSON file and then converting the JSON file to a readable file. 

Then I explored through the data and moved the needed data to the empty lists. 

The if block was created to read through the magnitude data, and make sure that only magnitudes that are greater or equal to zero that is appended to the mags list, and then the lons, lats, and hover_texts are listed inside the if block as well to avoid a ValueError/wrong data presentation. 

I mapped the data according to the information gotten earlier and stored in their various lists. 
I multiplied the size by 5 times so that we can get a bigger picture of the earthquake positions on the map. 

The title of the earthquake was gotten from the json file by going through the metadata and retrieving the title. 

Finally, I plotted the graph and stored the visualization in the file 'sevenday_quakes.html, which clearly shows 
the occurence of a seven day Earthquake across the world. 

The PNG file is the output of the visualization. 


