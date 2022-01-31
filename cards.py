from tkinter import *

from PIL import ImageTk, Image

import random

root = Tk()
root.title("Pokemon Card Game")
root.geometry("800x600")
root.configure(background="IndianRed3")

img = ImageTk.PhotoImage(Image.open("button.jpg"))

abra = ImageTk.PhotoImage(Image.open("abra.jpg"))
bulbasuar = ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
charmender = ImageTk.PhotoImage(Image.open("charmender.jpg"))
iyvasour = ImageTk.PhotoImage(Image.open("Iyvasour.jpg"))
jigglypuff = ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
kadabra = ImageTk.PhotoImage(Image.open("kadabra.jpg"))
meowth = ImageTk.PhotoImage(Image.open("meowth.jpg"))
nidoking = ImageTk.PhotoImage(Image.open("nidoking.jpg"))
paras = ImageTk.PhotoImage(Image.open("paras.jpg"))
persion = ImageTk.PhotoImage(Image.open("persion.jpg"))
pikachu = ImageTk.PhotoImage(Image.open("pikachu.jpg"))
ratata = ImageTk.PhotoImage(Image.open("ratata.jpg"))
squirtle = ImageTk.PhotoImage(Image.open("squirtle.jpg"))

label_image = Label(root)
label_image.place(relx = 0.5, rely=0.5, anchor=CENTER)

player1 = Label(root, text="Player 1: ", bg="red3", fg="ghost white")
player1.place(relx=0.1, rely=0.3, anchor=CENTER)

player2 = Label(root, text="Player 2: ", bg="red3", fg="ghost white")
player2.place(relx=0.9, rely=0.3, anchor=CENTER)

label_player1_score = Label(root, bg="azure2", fg="gray1")
label_player1_score.place(relx=0.1, rely=0.4, anchor=CENTER)

label_player2_score = Label(root, bg="azure2", fg="gray1")
label_player2_score.place(relx=0.9, rely=0.4, anchor=CENTER)

pokemon_list = [abra, bulbasuar, charmender, iyvasour, jigglypuff, kadabra, meowth, nidoking, paras, persion, pikachu, ratata, squirtle]
power_pokemon = [30, 60, 50, 100, 70, 70, 60, 90, 40, 70, 200, 40, 50]

player1_score = 0
def player1():
    global player1_score
    random_no = random.randint(0,12)
    random_pokemon = pokemon_list[random_no]
    label_image["image"] = random_pokemon
    random_pokemon_hp = power_pokemon[random_no]
    player1_score = player1_score + random_pokemon_hp
    label_player1_score["text"] = str(player1_score)
    
player1_button = Button(root, image=img, command=player1)
player1_button.place(relx=0.1, rely=0.6, anchor=CENTER)


player2_score = 0
def player2():
    global player2_score
    random_no2 = random.randint(0,12)
    random_pokemon2 = pokemon_list[random_no2]
    label_image["image"] = random_pokemon2
    random_pokemon2_hp = power_pokemon[random_no2]
    player2_score = player2_score + random_pokemon2_hp
    label_player2_score["text"] = str(player2_score)
    
player2_button = Button(root, image=img, command=player2)
player2_button.place(relx=0.9, rely=0.6, anchor=CENTER)

root.mainloop()