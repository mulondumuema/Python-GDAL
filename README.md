# Python-GDAL
A repository for python gdal


To install gdal in a virtual environment:

1. create the virtual environment

```$ python3 -m venv ~/.virtualenvs/gis ```

2. activate the virtual environment

```$ source ~/.virtualenvs/gis/bin/activate ```

3. in the virtual environment install gdal version similar in your system

```$ pip install --global-option=build_ext --global-option="-I/usr/include/gdal" GDAL==`gdal-config --version` ```

