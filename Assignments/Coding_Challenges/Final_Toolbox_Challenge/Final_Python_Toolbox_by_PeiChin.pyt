import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Final Python Toolbox by PeiChin"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [Select, Clip, Buffer]

# a. Select
# Create a study area by using select tool to extract the "Richmond" in towns shapefiles.
class Select(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Select Richmond in all towns "
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        input_polygon = arcpy.Parameter(name="input_polygon",
                                     displayName="Input Polygon (towns)",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        #input_polygon.value = r"D:\URI\Spring2021\NRS528\Data\Final_Toolbox_Challenge\Data\towns.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(input_polygon)

        output = arcpy.Parameter(name="output",
                                 displayName="Output",
                                 datatype="DEFeatureClass",
                                 parameterType="Required",  # Required|Optional|Derived
                                 direction="Output",  # Input|Output
                                 )
        #output.value = r"D:\URI\Spring2021\NRS528\Data\Final_Toolbox_Challenge\Data\towns_Select.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(output)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""

        input_polygon = parameters[0].valueAsText
        output = parameters[1].valueAsText

        arcpy.analysis.Select(in_features=input_polygon,
                              out_feature_class=output,
                              where_clause="NAME = 'RICHMOND'")
        return

# b. Clip
# Clip the "Rivers" layer to the Richmond study area.
class Clip(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Clip Rivers to the study area"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        input_line = arcpy.Parameter(name="input_line",
                                     displayName="Input Rivers' Line",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        #input_line.value = r"D:\URI\Spring2021\NRS528\Data\Final_Toolbox_Challenge\Data\Rivers.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(input_line)

        input_polygon = arcpy.Parameter(name="input_polygon",
                                        displayName="Input Polygon (Towns_Select)",
                                        datatype="DEFeatureClass",
                                        parameterType="Required",  # Required|Optional|Derived
                                        direction="Input",  # Input|Output
                                        )
        #input_polygon.value = r"D:\URI\Spring2021\NRS528\Data\Final_Toolbox_Challenge\Data\towns_Select.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(input_polygon)

        output = arcpy.Parameter(name="output",
                                 displayName="Output",
                                 datatype="DEFeatureClass",
                                 parameterType="Required",  # Required|Optional|Derived
                                 direction="Output",  # Input|Output
                                 )
        #output.value = r"D:\URI\Spring2021\NRS528\Data\Final_Toolbox_Challenge\Data\Rivers_study_area.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(output)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""

        input_line = parameters[0].valueAsText
        input_polygon = parameters[1].valueAsText
        output = parameters[2].valueAsText

        arcpy.analysis.Clip(in_features=input_line,
                            clip_features=input_polygon,
                            out_feature_class=output,
                            cluster_tolerance="")
        return

# c. Buffer
# Create the riparian zone by using Buffer tool on the rivers by 100m.

class Buffer(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Buffer tool on the rivers by 100m"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        input_line = arcpy.Parameter(name="input_line",
                                     displayName="Input Rivers' Line",
                                     datatype="DEFeatureClass",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        #input_line.value = r"D:\URI\Spring2021\NRS528\Data\Final_Toolbox_Challenge\Data\Rivers.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(input_line)

        output = arcpy.Parameter(name="output",
                                 displayName="Output",
                                 datatype="DEFeatureClass",
                                 parameterType="Required",  # Required|Optional|Derived
                                 direction="Output",  # Input|Output
                                 )
        #output.value = r"D:\URI\Spring2021\NRS528\Data\Final_Toolbox_Challenge\Data\riparian_zone.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(output)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""

        input_line = parameters[0].valueAsText
        output = parameters[1].valueAsText

        arcpy.analysis.Buffer(in_features=input_line,
                              out_feature_class=output,
                              buffer_distance_or_field="100 Meters",
                              line_side="FULL",
                              line_end_type="ROUND",
                              dissolve_option="ALL",
                              dissolve_field=[],
                              method="PLANAR")
        return


# def main():
#     tool = Buffer() # i.e. what you have called your tool class: class Clippy(object):
#     tool.execute(tool.getParameterInfo(), None)
#
# if __name__ == '__main__':
#     main()