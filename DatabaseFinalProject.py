import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pandas as pd
import io
import numpy as np


# read in data to use for plotted points
cols_to_use = ['latitude', 'longitude']
buildingdf = pd.read_csv('/home/ollie/Documents/latlon.csv')


lat = buildingdf['latitude'].values.tolist()
lon = buildingdf['longitude'].values.tolist()
combined = np.vstack((lat, lon)).T

# create map using BASEMAP
m = Basemap(projection='merc',llcrnrlat=-80,urcrnrlat=80,\
            llcrnrlon=-180,urcrnrlon=180,lat_ts=20,resolution='c')
m.drawcoastlines()
m.drawcountries()
m.drawstates()
m.bluemarble()
q = len(lat)

for i in range(0,q):
    lats,lons = float(lat[i]),float(lon[i])
    x,y = m(lons,lats)
    m.plot(x,y, 'ro')

plt.show()


