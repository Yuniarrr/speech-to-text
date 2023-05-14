from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my-application")  # inisialisasi geolocator

# mendapatkan lokasi saat ini berdasarkan IP pengguna
location = geolocator.geocode("")

print("Latitude:", location.latitude)
print("Longitude:", location.longitude)
