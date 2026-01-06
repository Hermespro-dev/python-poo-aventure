import time

def chrono(func):
    """ chrono est un décorateur qui permet de calculer le temps d'éxécution d'une fonction """
    def wrapper():
        
        # Temps de début
        debut = time.time()
        
        # Appel de la fonction originale (func)
        resultat = func(n)
        
        # Temps de fin
        fin = time.time()
        
        # Calcul du temps écoulé
        temps_ecoule = fin - debut
        
        # Affichage du temps écoulé
        print(f"La fonction '{func.__name__}' a mis {temps_ecoule:.6f} secondes à s'exécuter.") # ':.4f' formate temps_ecoule à 4 décimales
        
        return resultat # On retourne le résultat de la fonction originale (func)
    return wrapper


# TEST DU DECORATEUR AVEC UNE FONCTION qui calcule la somme en utilisant une boucle  et une autre qui calcule la somme en utilisant une formule :

n = int(input("Veuillez entrez un nombre entier naturel ! (Nous ferons la somme de tous les entiers naturels inférieurs ou égaux à ce ce nombre de deux façons différentes et calculerons leurs temps d'exécution respectif.)"))

# Fonction que nous utiliserons pour tester le décorateur
@chrono # Pour appliquer le décorateur à la fonction suivante
def somme(n):
    """ Cette fonction calcule la somme des 1 000 000 premiers entiers naturels en utilisant la boucle for """
    somme = 0
    for i in range(n + 1):
        somme += i
    return somme

# Autre fonction
@chrono
def somme_arithmetique(n):
    """ Cette fonction calcule la somme des 1 000 000 premiers entiers naturels en utilisant la formule de la somme arihtmétique """
    #n = int(input("Veuillez entrez un entier naturels !"))  10_000_000
    somme = n * (n + 1) // 2
    return somme

# Test
if __name__ == "__main__":
    print("Début du test du décorateur 'chrono'")
    
    # Appel des fonctions décorées
    
    # somme()
    resultat = somme()
    
    # somme_arithmetique()
    resultat = somme_arithmetique()
    
    
    print(f"Résultat de la fonction: {resultat}")
    print("Test terminé !")