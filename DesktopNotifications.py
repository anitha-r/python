# import required libraries
# win10toast_click : "An easy-to-use Python library for displaying Windows 10 Toast Notifications. "
# requests : Requests allows you to send HTTP/1.1 requests extremely easily.
import requests
from bs4 import BeautifulSoup
from win10toast_click import ToastNotifier
  
# create an object to ToastNotifier class
n = ToastNotifier()
  
# define a function to get the raw source data
def getdata(url):
    r = requests.get(url)
    return r.text
    

htmldata = getdata("https://weather.com/weather/today/l/Dallas+TX+USTX0321")
  
soup = BeautifulSoup(htmldata, 'html.parser')
  
current_temp = soup.find_all("span", class_= "CurrentConditions--tempValue--1RYJJ")

precip_Value = soup.find_all("div", class_= "CurrentConditions--precipValue--1RgXi")

current_loc = soup.find_all("h1", class_= "CurrentConditions--location--2_osB")

strTemp = (str(current_temp))
  
strPrecip = str(precip_Value)

strLoc = str(current_loc)   
result = "The temperature is " + strTemp[82:-9] + " in " + strLoc[48:-14] + "\n" + strPrecip[85:-14]
n.show_toast("Current weather conditions in your area", 
             result, duration = 10)