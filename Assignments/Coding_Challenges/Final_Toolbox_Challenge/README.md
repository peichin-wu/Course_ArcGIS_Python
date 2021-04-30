# Final Toolbox Challenge

## a. Select Richmond in all towns
* Create a study area by using select tool to extract the "Richmond" in towns shapefiles.
In general, the research we conduct has a specific study area.
Usually it’s not as big as a whole country, it’s mostly a city or a county.
However, the administrative shapefile usually contains more than one administrative area, so we need to filter out specific areas.
The first tool (a. Select Richmond in all towns) can help us quickly filter out "Richmond" from the shapefile RI  and save the output as a separate shapefile.

## b. Clip
* Clip the "Rivers" layer to the Richmond study area.
Another problem encountered when doing research is that the amount of data is too large. 
For example, I have river shapefile for the entire RI, but my research area is limited to "Richmond". 
I would like to cut the river shapefile first so that I can produce a "Rivers" layer which only in the Richmond study area.
As a result, the burden of software operation is relatively small, and I have been able to clearly grasp my research area.

## c. Buffer
* Create the riparian zone by using Buffer tool on the rivers by 100m.
The third tool is to calculate the riparian zone. 
The riparian zone is within 100 meters from the river. 
With this tool, I can immediately save the range of the riparian zone as a separate shapefile.