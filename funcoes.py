import time
import os



def limparTela():
    os.system("cls")

def aguardando(segundos):
    time.sleep(segundos)

def escreverTela(texto):
    print(texto.upper())  # deixa tudo em maiúsculo independente de como for escrito

     # deixar só os assets aqui, pra lembrar e facilitar uso 
     # deixa o core do arquivo no main.py

def dicas():
    x=0
    lista_dica = []
    while(x < 3):
        dica = input("Digite uma dica sobre a palavra: ")  
        lista_dica.append(dica)
        x = x + 1
    return lista_dica

def vencedor(): 
    print("            ___         ")
    print("         '.=====.'      ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         .' '.          ")
    print("        '-------'       ") 
    print("         VENCEDOR       ")
    print("                        ")

def perdedor():

 print("       ____                                        ")
 print("     .'``.``.                                      ")
 print("    / (o) `, `.                                    ")
 print("  -=`,     ;   `.                                  ")
 print("          :      `-.                               ")
 print("      /    ';        `.                            ")
 print("     /      .'         `.                          ")
 print("    |     (      `.     `-.._                      ")
 print("           ` ` `.          `-.._                   ")
 print("        `.   ;`-.._ `-`..-. `-.   `-._             ")
 print("         `..'     `-.```.  `-._ `-.._.'            ")
 print("             `--....-`--'      `-.,'               ")
 print("                ._)/                               ")
 print("               /--(                                ")
 print("           -./,--'`-,                              ")
 print("         ,^--(                     você perdeu :)' ")
 print("         ,--' `-,                                  ") 
print("                                                    ")




