def  est_port_valide(port) :
    if  1 <= port <= 65535:
        return True
    else:
        return False
    
def service_associe_port(port):
    if est_port_valide(port):
        if port == 80:
            print("HTTP")
        elif port == 443:
            print("HTTPS")
        elif port == 21:
            print("FTP")
        elif port == 22:
            print("SSH")
        elif port == 25:
            print("SMTP")
    else:
        print("Port non reconnu")

    
def saisir (message):
    valeur_int = -1
    while valeur_int == -1:
        valeur_str = input(f"Saisir {message}? : ")
        try:
            valeur_int = float(valeur_str) # si le cast fonctionne je passe à la suite :(else) et je saute except
        except: # si le cast ne fonctionne pas je lève une exception
            print("Vous n'avez pas saisi une valeur numérique")
        else:
            if valeur_int == 0: # si la valeur saisie est = zéro
                print("Vous avez saisi zéro")
            elif valeur_int < 0: # si la valeur saisie est négative
                print("Vous avez saisi une valeur négative")
                valeur_int = 0   #je réaffecte 0 à valeur_int pour revenir à la condition initiale
            elif valeur_int > limite:
                print(f"Vous avez saisi une valeur > {limite}")
                valeur_int = 0
            else: # si la valeur saisi est correcte (différente de zéro, n'est pas négative et une valeur numérique)
                print("Vous avez saisi {}".format(valeur_int))
    return valeur_int