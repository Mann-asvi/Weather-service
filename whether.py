import requests

city = input("Input the city name: ")
print("Displaying Weather report for:", city)

url = 'https://wttr.in/{}'.format(city)
res = requests.get(url)
print(res.text) 