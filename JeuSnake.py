from tkinter import *
from random import*

#cree une fenetre ( la racine )  :
window = Tk()
 
#Nom de la fentre :  
window.title("Snake")

#Taille de la fenetre:
window.geometry("600x600")

#La fenetre de change plus de taille:
window.resizable(width=False, height=False)

#Couleur d'arrière plan de la fenetre
window.config(background="green")

#crée la boite 
frame = Frame(window)

#ajouter un premier texte
label_title = Label(frame, text="SNAKE", font =("Algerian", 90), bg="green")

# On fait apparaitre le label dans la fenetre 
label_title.pack()

#ajouter un premier bouton
start_button = Button(frame, text="Play",font=("Ariel", 30), bg="white", fg="black")

#Detruit la fenetre
start_button.quit()

#On fait apparaitre le label dans la fenetre:
start_button.pack()

#On fait apparaitre la boite dans la fenetre:
frame.pack(expand=YES)

#On cree une nouvelle fenetre:
window = Tk()

#Titre de la fenetre Toplevel
window.title("SNAKE")

#Taille de la fenetre Toplevel
window.minsize(600, 600)

#La fenetre ne change plus de taille
#window.resizable(width=False, height=False)

#On crée un canevas : 
ground = Canvas(window,width = 600 , height = 600 , bd=0, bg="green")
ground.pack(padx=10,pady=10)
 
#Une fonction pour le deplacement vers la droite :
def droite(event):
    global dx, dy #Les coordonnés initial pour toute fonctions
    dx=5  # coordonnés de l'abscisse
    dy=0  # coordonés de l'ordonné
    
#Une fonction pour le déplacement vers la gauche :
def gauche(event): 
    global dx, dy #Les coordonnés initial pour toutes fonctions
    dx=-5  # coordonnés de l'abscisse
    dy=0  # coordonés de l'ordonné

#Une fonction pour le déplacement vers le haut:
def haut(event): #Les coordonnés initial pour toutes fonctions
    global dx, dy
    dx=0  # coordonnés de l'abscisse
    dy=-5 # coordonés de l'ordonné
    
#Une fonction pour le déplacement vers le bas : 
def bas(event):  #Les coordonnés initial pour toutes fonctions
    global dx, dy
    dx=0  # coordonnés de l'abscisse
    dy=5  # coordonés de l'ordonné

def stop(event):
    global dx, dy  #Les coordonnés initial pour toutes fonctions
    dx=0  # coordonnés de l'abscisse
    dy=0  # coordonés de l'ordonné
    


#On cree un carre:
carre = ground.create_rectangle(20,20,0,0,fill='red')

def deplacement():
    global dx, dy  #Les coordonnés initial pour toute fonctions
    #On deplace la balle :
    ground.move(carre,dx,dy)
    #On repete cette fonction
    window.after(20,deplacement)
 
#Coordonné du carre:
Pos_X = 60 #coordonné de l'abscisse de départ
Pos_Y = 10 # coordonés de l'ordonné de départ

#déplacement du carré au départ : 
dx=0 #coordonnés de l'abscisse de départ
dy=0 # coordonés de l'ordonné de départ
 
# On cree un obstacle

#On crée une matrice nommmé "tb" qui représente le terrain de jeu :
tb =[
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0],
[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
[0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]


# On affiche tb :
print (tb)

i = 0 # la première ligne du tableau ( initialisation)
j = 0 # la première colonne du tableau (initialisation)
while j < 30 : # ce bloc est exécuté tant que la condition (j<30 est vraie)
    while i < 30 : #ce bloc est exécuté tant que la condition (i <30 est vraie)
        if tb [j][i]== 1: #Si l'expression est vrai alors il y a un carré de couleur noir
              ground.create_rectangle(j*20,i*20,j*20+20,i*20+20,fill='black')
        i=i+1 # on augmente la valeur initiale de la ligne
    i=0
    j=j+1 # on augmente la valeur initiale de la colonne

#Food
def food():
    global appelx, appely
    
#Coordonné de la nourirure
applex=randrange(10,600,50)

#Coordonné de la nouriture
appley=randrange(10,600,50)

# nourirture jaune
f=ground.create_oval(applex-8,appley+8,applex+8,appley-8,width=1,fill="yellow")


def score():
    global s1
    print ("Score joueur 1"),score1
    ground.delete(s1)

#définition des scores
score1=0
s1=ground.create_text(500,10,text="Score 1: "+str(score1))
    
#On associe la touche droite du clavier a la fonction droite():
ground.bind_all('<Right>', droite)
#On associe la touche droite du clavier a la fonction gauche()
ground.bind_all('<Left>', gauche)
#On associe la touche droite du clavier a la fonction haut()
ground.bind_all('<Up>', haut)
#On associe la touche droite du clavier a la fonction bas()
ground.bind_all('<Down>', bas)
#On associe la touche p du clavier a la fonction pause()
ground.bind_all('<p>', stop)



#Création  d'un bouton "Quitter":
exit_button = Button(window, text="Exit", font= ("Aharoni", 20), bg= "black", fg="white", command = window.destroy)

#On ajoute l'affichage du bouton dans la fenêtre tk:
exit_button.pack()

#On afiche les déplacement 
deplacement()

#On affiche tout les widget de la fenetre
window.mainloop()
