from ast import If
from tkinter import END
from turtle import end_fill
import streamlit as st
import os
import json
import streamlit as st
import pandas as pd
import altair as alt

#Liste
dic ={
    "Felix" :1,
    "Johannes" :2,
    "Stefan" :3,
    "Diego" :4,
    "Samir" :5,
    "Fabian" :6,
    "David" :7,
    "Vinko" :8,
}

Temp={
    "Aussentemp": 18,
    "innentemp": 22,
    "Vorlauftemp": 25,
    "rücklauftemp":20
}
Klassenliste=[
    "Felix","Bärtschi",
    "Johannes","Gotsch",
    "Stefan", "Burgherr",
    "Diego", "Bacao",
    "Samir","Rais",
    "Fabian","Heist",
    "David","Sigrist",
    "Vinko","Varkas",
]


#Klasse=pd.DataFrame(Klassenliste.items(),columns=["Vorname","Nachname"])
df = pd.DataFrame(dic.items(),columns=["Name","Nummer"])
Temperaturen = pd.DataFrame(Temp.items(),columns=["Temp","Grad"])


#unterlisten
sections1= st.sidebar.radio("TEST", ("Bilder", "Klassenliste", "Button", "Diagramm", "Leer1"))
sections2= st.sidebar.radio("Kategorien Projektarbeit", ("Wetterdaten ☀️", "Lichtsteuerung 💡", "Storensteuerung 🪟", "Gebäudeoptimierung 🏠", 
"Heizungssteuerung 🔥", "Förderbandsteuerung ⚙️", "Liftsteuerung 🛗", "Leer2"))
     #Bilder anzeigen (Wenn bild wie unten angezeigt werden soll muss das bild im gleichen Ordner sein wie die py-datei)

if sections1== "Bilder": 
    st.title("Bilder")
    from PIL import Image
    image= Image.open("Mustang Shelby.jpg")
    st.image(image)
    with open("Mustang Shelby.jpg", "rb") as file:
        btn = st.download_button(
            label="Download image",
            data=file,
            file_name="Mustang Shelby.jpg",
            mime="image/png"
          )

    
elif sections1=="Klassenliste":
    st.title("Klassenliste")
    st.write(df)

elif sections1=="Button":
    st.title("Button")
    #Knopf erstellen 
    if not os.path.isfile("KLICK MY"):
        with open("KLICK MY", "w")as f:
            json.dump({"clicks":0},f)

    with open ("KLICK MY")as f:
        counter = json.load(f)["clicks"]

    if st.button("KLICK MY"):
        counter +=1

    st.write(f"The button was clicked {counter} times")

    with open ("KLICK MY", "w")as f:
        json.dump({"clicks": counter}, f)
    

elif sections1=="Diagramm":
    
    st.title("Diagramme")

    #verschiedene Diagramme und Tabellen können erstellt werdne wie z.B. bar_chart,area_chart,usw
    st.bar_chart(data=Temperaturen,x="Temp", y="Grad")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Aussentemp", "18 °C", "1.2 °C")
    col2.metric("Innentemp", "22 °C", "0.8 °C")
    col3.metric("Vorlauftemp", "25 °C", "3 °C")
    col4.metric("Rücklauftemp", "20 °C", "-1.2 °C")



elif sections2== "Wetterdaten ☀️":
    st.title("Wetterdaten")
    st.header("Temperatur-Unterschied an Land 1880 bis 2020")
    #Diagramm für den Temperaturverleuf erstellt und Grafik so verändert, dass sie auf meine Bedürfnisse stimmt.

    df = pd.read_csv("C:/Users/stefa/Documents/Weiterbildung Gebäudetechniker_Informatiker/Semester 3/Programmieren 2/GlobalTemp.csv")
    df = df.iloc[:17,:]
    chart = alt.Chart(df).mark_line().encode(x=alt.X('Year'), y=alt.Y('T (degC)'), color=alt.Color("Verlauf:N")).properties(title="Temperatur-Unterschied von 1880-2020") 
    st.altair_chart(chart, use_container_width=True)
    
    #Es war sehr schwierig die Grafik richtig hin zu bekommen... Nach langer Zeit hat es dann geklappt!
    #der Code bin=alt.Bin(maxbins=12) Ging leider nicht

    st.write("Der Temperaturverleuf hat sich erheblich erhöht. Wir müssen an unsere Zukunft denken und versuchen die Erderwärmung zu stoppen!")
    from PIL import Image
    image= Image.open("Klimawandel.jpg")
    st.image(image)

elif sections2=="Lichtsteuerung 💡":
    st.title("Lichtsteuerung")
    #Lichtsteuerung erstellt mit Buttons EIN/AUS und Anzeige mit Bild und Text. 
   
    if not os.path.isfile("EIN"):
        with open("EIN", "w")as f:
            json.dump({"clicks":0},f)

    with open ("EIN")as f:
        counter = json.load(f)["clicks"]
        
    if st.button("EIN"):
        counter +=1
        from PIL import Image
        image= Image.open("Lampe EIN.jpg")
        st.image(image)

    st.write(f"Die Lampe ist Eingeschaltet {counter}")
    
    if not os.path.isfile("AUS"):
        with open("AUS", "w")as f:
            json.dump({"clicks":0},f)

    with open ("AUS")as f:
        counter = json.load(f)["clicks"]
        
    if st.button("AUS"):
        counter +=1
        from PIL import Image
        image= Image.open("Lampe AUS.jpg")
        st.image(image)

    st.write(f"Die Lampe ist Ausgeschaltet {counter}")


elif sections2=="Storensteuerung 🪟":
    st.title("Storensteuerung")
    #Steuerung mit Buttons Auf/AB Erstellt und Video eingefügt.
 
    if st.button("AB↓"):
        video_file = open('Storen unten.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)

    if st.button("AUF↑"):
        video_file = open('Storen.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)

elif sections2=="Gebäudeoptimierung 🏠":
    st.title("Gebäudeoptimierung")

    def optimize_building(building_parameters):
    #Code zur Optimierung des Gebäudes anhand der angegebenen Parameter. Daür wurde die Buttton erstellt und die Parameter definiert.

     optimized_parameters = {'Wand Dicke': 10, 'Dach Isolation': 20, 'Fenster Dicke': 0.8}
     return optimized_parameters

    building_parameters = {'Wand Dicke': 5, 'Dach Isolation': 10, 'Fenster Dicke': 0.6}
    st.markdown('Gebäudeparameter:')
    st.markdown(building_parameters)

    if st.button('Optimieren'):
        optimized_parameters = optimize_building(building_parameters)
        st.markdown('Optimierte Gebäudeparameter:')
        st.markdown(optimized_parameters)


elif sections2=="Heizungssteuerung 🔥":
    st.title("Heizungssteuerung")
    #Die Schalter Heizen/Kühlen wurden definiert und eine Steuerung erstellt für Heizen +1 und Kühlen -1.
   
    mode = st.radio('Auswahl:', ('Heizen', 'Kühlen'))
    current_temperature = 21

    if mode == 'Heizen':
        current_temperature += 1
        st.markdown(f'Die aktuelle Temperatur beträgt {current_temperature}°C.')
    else:
        current_temperature -= 1
        st.markdown(f'Die aktuelle Temperatur beträgt {current_temperature}°C.')

elif sections2=="Förderbandsteuerung ⚙️":
    st.title("Förderbandsteuerung")
    #Die anfängliche Fördermenge wird auf 0 gesetzt. Danach Erstellung eines Sliders, mit dem die Fördermenge verändert werden kann. 
    #Grösse der Veränderung der Fördermenge defniert und eine Anzeige erstellt der aktuellen Fördermenge.
   
    fördermenge = 0
    fördermenge_slider = st.slider("Wähle die Fördermenge:", 0, 100, 0)
    fördermenge = fördermenge_slider
    st.write(f"Die aktuelle Fördermenge beträgt: {fördermenge}")


elif sections2=="Liftsteuerung 🛗":
    st.title("Liftsteuerung")
    #Erstelle Buttons für die beiden Sensoren und Programmierung der Texte mit Sleepfunktion.

    if st.button("Sensor 1, EG"):

        texts = [
            "Lift befindet sich im 4. Stock 🛗",
            "Lift befindet sich im 3. Stock 🛗",
            "Lift befindet sich im 2. Stock 🛗",
            "Lift befindet sich im 1. Stock 🛗",
            "Lift befindet sich im EG 🛗 sie können nun einsteigen"
        ]


        for text in texts:
            st.write(text)
            for i in range(9000000):
                pass 
         

    if st.button("Sensor 2, 4. Stock"):
        texts = [
            "Lift befindet sich im EG 🛗",
            "Lift befindet sich im 1. Stock 🛗",
            "Lift befindet sich im 2. Stock 🛗",
            "Lift befindet sich im 3. Stock 🛗",
            "Lift befindet sich im 4. Stock 🛗 sie können nun einsteigen"
        ]

        for text in texts:
            st.write(text)
            for i in range(9000000):
                pass 
        #Hier habe ich eine Schleife erstellt, welche nur zur Verzögerung dient
        #Die Funktion Time die ich eigentlich verwenden wollte geht leider bei mir nicht!
            
       