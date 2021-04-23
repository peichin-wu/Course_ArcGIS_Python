import arcpy, os

cwd = os.getcwd()

photo_count_da = 0
non_photo_count_da = 0
with arcpy.da.SearchCursor(os.path.join(cwd,"RI_Forest_Health_Works_Project_Points_All_Invasives\RI_Forest_Health_Works_Project%3A_Points_All_Invasives.shp"), ['photo']) as cursor:
    for row in cursor:
        if row[0] == 'y' :
            photo_count_da += 1
        else:
            non_photo_count_da += 1
print("There are " + str(photo_count_da) + " sites have photos, and there are " + str(non_photo_count_da) + " not. ")

# Species:
# Create an empty list first, and let the row in cursor append in the list.
# Use "set" to list unique species in the dataset.
# Use "len" to count the number of the unique species, and minus one to remove the " " (blank) one.
emptylist=[]
with arcpy.da.SearchCursor(os.path.join(cwd,"RI_Forest_Health_Works_Project_Points_All_Invasives\RI_Forest_Health_Works_Project%3A_Points_All_Invasives.shp"), ['Species']) as cursor:
    for row in cursor:
        emptylist.append(row)
print(len(set(emptylist))-1)
print("There are " + str(len(set(emptylist))-1) + " unique species in the dataset. ")


#Generate two shapefiles, one with photos and the other without.
cwd = os.getcwd()
input_shp = os.path.join(cwd,"RI_Forest_Health_Works_Project_Points_All_Invasives\RI_Forest_Health_Works_Project%3A_Points_All_Invasives.shp")
outfolder = os.path.join(cwd,"result")

fields = ['OBJECTID', 'id', 'FileName', 'Site', 'Owner', 'Point_num', 'Species', 'num_Indivi', 'Other', 'PhotoN', 'PhotoE','PhotoS','PhotoW','LifeStage','Habitat','PointNotes','photo','Treatment_']
expression = arcpy.AddFieldDelimiters(input_shp, "photo") + " = 'y'"
arcpy.Select_analysis(in_features=input_shp,
                              out_feature_class=os.path.join(outfolder, 'photo.shp'),
                              where_clause=expression)
expression2 = arcpy.AddFieldDelimiters(input_shp, "photo") + " = ''"
arcpy.Select_analysis(in_features=input_shp,
                              out_feature_class=os.path.join(outfolder, 'non_photo.shp'),
                              where_clause=expression2)
