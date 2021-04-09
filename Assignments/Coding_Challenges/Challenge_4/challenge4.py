
#####
# Step  - Querying your data, extent, cell size, type etc
#####

# Extract Challenge_4_data.zip into a folder of known location.

#  Below is the code that interrogates a shapefile and returns the type of data stored within it:
import arcpy
import pandas as pd
import os

input_folder = r"C:\Data\Students_2021\Wu\Assignments\Coding_Challenges\Challenge_4\Challenge_4_data"
input_file = "Building_footprints_South_Kingston.shp"
desc = arcpy.Describe(os.path.join(input_folder, input_file))


# 1. Dataset Type
print("Shape Type: %s" % desc.shapeType)
# 2. Spatial Reference Name and Type.
print("Spatial Reference Name: %s" % desc.spatialReference.name)
print("Spatial Reference Type: %s" % desc.spatialReference.type)
print("Spatial Unit: %s" % desc.spatialReference.linearUnitName)
# 3. How many building features are in the dataset?
# 4. What is the area of the largest building?
# 5. What is the average area of the features?
in_table = os.path.join(input_folder, input_file)
out_table = os.path.join(input_folder, "Output_Table.csv")
field = "FID"
statistics_type = "COUNT"
field1 = "SqMiles"
statistics_type1 = "MAX"
field2 = "SqMiles"
statistics_type2 = "MEAN"
case_field = "#"
arcpy.Statistics_analysis(in_table, out_table, [[field, statistics_type], [field1, statistics_type1], [field2, statistics_type2]], case_field)
df_new = pd.read_csv(os.path.join(input_folder, "Output_Table.csv"))
print("There are", df_new.COUNT_FID.values, "buildings in the dataset.")
print("The largest area of building is", df_new.MAX_SqMiles.values, "miles square.")
print("The average of area is", df_new.MEAN_SqMiles.values, "miles square.")
