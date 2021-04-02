
#####
# Step 3 - Python Script from Tools
#####

# NOTE THAT THIS TASK IS ALSO YOUR CODING CHALLENGE THIS WEEK, I DO NOT EXPECT US TO COMPLETE THIS IN CLASS.

# Task 1 - Use what you have learned to process the Landsat files provided, this time, you know you are
# interested in the NVDI index which will use Bands 4 (red, aka vis) and 5 (near-infrared, aka nir) from the
# Landsat 8 imagery. Data provided are monthly (a couple are missing due to cloud coverage) during the
# year 2015 for the State of RI.

# Before you start, here is a suggested workflow:

# 1) Extract the Step_3_data.zip file into a known location.
# 2) For each month provided, you want to calculate the NVDI, using the equation: nvdi = (nir - vis) / (nir + vis)
# https://en.wikipedia.org/wiki/Normalized_difference_vegetation_index. Consider using the Raster Calculator Tool
# in ArcMap and using "Copy as Python Snippet" for the first calculation.

# The only rule is, you should run your script once, and generate the NVDI for ALL MONTHS provided. As part of your
# code submission, you should also provide a visualization document (e.g. an ArcMap layout), showing the patterns for
# an area of RI that you find interesting.


import os, arcpy
from arcpy.sa import *
listMonth = ["02", "04", "05", "07", "10", "11"]
outputDirectory = r"D:\URI\Spring2021\NRS528\Data\06_Cheating\Step_3_data_lfs"
if not os.path.exists(outputDirectory):
    os.mkdir(outputDirectory)


for month in listMonth:
    arcpy.env.workspace = r"D:\URI\Spring2021\NRS528\Data\06_Cheating\Step_3_data_lfs\2015" + str(month)

    listRasters = arcpy.ListRasters("*", "TIF")
    print("For year: " + month + ", there are: " + str(len(listRasters)) + " bands to process.")

    listRasters_B4 = [x for x in listRasters if "_B4.tif" in x]
    print("Compositing Bands for " + month)
    arcpy.CompositeBands_management(in_rasters=listRasters_B4, out_raster=os.path.join(outputDirectory, "2015" + str(month) + "_B4.tif"))
    print("Compositing Bands for " + month + " finished.")

    listRasters_B5 = [x for x in listRasters if "_B5.tif" in x]
    print("Compositing Bands for " + month)
    arcpy.CompositeBands_management(in_rasters=listRasters_B5,out_raster=os.path.join(outputDirectory, "2015" + str(month) + "_B5.tif"))
    print("Compositing Bands for " + month + " finished.")
for month in listMonth:
    arcpy.env.workspace = r"D:\URI\Spring2021\NRS528\Data\06_Cheating\Step_3_data_lfs"
    nir = Raster("2015" + str(month) + "_B5.tif")
    vis = Raster("2015" + str(month) + "_B4.tif")
    output_raster = (nir - vis) / (nir + vis)
    output_raster.save(r"D:\URI\Spring2021\NRS528\Data\06_Cheating\Step_3_data_lfs\2015" + str(month) + "_nvdi.tif")

