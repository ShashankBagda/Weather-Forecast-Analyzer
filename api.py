import http.client
import time
from email.base64mime import header_encode
from statistics import mean


def get_data(city_id):
    data = "/current/" + city_id + '?tempunit=C&windunit=KMH&lang=en'
    conn.request("GET", data, headers=headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    return 0


def Average(arr):
    return sum(arr) / len(arr)


conn = http.client.HTTPSConnection("foreca-weather.p.rapidapi.com")

headers = {'X-RapidAPI-Key': "9d7789caa1msh2d7e3cdfe79f8d4p168a3fjsn292f57c1d45c",
           'X-RapidAPI-Host': "foreca-weather.p.rapidapi.com "}

# print('\n'+"Select your choice : "+'\n' +
#       "Enter 1 - To get Weather Data using City Name" + '\n')  # + "Enter 2 - To get Weather Data using City ID"+'\n')
# choice = input("Enter your choice : ")

# if choice == '1':
city_name = input("Enter city name : ")
data = "/location/search/" + city_name + "?lang=en"
# print(data+'\n')
conn.request("GET", data, headers=headers)

res = conn.getresponse()
data = res.read()
data_str = data.decode("utf-8")

print(data_str + '\n')
str = ''
temp = ''
rel_Hud = ''
press = ''
arr = []
arr2 = []
arr3 = []

for i in range(20, 30):
    if (data_str[i] != ','):
        str += data_str[i]
print('City ID : '+str+'\n')

set = input('Enter Data Range : ')
set = int(set)
time_interval = int(input('Enter the Time Interval in seconds : '))

hrs = int((time_interval * set)/3600)
min = int(((time_interval * set) % 3600) / 60)
sec = int(((time_interval * set) % 3600) % 60)

print('\n', 'Estimated process completion time : ', hrs,
      ' Hours ', min, ' Minutes ', sec, ' Seconds', '\n')

for j in range(0, set):

    data = "/current/" + str + '?tempunit=C&windunit=KMH&lang=en'
    conn.request("GET", data, headers=headers)

    res = conn.getresponse()
    data = res.read()
    print('Data Set - ', j+1)
    data_str = data.decode("utf-8")
    print(data_str, '\n')

    time.sleep(time_interval)

    data_str = data.decode("utf-8")

    s = "temperature"
    ind = data_str.find(s)
    # print(s, end=": ")
    for i in range(ind + len(s) + 2, len(data_str)):
        if data_str[i] == ',':
            break
        else:
            temp += data_str[i]  # , end = ""
    print(temp + '\n')
    arr.append(int(temp))
    temp = ''

    s = "relHumidity"
    ind = data_str.find(s)
    # print(s, end=": ")
    for i in range(ind + len(s) + 2, len(data_str)):
        if data_str[i] == ',':
            break
        else:
            rel_Hud += data_str[i]  # , end = ""
    print(rel_Hud + '\n')
    arr2.append(int(rel_Hud))
    rel_Hud = ''

    s = "pressure"
    ind = data_str.find(s)
    # print(s, end=": ")
    for i in range(ind + len(s) + 2, len(data_str)):
        if data_str[i] == ',':
            break
        else:
            press += data_str[i]  # , end = ""
    print(press + '\n')
    arr3.append(float(press))
    press = ''

print('\n', 'Temperature Data Set - ', arr)
avg_temp = Average(arr)
print('Average Temperature : ', round(avg_temp, 3))

print('\n', 'Humidity Data Set - ', arr2)
avg_hud = Average(arr2)
print('Average Relative Humidity : ', round(avg_hud, 3))

print('\n', 'Pressure Data Set - ', arr3)
press = Average(arr3)
print('Average Pressure : ', round(press, 3))

if (press < 1000):
    print(
        '\n', "Location have Lower Pressure which indicates cloudy and rainy weather..")
    if (avg_hud > 90):
        print(
            '\n', "There might be a Heavy Rainfall, Don't forget to carry your Umbrellas...")
    elif (avg_hud > 80):
        print('\n', "There might be a Rainfall")
    elif (avg_hud > 70):
        print('\n', "There might be a Light Rainfall")
    elif (avg_hud > 60):
        print('\n', "There might be a Rainfall")
    else:
        print('\n', "Nothing to worry, Weather is Clear !!")
else:
    print(
        '\n', "Location have Higher Pressure which indicates clear and sunny weather.")
    if (avg_temp > 40):
        print('\n', "Temperature is more Hotter")
    elif (avg_temp > 30):
        print('\n', "Temperature is Hotter")
    elif (avg_temp > 20):
        print('\n', "Temperature is Moderate")
    elif (avg_temp > 10):
        print('\n', "Temperature is Colder")
    elif (avg_temp > 0):
        print('\n', "Temperature is More Colder")
    else:
        print('\n', "Temperature is soo Cold, Don't forget to wear your Jacket..")
