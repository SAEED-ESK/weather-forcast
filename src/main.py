#Weather report
from bs4 import BeautifulSoup
import requests

#header user agent is a string allows the server to identify the O.S and application
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


def weather(city):
    # Replaces the space with + operator
    city = city.replace(" ","+")
    #requests and get function to get the information from the URL provided
    res = requests.get(
        f"https://www.google.com/search?q={city}&oq={city}"
        f"&aqs=chrome.1.69i59l2j69i57j0i512l7.5274j0j9"
        f"&sourceid=chrome&ie=UTF-8", headers=headers)
    print("Searching in google......\n")
    #Navigates on that particular website ,extract and store the data in soup object
    soup = BeautifulSoup(res.text,'html.parser')
    #gets the information of location 
    location = soup.select('#wob_loc')[0].getText().strip()
    #gets the information of time
    time = soup.select('#wob_dts')[0].getText().strip()
    #gets the desired information
    info = soup.select('#wob_dc')[0].getText().strip()
    #gets the weather information
    weather = soup.select('#wob_tm')[0].getText().strip()

    print(location)
    print(time) 
    print(info)
    print(weather+"°C")

if __name__ == "__main__":
    city = input("enter the city name: ")

    #Concatenating the city name and weather and passing the city object to weather function
    weather(city + " weather")