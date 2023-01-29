import http.client

conn = http.client.HTTPSConnection("open-weather13.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "9d7789caa1msh2d7e3cdfe79f8d4p168a3fjsn292f57c1d45c",
    'X-RapidAPI-Host': "open-weather13.p.rapidapi.com"
}

print("Select your choice : ")
print("Enter 1 - To get weather forecast using City Name")
print("Enter 2 - To get weather forecast using Latitude and Longitude")
print("Enter 3 - To get weather forecast of next 5 Days")
choice = input("Enter your choice : ")

if choice == '1':
    city_name = input("Enter city name : ")
    data = "/city/" + city_name
    print(data)
    conn.request("GET", data, headers=headers)
elif choice == '2':
    longi = input("Enter Longitude of your location : ")
    lati = input("Enter Latitude of your location : ")
    data = "/city/latlon/" + lati + longi
    conn.request("GET", data, headers=headers)
elif choice == '3':
    longi = input("Enter Longitude of your location : ")
    lati = input("Enter Latitude of your location : ")
    data = "/city/fivedaysforcast/" + lati + '/' + longi
    conn.request("GET", data, headers=headers)
else:
    print("Enter Valid Choice... Try Again")
# conn.request("GET", "/city/latlon/30.438/-89.1028", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
