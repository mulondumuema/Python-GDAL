# Python-GDAL
A repository for python gdal


To install gdal in a virtual environment:

1. create the virtual environment

```$ python3 -m venv ~/.virtualenvs/gis ```

2. activate the virtual environment

```$ source ~/.virtualenvs/gis/bin/activate ```

3. in the virtual environment install gdal version similar in your system

```$ pip install --global-option=build_ext --global-option="-I/usr/include/gdal" GDAL==`gdal-config --version` ```

to check the installed gdal version

```$ gdalinfo --version```

You also need to have installed the GEOS library (for spatial analysis) and PROJ.4 (for projections). In Ubuntu you can install these with:

```$ sudo apt-get install binutils libproj-dev gdal-bin ```

```$ sudo apt-get install -y libgeos-dev```

The library oftenly used to for analysing geospatial data is shapely. While folium can be used to view the data.

Attached are example programs.

Installing Mapnik

Mapnik is a freely-available library for building mapping applications. Mapnik takes geospatial data from a PostGIS database, shapefile, or any other format supported by GDAL/OGR, and turns it into clearly-rendered, good-looking images.

to install mapnik:

``` sudo apt-get install -y git autoconf libtool libxml2-dev libbz2-dev libgeos-dev libgeos++-dev libproj-dev gdal-bin libgdal-dev g++ libmapnik-dev mapnik-utils python-mapnik ```

Check the installed version with:

```mapnik-config -v ```

Mapnik example

this is based on [this github repo](https://github.com/mapnik/mapnik/wiki/GettingStartedInPython).

Download and unzip the data:

``` wget https://github.com/mapnik/mapnik/wiki/data/110m-admin-0-countries.zip ```

``` unzip 110m-admin-0-countries.zip ```

To plot copy the code below in a file world.py:

```
import mapnik
m = mapnik.Map(600,300)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff9')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer.stroke = mapnik.Color('rgb(50%,50%,50%)')
line_symbolizer.stroke_width = 0.1

r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('My Style',s)
ds = mapnik.Shapefile(file='ne_110m_admin_0_countries.shp')
layer = mapnik.Layer('world')
layer.datasource = ds
layer.styles.append('My Style')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m,'world.png', 'png')
print("rendered image to 'world.png'")
```

Run the code by running 

``` $ python3 world.py```


