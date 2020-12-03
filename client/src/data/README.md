# Preparing data
### Retrieve the shapefiles
```bash 
curl -k -X GET --header "Accept: application/zip" --header "Authorization: Bearer TOKEN" -o ./shapefiles.zip "https://opendata-api.stib-mivb.be/Files/2.0/Shapefiles"
```

### Preparing the data 
#### Convert the shapefiles into geojsons
> https://www.npmjs.com/package/shp2json

#### Clean the data
> https://github.com/node-geojson/geojson-pick

#### Reduce the precision
> https://github.com/perrygeo/geojson-precision

Or simply do these steps with :
> https://mapshaper.org/

### Rename the geojsons 
```bash
mv ACTU_STOPS.geojsons stops.json && rm stops.geojsons
mv ACTU_LINES.geojsons lines.json && rm lines.geojsons
```