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
