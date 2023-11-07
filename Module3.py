from tkinter import *
import psycopg2
from PIL import ImageTk,Image
import requests

hostname = '20.0.35.176'
database = 'station'
username = 'postgres'
pword = 'Senay!2023'
port_id = 5432

connection = psycopg2.connect(
    host=hostname,
    dbname=database,
    user=username,
    password=pword,
    port=port_id)

cur = connection.cursor()

root = Tk()
root.geometry("900x800")

background_img = ImageTk.PhotoImage(Image.open('NS.png'))
label=Label(master=root, image=background_img, width = 900, height = 300)
label.place(y=260)

cur.execute("SELECT DISTINCT inhoud, reiziger.naam_r FROM bericht, reiziger LIMIT 5")
rows = cur.fetchall()
text = Text(master=root, width=55, height=8)
for row in rows:
    text.insert(END, ', '.join(map(str,row))+ '\n')
    text.place(x=30, y=40)

'''img1 = ImageTk.PhotoImage(Image.open('img_lift.png'))
label = Label(image=img1)
label.place(x=75, y=610)'''

img2= ImageTk.PhotoImage(Image.open('img_ovfiets.png'))
label = Label(image=img2)
label.place(x=265, y=610)

img3= ImageTk.PhotoImage(Image.open('img_toilet.png'))
label = Label(image=img3)
label.place(x=490, y=610)

'''img4= ImageTk.PhotoImage(Image.open('img_pr.png'))
label = Label(image=img4)
label.place(x=690, y=610)'''

resource_uri= "https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}"
city = "Haarlem,NL"
api_key = "8c105df757bbe23dd8a55374465888d4"

root.title(f"Station {city[:-3]} Feedback")
def weersvoorspelling(api_key, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    response_data = response.json()

    temp = response_data['main']['temp']
    temp = round(temp - 273.15, 0)

    feels_like = response_data['main']['feels_like']
    feels_l_temp = round(feels_like - 273.15, 0)

    humidity = response_data['main']['humidity']

    return {
        'temp': temp,
        'feels_like': feels_l_temp,
        'humidity': humidity
    }


weather = weersvoorspelling(api_key, city)
print(weather["temp"])
print(weather["feels_like"])
print(weather["humidity"])

city_label = Label(master=root, text= f"{city[:-3]}", font=("Arial", 30))
city_label.place(x= 650, y=30)

temp_label = Label(master=root, text=f"{weather["temp"]}°C", font=("Arial", 22))
temp_label.place(x= 690, y=80)
feels_l_label = Label(master=root, text=f"Feels like {weather["feels_like"]}°C", font=("Arial", 15))
feels_l_label.place(x= 660, y=120)
humidity_label = Label(master=root, text=f"Humidity: {weather["humidity"]}%", font=("Arial", 15))
humidity_label.place(x= 670, y=160)

wolk=Image.open('cloudy.png')
resized_image= wolk.resize((90,90))
new_image= ImageTk.PhotoImage(resized_image)
new_image_label = Label(image=new_image)
new_image_label.place(x= 550, y=20)

root.mainloop()

