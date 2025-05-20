// Visualization of GOOGLE/Research/open-buildings/v3/polygons.

// Load the building polygons
var t = ee.FeatureCollection('GOOGLE/Research/open-buildings/v3/polygons');

// Define Area of Interest (projects/ee-kingsleychika-rwwetland/assets/Ruilindo_AOI)
var roi = roi;

// Add roi to the map
Map.addLayer(roi, {}, 'Rulindo Study Area Building');
Map.centerObject(roi, 12);

// Filter buildings based on confidence levels
var t_065_070 = t.filter('confidence >= 0.65 && confidence < 0.7');
var t_070_075 = t.filter('confidence >= 0.7 && confidence < 0.75');
var t_gte_075 = t.filter('confidence >= 0.75');

// Add layers to the map
Map.addLayer(t_065_070, {color: 'FF0000'}, 'Buildings confidence [0.65; 0.7)');
Map.addLayer(t_070_075, {color: 'FFFF00'}, 'Buildings confidence [0.7; 0.75)');
Map.addLayer(t_gte_075, {color: '00FF00'}, 'Buildings confidence >= 0.75');

Map.setOptions('SATELLITE');

// Filter the FeatureCollection based on roi and then export
var t_roi = t.filterBounds(roi);
Export.table.toDrive({
  collection: t_roi,
  description: 'OpenBuildings',
  fileFormat: 'GeoJSON', // 'SHP' for Shapefile format
  folder: 'Google_Earth_Engine_Export', // Location Folder Google Drive in my Drive
  fileNamePrefix: 'Buildings'
});