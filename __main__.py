import random
import os
import sys 
import time

mazzo=[
                "Ac", "Aq", "Af", "Ap",
                "2c", "2q", "2f", "2p",
                "3c", "3q", "3f", "3p",
                "4c", "4q", "4f", "4p",
                "5c", "5q", "5f", "5p",
                "6c", "6q", "6f", "6p",
                "7c", "7q", "7f", "7p",
                "8c", "8q", "8f", "8p",
                "9c", "9q", "9f", "9p",
                "10c", "10q", "10f", "10p",
                "Jc", "Jq", "Jf", "Jp",
                "Qc", "Qq", "Qf", "Qp",
                "Kc", "Kq", "Kf", "Kp"
            ]

mazzo_reset=[
                "Ac", "Aq", "Af", "Ap",
                "2c", "2q", "2f", "2p",
                "3c", "3q", "3f", "3p",
                "4c", "4q", "4f", "4p",
                "5c", "5q", "5f", "5p",
                "6c", "6q", "6f", "6p",
                "7c", "7q", "7f", "7p",
                "8c", "8q", "8f",  "8p",
                "9c", "9q", "9f", "9p",
                "10c", "10q", "10f", "10p",
                "Jc", "Jq", "Jf", "Jp",
                "Qc", "Qq", "Qf", "Qp",
                "Kc", "Kq", "Kf", "Kp"
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
            risp=int(input("1- Stai\n2-Chiama carta\n3-Raddoppia\n4-Split\n->"))
            if risp==1:
                tBanco()
                break
            elif risp==2:
                call()
            elif risp==3:
                raddoppio()
            elif risp==4:
                split()
    else:
        risp=0
        while not 1<=risp<=4:
            risp=int(input("1- Stai\n2-Chiama carta\n3-Raddoppia\n->"))
            if risp==1:
                tBanco()
                break
            elif risp==2:
                call()
            elif risp==3:
                raddoppio()

def valueCheck(g):
    val=0
    acePresent=False
    for ele in g:
        val+=carte_valori[ele[0]]
        if ele[0]=="A":
            acePresent=True
    if val >22  and acePresent:
        val-=10
    return(val)

def call(p1):
    p1.append(mazzo[0])
    del mazzo[0]
    print(p1, valueCheck(p1))
    if valueCheck(p1)==21:
        print("Blackjack!")
        tBanco()
    if valueCheck(p1)<22:
        risp=0
        while not 1<= risp <=2:
            risp=int(input("1-Stai\n2-Chiama carta\n->"))
            if risp==1:
                tBanco()
                break
            elif risp==2:
                call()
    else:
        print("Hai sballato")

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
    call(p1)
    call(p1_1)
            
def tBanco():
    #turn
    while valueCheck(banco)<=16:
        banco.append(mazzo[0])
        del mazzo[0]
        print(banco, "->", valueCheck(banco))
    if valueCheck(banco)==21:
        print("Blackjack!")
    if valueCheck(banco)<22:
        print(valueCheck(banco))
        winCheck()
    else:
        print("Il banco sballa, hai vinto")
        
def winCheck():
    if splitted:
        if valueCheck(p1)==valueCheck(banco) and valueCheck(p1_1)==valueCheck(banco):
            print("parità")
            #vuoi rigiocare?
        elif valueCheck(p1)<valueCheck(banco) and valueCheck(p1_1)<valueCheck(banco):
            print("Vince il banco")
            #vuoi rigiocare
        else:
            print("Hai vinto")
            #vuoi rigiocare?
    else:
        if valueCheck(p1)==valueCheck(banco):
            print("parità")
        elif valueCheck(p1)<valueCheck(banco):
            print("Vince il banco")
        else:
            print("Hai vinto")

shuffle()
distro()
print(banco,"->", valueCheck(banco))
print(p1, "->", valueCheck(p1))
firstAction()

#aggiungi il sistema di puntate
#aggiungi il pagamento da parte del banco
#aggiungi il file di cache
#aggiungi il loading screen
#aggiungi la funzione turn() per la visualizzazione da terminale