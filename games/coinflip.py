from microbit import *
import random

display.scroll("Kop=A, Munt=B")

keuze = ""

while True:
    if button_a.is_pressed():
        keuze = "kop"
        break
 

    if button_b.is_pressed():
        keuze = "munt"
        break

    
x=(str(random.randint(1,2)))
if x==1:
    x="kop"
else:
    x="munt"



if keuze==x:
    display.scroll("Geraden")
else:
    display.scroll("Nope")
