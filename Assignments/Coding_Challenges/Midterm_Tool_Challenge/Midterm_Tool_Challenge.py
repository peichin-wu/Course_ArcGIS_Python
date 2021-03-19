

import arcpy
arcpy.env.scratchWorkspace = r"D:\URI\Spring2021\NRS528\Data\Midterm_Tool_Challenge\Data"

Rivers = r"Data\Rivers.shp"
towns = r"Data\towns.shp"
NLCD_2016_img = arcpy.Raster(r"Data\NLCD_2016.img")
# NLCD_2016_img = arcpy.Raster("NLCD_2016.img")

# a. Select
# Create a study area by using select tool to extract the "Richmond" in towns shapefiles.
towns_Select = fr"{arcpy.env.scratchGDB}\towns_Select"
arcpy.analysis.Select(in_features=towns,
                      out_feature_class=towns_Select,
                      where_clause="NAME = 'RICHMOND'")

# b. Clip
# Clip the "Rivers" layer to the Richmond study area.
Rivers_study_area = fr"{arcpy.env.scratchGDB}\Rivers_study_area"
arcpy.analysis.Clip(in_features=Rivers,
                    clip_features=towns_Select,
                    out_feature_class=Rivers_study_area,
                    cluster_tolerance="")

# c. Buffer
# Create the riparian zone by using Buffer tool on the rivers by 100m.
riparian_zone = fr"{arcpy.env.scratchGDB}\riparian_zone"
arcpy.analysis.Buffer(in_features=Rivers_study_area,
                      out_feature_class=riparian_zone,
                      buffer_distance_or_field="100 Meters",
                      line_side="FULL",
                      line_end_type="ROUND",
                      dissolve_option="ALL",
                      dissolve_field=[],
                      method="PLANAR")

# d. Tabulate Area
# Calculate the areas of each NLCD land cover class within the riparian zones.
land_cover_by_river = fr"{arcpy.env.scratchGDB}\land_cover_by_river"
arcpy.sa.TabulateArea(in_zone_data=riparian_zone,
                      zone_field="OBJECTID",
                      in_class_data=NLCD_2016_img,
                      class_field="NLCD_Land",
                      out_table=land_cover_by_river,
                      processing_cell_size= NLCD_2016_img,
                      classes_as_rows="CLASSES_AS_ROWS")
