import random
import os
import time

mazzo=[
                "A♥", "A♦", "A♣", "A♠",
                "2♥", "2♦", "2♣", "2♠",
                "3♥", "3♦", "3♣", "3♠",
                "4♥", "4♦", "4♣", "4♠",
                "5♥", "5♦", "5♣", "5♠",
                "6♥", "6♦", "6♣", "6♠",
                "7♥", "7♦", "7♣", "7♠",
                "J♥", "J♦", "J♣", "J♠",
                "Q♥", "Q♦", "Q♣", "Q♠",
                "K♥", "K♦", "K♣", "K♠"
            ]

mazzo_reset=[
                "A♥", "A♦", "A♣", "A♠",
                "2♥", "2♦", "2♣", "2♠",
                "3♥", "3♦", "3♣", "3♠",
                "4♥", "4♦", "4♣", "4♠",
                "5♥", "5♦", "5♣", "5♠",
                "6♥", "6♦", "6♣", "6♠",
                "7♥", "7♦", "7♣", "7♠",
                "J♥", "J♦", "J♣", "J♠",
                "Q♥", "Q♦", "Q♣", "Q♠",
                "K♥", "K♦", "K♣", "K♠"
            ]

carte_valori={
                "A"     :   11,
                "2"     :   2,
                "3"     :   3,
                "4"     :   4,
                "5"     :   5,
                "6"     :   6,
                "7"     :   7,
                "8"     :   8,
                "9"     :   9,
                "1"   :    10,
                "J"      :   10,
                "Q"    :    10,
                "K"     :    10
}

banco=[]

p1, p1_1 = [] , []

rad=False
splitted=False

def shuffle():
    random.shuffle(mazzo)

def distro():
    for i in range (2):
        p1.append(mazzo[0])
        del mazzo[0]
        banco.append(mazzo[0])
        del mazzo[0]

def splitCheck():
    if p1[0][0]==p1[1][0]:
        return(True)
    else:
        return(False)

def firstAction():
    if splitCheck():
        risp=0
        while not 1<=risp<=4:
            risp=int(input("1- Stai\n2- Chiama carta\n3- Raddoppia\n4- Split\n->"))
            if risp==1:
                tBanco()
                break
            elif risp==2:
                call(p1)
            elif risp==3:
                raddoppio()
            elif risp==4:
                split()
    else:
        risp=0
        while not 1<=risp<=4:
            risp=int(input("1- Stai\n2- Chiama carta\n3- Raddoppia\n->"))
            if risp==1:
                tBanco()
                break
            elif risp==2:
                call(p1)
            elif risp==3:
                raddoppio()

def valueCheck(g):
    val=0
    acePresent=0
    for ele in g:
        val+=carte_valori[ele[0]]
        if ele[0]=="A":
            acePresent+=1
    if val >=22  and acePresent:
        while val>=22 and acePresent!=0:
            val-=10
            acePresent-=1
    return(val)

def call(g):
    os.system('cls' if os.name == 'nt' else 'clear')
    g.append(mazzo[0])
    del mazzo[0]
    table(g)    
    if valueCheck(g)==21 and splitted==False:
        print("Blackjack!")
        tBanco()
    elif valueCheck(g)<22 and splitted==False:
        risp=0
        while not 1<= risp <=2:
            risp=int(input("1-Stai\n2-Chiama carta\n->"))
            if risp==1:
                tBanco()
                break
            elif risp==2:
                call(g)
    elif valueCheck(g)==21 and splitted==True:
        print("Blackjack!")
    elif  valueCheck(g)<22 and splitted==True:
        risp=0
        while not 1<= risp <=2:
            risp=int(input("1-Stai\n2-Chiama carta\n->"))
            if risp==1:
                break
            elif risp==2:
                call(g)
    elif valueCheck(g)>=22 and splitted==True:
        print("Hai sballato")
    elif valueCheck(g)>=22 and splitted==False:
        print("Hai sballato")
        askForReplay()
        

def raddoppio():
    rad=True
    p1.append(mazzo[0])
    del mazzo[0]
    print(p1,"->" ,valueCheck(p1))
    if valueCheck(p1)==21:
        print("Blackjack!")
        tBanco()
    elif valueCheck(p1)>21:
        print("Hai sballato")
    else:
        tBanco()

def split():
    splitted=True
    p1_1.append(p1[1])
    del p1[1]
    p1.append(mazzo[0])
    del mazzo[0]
    p1_1.append(mazzo[0])
    del mazzo[0]
    print("\n\n Ecco la prima parte dello split")
    call(p1)
    print("\n\n Ecco la seconda parte dello split")
    call(p1_1)
            
def tBanco():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Tocca al banco!")
    print("le carte del banco: ", banco, "-->",valueCheck(banco),end="\n\n")
    print("la tua mano: ", p1, "-->",valueCheck(p1), end="\n\n")
    while valueCheck(banco)<=16:
        banco.append(mazzo[0])
        print("il banco pesca...")
        del mazzo[0]
        print("le carte del banco: ", banco, "-->",valueCheck(banco),end="\n\n")
    if valueCheck(banco)==21:
        print("Blackjack!")
    if valueCheck(banco)<22:
        winCheck()
    else:
        print("Il banco sballa, hai vinto")
        askForReplay()

        
def winCheck():
    if splitted:
        if valueCheck(p1)==valueCheck(banco) and valueCheck(p1_1)==valueCheck(banco):
            print("parità")
            askForReplay()
        elif valueCheck(p1)<valueCheck(banco) and valueCheck(p1_1)<valueCheck(banco):
            print("Vince il banco")
            askForReplay()
        else:
            print("Hai vinto")
            askForReplay()
    else:
        if valueCheck(p1)==valueCheck(banco):
            print("parità")
            askForReplay()
        elif valueCheck(p1)<valueCheck(banco):
            print("Vince il banco")
            askForReplay()
        else:
            print("Hai vinto")
            askForReplay()



def table(n):
    print("le carte del banco: ", banco[0], "*", end="\n\n")
    print("la tua mano: ", n, "-->",valueCheck(p1), end="\n\n")




def load():
    for i in range(6):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n")
        print("Caricamento")
        print("° "*(i+1))
        time.sleep(0.5)
    
    time.sleep(1)
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n\n")
    print(" _______  __                   __                                  __     ")  
    print("|       \|  \                 |  \                                |  \      ")
    print("| ▓▓▓▓▓▓▓\ ▓▓ ______   _______| ▓▓   __       __  ______   _______| ▓▓   __ ")
    print("| ▓▓__/ ▓▓ ▓▓|      \ /       \ ▓▓  /  \     |  \|      \ /       \ ▓▓  /  \ ")
    print("| ▓▓    ▓▓ ▓▓ \▓▓▓▓▓▓\  ▓▓▓▓▓▓▓ ▓▓_/  ▓▓      \▓▓ \▓▓▓▓▓▓\  ▓▓▓▓▓▓▓ ▓▓_/  ▓▓")
    print("| ▓▓▓▓▓▓▓\ ▓▓/      ▓▓ ▓▓     | ▓▓   ▓▓      |  \/      ▓▓ ▓▓     | ▓▓   ▓▓ ")
    print("| ▓▓__/ ▓▓ ▓▓  ▓▓▓▓▓▓▓ ▓▓_____| ▓▓▓▓▓▓\      | ▓▓  ▓▓▓▓▓▓▓ ▓▓_____| ▓▓▓▓▓▓\ ")
    print("| ▓▓    ▓▓ ▓▓\▓▓    ▓▓\▓▓     \ ▓▓  \▓▓\     | ▓▓\▓▓    ▓▓\▓▓     \ ▓▓  \▓▓\ ")
    print(" \▓▓▓▓▓▓▓ \▓▓ \▓▓▓▓▓▓▓ \▓▓▓▓▓▓▓\▓▓   \▓▓__   | ▓▓ \▓▓▓▓▓▓▓ \▓▓▓▓▓▓▓\▓▓   \▓▓")
    print("                                       |  \__/ ▓▓              ")             
    print("                                        \▓▓    ▓▓                    ")       
    print("                                         \▓▓▓▓▓▓           ")                 

    print("-------------------")
    print("╔═══╗    ╔═══╗╔═══╗\n║╔═╗║    ║╔═╗║║╔═╗║\n║║ ╚╝╔╗╔╗║╚══╗║║ ║║\n║║ ╔╗║║║║╚══╗║║║ ║║\n║╚═╝║║╚╝║║╚═╝║║╚═╝║\n╚═══╝╚══╝╚═══╝╚═══╝")
    print("-------------------")
    time.sleep(2.4)

    os.system('cls' if os.name == 'nt' else 'clear')

def play():
    shuffle()
    distro()
    table(p1)
    firstAction()

def askForReplay():
    risp=""
    while True:
        risp=input("Vuoi rigiocare? [y/n] \n")
        if risp=="y":
            print("Perfetto, ricominciamo!")
            time.sleep(1.8)
            os.system('cls' if os.name == 'nt' else 'clear')
            play()
        elif risp=="n":
            print("Va bene, rigioca quando vuoi")
        else:
            print("Davvero non riesci scrivere 'y' o 'n'? \nFiga zio ma ti svegli??")

def main():
    load()
    play()

if __name__ == "__main__":
    main()



#rendi obj oriented :)    
#aggiungi il sistema di puntate
#aggiungi il pagamento da parte del banco
#aggiungi il file di cache
