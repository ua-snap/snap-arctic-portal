# snap-arctic-portal

Core / umbrella / app repository for our Arctic Portal work.

## Some data recipes

Placeholder (move to other location when we get farther) for notes we have on data transformations we've needed to ingest material into GN.

**Need to get rid of `nodata` values rendering as black**: First you need to assign the nodata value if there isn't one, and then you may need to do this: `gdalwarp -of GTiff -srcnodata 0 -dstalpha infile.tif outfile.tif`

*After reprojecting, you may need to clip a raster to its maximum logical extent*.  Example, when you transform the whole-earth Natural Earth dataset to 3338, there's a lot of regions that are insane and need to be thrown out.  You can use [epsg.io](http://epsg.io) to find bounding boxes.  An example of doing this clipping is this:

```
gdalwarp -overwrite -te -3055938.4795 -209981.1884 3446517.6368 3476986.5642 natural-earth-reprojected.tif natural-earth-reprojected-expanded-bounds.tif
```

### A useful set of `gdal` recipes
Here is *[a general stew of useful gdal commands](https://github.com/dwtkns/gdal-cheat-sheet)*.
