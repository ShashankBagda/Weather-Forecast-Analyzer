from email.base64mime import header_encode
import http.client
import sys
import os
import time

str = ''
conn = http.client.HTTPSConnection("foreca-weather.p.rapidapi.com")

headers = {'X-RapidAPI-Key': "9d7789caa1msh2d7e3cdfe79f8d4p168a3fjsn292f57c1d45c",
           'X-RapidAPI-Host': "foreca-weather.p.rapidapi.com "}

print('\n'+"Select your choice : "+'\n' +
      "Enter 1 - To get Weather Data using City Name" + '\n' +
      "Enter 2 - To get Weather Data using City ID"+'\n')
choice = input("Enter your choice : ")

if choice == '1':
    city_name = input("Enter city name : ")
    data = "/location/search/" + city_name + "?lang=en"
    print(data+'\n')
    conn.request("GET", data, headers=headers)

    res = conn.getresponse()
    data = res.read()
    data_str = data.decode("utf-8")

    print(data_str + '\n')

    for i in range(20, 30):
        if (data_str[i] != ','):
            str += data_str[i]
    print('City ID : '+str+'\n')

    set = input('Enter Data Range : ')
    set = int(set)
    for j in range(0, set):

        data = "/current/" + str + '?tempunit=C&windunit=KMH&lang=en'
        conn.request("GET", data, headers=headers)

        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))

        time.sleep(2)


elif choice == '2':
    city_id = input("Enter city ID : ")
    data = "/current/" + city_id + '?tempunit=C&windunit=KMH&lang=en'
    conn.request("GET", data, headers=headers)

    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

else:
    print("Enter Valid Choice... Try Again"+'\n')
