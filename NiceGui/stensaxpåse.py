from nicegui import ui
import random

def spela(val):
    val_lista=["Sten","Sax","Påse"]
    datorn = random.choice(val_lista)
    if val==datorn:
        resultat.text=f"Oavgjort! Båda valde{val}."
    elif(val=="Sten" and datorn == "Sax") or \
        (val=="Sax" and datorn == "Påse") or \
        (val=="Påse" and datorn == "Sten"):
        resultat.text=f"Du vann! {val} slår {datorn}."
    else:
        resultat.text=f"Datorn vann! {datorn} slår {val}."

ui.label("Välj ett drag:").classes('text-xl mb-4')

with ui.row():
    ui.button("Sten",on_click=lambda: spela("Sten")).classes('text-lg').props("flat").style("color:black !important;")
    ui.button("Sax",on_click=lambda: spela ("Sax")).classes('text-lg').props("flat").style("color:black !important;")
    ui.button("Påse",on_click=lambda: spela ("Påse")).classes('text-lg').props("flat").style("color:black !important;")

resultat=ui.label("Lycka till!").classes('mt-4 font-bold')

ui.run(native=True)