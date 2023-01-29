import http.client
import sys
import os

conn = http.client.HTTPSConnection("foreca-weather.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "9d7789caa1msh2d7e3cdfe79f8d4p168a3fjsn292f57c1d45c",
    'X-RapidAPI-Host': "foreca-weather.p.rapidapi.com"
}

print('\n'+"Select your choice : "+'\n')
print("Enter 1 - To get City ID")
print("Enter 2 - To enter City ID and get Weather Data")
choice = input("Enter your choice : ")

temp = ""

if choice == '1':
    city_name = input("Enter city name : ")
    data = "/location/search/" + city_name + "?lang=en"
    print(data+'\n')
    conn.request("GET", data, headers=headers)

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

    dic = data.decode("utf-8")
    s = "id"
    ind = dic.find(s)
    print(s, end=": ")
    for i in range(ind + len(s), len(dic)):
        print(dic[i], end="")
        if dic[i] == ',':
            break


elif choice == '2':
    city_id = input("Enter city ID : ")
    data = "/current/" + city_id + '?tempunit=C&windunit=KMH&lang=en'
    conn.request("GET", data, headers=headers)
else:
    print("Enter Valid Choice... Try Again"+'\n')
    os.execl(sys.executable, sys.executable, *sys.argv)
    # exit()

# res = conn.getresponse()
# data = res.read()
# print(data.decode("utf-8"))

# dic = data.decode("utf-8")
# s = "temperature"
# ind = dic.find(s)
# print(s, end=": ")
# for i in range(ind + len(s), len(dic)):
#     print(dic[i], end="")
#     if dic[i] == ',':
#         break


# print(dic())
# print(dic["current"]["temperature"])
