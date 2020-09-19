from neighbourhood import danger_zone, safety_zone
import geopy
from geopy.geocoders import GoogleV3 #import Google API
#documentation at https://geopy.readthedocs.io/en/stable/#googlev3

#initiliaze
tude_string = ""
danger_list = []
safety_list = []

#assign geolocator to _init_(params)
geolocator = GoogleV3(api_key='AIzaSyDtLyQEuPDHzgHVqVz6pOoxR7i8DzQRSDM', user_agent=None)
for i in range(len(danger_zone)):
    location = geolocator.geocode(danger_zone[i] + "Toronto, Ontario")
    tude_string = str(location.latitude) + "," + str(location.longitude)
    danger_list.append(tude_string)

for i in range(len(safety_zone)):
    location = geolocator.geocode(safety_zone[i] + "Toronto, Ontario")
    tude_string = str(location.latitude) + "," + str(location.longitude)
    safety_list.append(tude_string)

#similar to neighbourhood, archival purposes storing
with open("C:/Users/lavao/Documents/GitHub/HackMIT-2020/scripts/danger_coords.txt", "w") as output_file:
   for item in danger_list:
       output_file.write(str(item + '\n'))

with open("C:/Users/lavao/Documents/GitHub/HackMIT-2020/scripts/safety_coords.txt", "w") as output_file:
   for item in safety_list:
       output_file.write(str(item + '\n'))

if (__name__ == '__main__'):
    print (__name__ + 'has run')