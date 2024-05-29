## Setup

```
python3 -m venv ~/.venv/gpx4run
source ~/.venv/gpx4run/bin/activate
pip install -r requirements.txt
```

## Update PostGIS

Sync KML changes to PostGIS:

```
python postgis-update.py \
../settings/Points\ of\ Interest.kml \
../postgis/data/points-of-interest.csv
```

```
python postgis-update.py \
../settings/Destinations.kml \
../postgis/data/destinations.csv
```

```
python postgis-update.py \
../settings/Start.kml \
../postgis/data/start.csv
```