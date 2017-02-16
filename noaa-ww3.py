# -*- coding: utf-8 -*-
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import netCDF4
import datetime
import json
import math

now = datetime.datetime.utcnow() - datetime.timedelta(days=1)
today = now.strftime("%Y%m%d")
report = "nph"
root = 'http://nomads.ncep.noaa.gov:9090/dods/wave/'
url= root + report + '/' + report + today + '/' + report + today +'_00z'
plt.figure()
# Extract the significant wave height of combined wind waves and swell
file = netCDF4.Dataset(url)
lat  = file.variables['lat'][:]
lon  = file.variables['lon'][:]
data = file.variables['htsgwsfc'][:]
llcrnrlon = lon.min()
urcrnrlon = lon.max()
llcrnrlat = lat.min()
urcrnrlat = lat.max()
file.close()
# web mercator projection
m=Basemap(projection="tmerc",lat_ts=0,llcrnrlon=llcrnrlon, \
  urcrnrlon=urcrnrlon,llcrnrlat=llcrnrlat,k_0=1, lon_0=0,  urcrnrlat=urcrnrlat, \
  resolution='h', rsphere=6378137, ellps="WGS84", epsg=3857)

x, y = m(*np.meshgrid(lon,lat))

# create all of the forecase images images
for i in range(1, len(data)):
  filepath = report+"-"+str(i)+".png"
  m.pcolormesh(x,y,data[i],shading='flat',cmap=plt.cm.jet)
  plt.draw()
  plt.savefig(filepath, transparent=True, bbox_inches='tight', pad_inches=0)

response_data = {
  "report_type": report,
  "length": len(data),
  "llcrnrlon": llcrnrlon,
  "llcrnrlat": llcrnrlat,
  "urcrnrlat": urcrnrlat,
  "urcrnrlon": urcrnrlon,
}

print(response_data)