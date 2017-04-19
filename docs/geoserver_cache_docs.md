# Properly configuring GeoServer / GeoWebCache with Leaflet and custom projections (Proj4Leaflet)

These instructions demonstrate the process for EPSG:3572.

## Set up a Gridset for the appropriate projection.

Geoserver Admin > Tile Caching > Gridsets > New
Set Name / Projection to EPSG:3572, when you tab out of the Projection box it should autocomplete a bit of information here, such as Units, Meters per Unit.

Under “Gridset Bounds,” > Compute from maximum extent of CRS.  We’ll need these numbers to configure Leaflet.  (An error at the top may show, “Field ‘Gridset Bounds’ is required,” ignore that).

Two approaches to the next part, with the important part being that the list of resolutions matches between Leaflet & the Gridset.  For both, Under Tile Matrix Set, ensure Define Grids Based on: Resolution is selected.

Approach (1), let GeoWebCache pick the resolutions: click Add Zoom Level until you have enough zoom levels.  The exact number will depend on the spatial domain, but adding 20 is probably more than enough.

Approach (2), use ones you’ve defined in Leaflet but configure GeoWebCache to understand: click Add Zoom Level, then *edit it* to reflect the value you have in your `resolutions` array in Leaflet.  Continue adding/editing as much as you need, noting that by default GeoServer will use half of the initial value, which makes it pretty fast to generate these.

Save.

## Configure the layer to use the gridset for cache

Geoserver Admin > Tile Caching > Tile Layers > Pick the layer you want to enable cache for.

Towards the bottom, Available Gridsets > EPSG:3572 > *Click the “Plus” button next to that drop-down*.  (You can select it from the drop down, but unless you hit the "Plus," it does not actually add the gridset to the tile layer.)  Ensure that ‘Min/Max’ are selected for published and cached zoom levels.  Click Save.

## Align the Leaflet configuration with the Gridset

In the relevant Leaflet code where you are configuring the base `map` object, the `origin` property should be set to the *lower left* coordinate listed in the maximum extent calculated by the CRS.  In this example, it should be:

```
origin: [-4234288.146966308, -4234288.146966307]
```

The array of resolutions needs to match what’s in the “Pixel Size” column in the Gridset configuration in GeoServer.

Finally, each layer must be configured to include a `TILED=true` parameter as part of the WMS request.

## Troubleshooting and Gotchas

To see if a specific tile is hitting cache or not, look at the response headers from a tile request.  Easiest is to use Chrome, add the layer you want to check with the network tab of the developer tools open, then right-click and Select Response Headers.  Proper cache response looks something like this:

```
HTTP/1.1 200 OK
Content-Type: image/png
geowebcache-crs: EPSG:3338
ETag: ee72b733dea96b0621dbacc777ef24fa
geowebcache-layer: geonode:na_landcover_2010_25hammu
geowebcache-gridset: 3338_Rowdy
geowebcache-tile-index: [9, 2, 5]
Last-Modified: Thu, 11 Aug 2016 00:56:17 GMT
geowebcache-cache-result: HIT
geowebcache-tile-bounds: 70586.0656835828,1493385.882955059,594874.0656835828,2017673.882955059
Cache-Control: no-cache
Content-Disposition: inline; filename=geonode-na_landcover_2010_25hammu.png
Transfer-Encoding: chunked
Server: Jetty(8.y.z-SNAPSHOT)
```

Misconfigured gridset or misconfigured Leaflet looks like this:

```
HTTP/1.1 200 OK
Content-Type: image/png
geowebcache-miss-reason: request does not align to grid(s) 'EPSG:3338' '3338_Rowdy'
geowebcache-cache-result: MISS
Content-Disposition: inline; filename=geonode-na_landcover_2010_25hammu.png
Transfer-Encoding: chunked
Server: Jetty(8.y.z-SNAPSHOT)
```

If the request misses cache but no reason is given (`geowebcache-miss-reason:` blank) then check the layer cache configuration: the min/max zoom levels available enabled for a layer cache may reset to 0/0 if you edit the gridset -- double check that they are set to min/max.

Note that you must request the specific *cache layer*, not the *layer*.  For our case, this means that you need to prepend `geonode:`, as you can see in the base layer configurations

## Seeding the GeoServer cache

GeoNode Admin > Tile Caching > Tile Layers > (for the layer you want to seed) Seed/Truncate.  Now you're on the GeoWebCache (minimal!) interface.

From the drop-downs, select the gridset you want to populate, then *pick the correct zoom levels* corresponding to *what is configured for that gridset*.  There's one gotcha with seeding the cache: if you enable zoom levels outside of what the gridset understands, it doesn't start the seed and doesn't provide a useful feedback message.

Click "Submit" to start the seed process.  If it doesn't show the job as being in progress/submitted, then double-check settings and zoom levels.
