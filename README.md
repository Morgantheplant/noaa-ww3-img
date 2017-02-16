## NOAA WW3 Forecast to PNG

Plots NOAA WavewatchIII grib forecast data to a PNG via Basemap as a web mercator projection (Google Maps). Coastlines and boarders removed so it can easily be plotted to GoogleMaps.

![sample_image](npm-1.png)

```
// original API repsponse

{'llcrnrlat': 4.75, 'urcrnrlat': 60.5, 'length': 43, 'urcrnrlon': 282.75, 'llcrnrlon': 189.75, 'report_type': 'nph'}

``` 
Originally tried to deploy this as separate Django API that I could grab images for [another project](https://github.com/Morgantheplant/smurf). Grew bored/frustrated with it and decided to gut it for now. 

Note: [Basemap](http://matplotlib.org/basemap) is a VERY large dependency and requires numpy and matplotlib before installation. Tried to customize a buildpack to with no luck getting it up on a free Heroku instance (it was way too large): https://devcenter.heroku.com/articles/buildpacks https://github.com/thenovices/heroku-buildpack-scipy May come back to this later.





