# I use class 04_arcpy_step2_task1 for example to create the function "describe_image"
import arcpy

def describe_image(input_image):
    desc_image = arcpy.Describe(input_image)
    print("Dataset Type: %s" % desc_image.datasetType)
    if arcpy.Exists(input_image):
        if desc_image.dataType == "RasterDataset":
            print("Spatial Reference Name: %s" % desc_image.spatialReference.name)
            print("Spatial Reference Type: %s" % desc_image.spatialReference.type)
            print("Spatial Unit: %s" % desc_image.spatialReference.linearUnitName)
            print("Extent:\n  YMin: {0},\n YMax: {1}".format(desc_image.extent.YMin, desc_image.extent.YMax))
            print("Cell size X: {0}, Cell size Y: {1}".format(desc_image.children[0].meanCellWidth,
                                                              desc_image.children[0].meanCellHeight))
            print("Band Count: %s" % desc_image.bandCount)
        else:
            print("Input data not RasterDataset..")
    else:
        print("Dataset not found, please check the file path..")


input_image = r"D:\URI\Spring2021\NRS528\Data\08_Functions\challenge_data\0320001450.JP2"
describe_image(input_image)
