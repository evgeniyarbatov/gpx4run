import csv
import xml.etree.ElementTree as ET

import sys

def main(args):
  kml_path = args[0]
  output_path = args[1]

  with open(output_path, mode='w') as csv_file:
    csv_writer = csv.writer(csv_file)

    tree = ET.parse(kml_path)
    root = tree.getroot()

    ns = {"kml": "http://www.opengis.net/kml/2.2"}
    placemarks = root.findall(".//kml:Placemark", ns)

    for placemark in placemarks:
      name = placemark.find("kml:name", ns)
      if name is None:
        continue

      coords = placemark.find(".//kml:coordinates", ns)
      if coords is None:
        continue

      points = coords.text.strip().split()
      for point in points:
        coordinates = point.split(",")

        latitude = float(coordinates[1])
        longitude = float(coordinates[0])

        csv_writer.writerow([name.text, latitude, longitude])

if __name__ == "__main__":
  main(sys.argv[1:])