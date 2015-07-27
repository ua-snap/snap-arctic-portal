# snap-arctic-portal

Core / umbrella / app repository for our Arctic Portal work.

# Some data recipes

Placeholder (move to other location when we get farther) for notes we have on data transformations we've needed to ingest material into GN.

*Raster uploads but has transparent areas when reprojected by GN*: `gdalwarp -of GTiff -srcnodata 0 -dstalpha infile.tif outfile.tif`

*After reprojecting, you may need to clip a raster to its maximum logical extent*.  Example, when you transform the whole-earth Natural Earth dataset to 3338, there's a lot of regions that are insane and need to be thrown out.  You can use [epsg.io](http://epsg.io) to find bounding boxes.

Here is *[a general stew of useful gdal commands](https://github.com/dwtkns/gdal-cheat-sheet)*.
