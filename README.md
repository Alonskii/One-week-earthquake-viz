# One-week-earthquake-viz

This is a python project done by Collins Emmanuel. 

It is a one week data visualization of earthquake occurence around the globe. 

The Json data set was downloaded from https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php 

First, I started by importing the necessary Libraries for the visualization, then I proceeded 
by opening the json file and reading through the file. 

Then I explored through the data and moved the needed data to the empty lists. 

I created another list(clean_mags) because the list(mags) had some elements that wasn't needed 
for the visualization. So I constructed a loop to loop through the list(mag) and then append the
positive numbers to the list(clean_mags). 

I mapped the data according to the information gotten earlier and stored in their various lists. 
I multiplied the size by 5 times so that we can get a bigger picture of the earthquake point on the map. 

The title of the earthquake was gotten from the json file by going through the metadata and retrieving the title. 

Finally, I plotted the graph and stored the visualization in the file 'sevenday_quakes.html, which clearly shows 
the occurence of a seven day Earthquake across the world. 

