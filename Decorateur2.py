import time

#=============================================================================
#           CREATION DE DEUX DECORATEURS ('chorno' et 'repetition')
#=============================================================================

#--------------------------
#          chrono
#--------------------------
def chrono(func):
    """ 
    chrono est un décorateur qui permet de calculer le temps d'éxécution d'une fonction 
    
    Args:
        func: La fonction à chronométrer
    
    Returns:
        wrapper: La fonction enveloppée avec la mesure du temps 
    """
    def wrapper(*args, **kwargs):
        
        """ 
        
        '*args' : permet de predre en paramètre tous les arguments positionnels. Exple: le paramètre n
        
        '**kwargs' : permet de prendre en paramètre tous les arguments nommés. Exple: nom = "Hermes"
        
        '*args **kwargs' : permet à la fonction qui l'utilise de prendre tous les types d'arguments (arguments positionnels et arguments nommés)
        
        """
        
        # Temps de début
        debut = time.time()
        
        # Appel de la fonction originale (func)
        resultat = func(*args, **kwargs)
        
        # Temps de fin
        fin = time.time()
        
        # Calcul du temps écoulé
        temps_ecoule = fin - debut
        
        # Affichage du temps écoulé
        print(f"\n La fonction '{func.__name__}' a mis {temps_ecoule:.6f} secondes à s'exécuter.") # ':.4f' formate temps_ecoule à 4 décimales
        print(f" Résultat: {resultat} \n")
        
        if resultat is not None:
            print(f"Résultat: {resultat}")
        else:
            print("(La fonction ne retourne rien)")
        
        return resultat # On retourne le résultat de la fonction originale (func)
    return wrapper



#--------------------------
#        repetition
#--------------------------
def repetition(n_fois):
    """ 
    repetition est un décorateur qui exécute une fonction n_fois et affiche le temps moyen
    
    Args :
        n_fois: le nombre de fois à répéter l'exécution
    
    Returns :
        decorateur: Le décorateur qui sera appliqué à la fonction
    """
    
    def decorateur_repetition(func):
        """ 
        Décorateur interne qui reçoit la fonction à décorer.
        
        Args:
            func: la fonction originale à décorer
        
        Returns: 
            wrapper: La fonction enveloppée qui répète l'exécution
        """
        def wrapper(*args, **kwargs):
            """ 
            wrapper exécute la fonction n_fois fois.
            
            Args:
                *args: Arguments positionnels pour la fonction
                **kwargs: Arguments nommés pour la fonction
            
            Returns:
                Le résultat de la dernière exécution
            """
            temps_total = 0
            resultat = None
            
            print(f"\n Début des test de répétition pour '{func.__name__}'")
            print(f" Nombre de répétition: {n_fois}")
            print("-" * 40)
            
            # Boucle pour répéter l'exécution n_fois fois
            for i in range(n_fois):
                debut = time.time()
                resultat = func(*args, **kwargs)
                fin = time.time()
                temps_execution = fin - debut
                temps_total += temps_execution
                
                # Affichage du temps d'exécution de chaque itération
                print("~" * 30)
                print(f" Itération {i+1}: {temps_execution:.6f} secondes")
                print("~" * 30)
            
            temps_moyen = temps_total / n_fois
            
            print("-" * 40)
            print("Résumé des test:")
            print(f" Nombre d'exécution: {n_fois}")
            print(f" Temps total: {temps_total:.6f}")
            print(f" Temps moyen: {temps_moyen:.6f}")
            
            return resultat
        
        return wrapper
    
    return decorateur_repetition
        


# TESTS DE FONCTIONNEMENT DE **kwargs ET DU DECORATEUR AVEC UNE FONCTION qui calcule la somme en utilisant une boucle et une autre qui calcule la somme en utilisant une formule :


# Fonction que nous utiliserons pour tester le décorateur
@repetition(5) # Pour appliquer le décorateur à la fonction suivante
def somme_boucle(n):
    """ Cette fonction calcule la somme des 1 000 000 premiers entiers naturels en utilisant la boucle for """
    somme = 0
    for i in range(n + 1):
        somme += i
    return somme

# Autre fonction
@repetition(8)
def somme_formule(n):
    """ Cette fonction calcule la somme des 1 000 000 premiers entiers naturels en utilisant la formule de la somme arihtmétique """
    somme = n * (n + 1) // 2
    return somme

# UTILISATION DE **Kwargs
@chrono
def saluer(nom, fois=1):
    """ Fonction qui montre l'utilisation de **kwargs. """
    for _ in range(fois):
        print(f"Bonjour {nom} !")
    return f"Salutations terminés pour {nom}."  



# TEST
if __name__ == "__main__":
    print("=" * 60)
    print("TEST COMPLET DES DECORATEURS 'chrono' et 'repetition(n_fois)'")
    print("=" * 60)
    
    n = int(input("\n Entrez un nombre entier : "))
    
    print(f"\n Calcul pour n = {n:,} (soit {n:,})")
    print("-" * 45)
    
    # Test 1 : Boucles vs Formule
    print("\n1. COMPARAISSON D'ALGORITHMES :")
    print("-" * 35)
    
    resultat_boucle = somme_boucle(n)
    resultat_formule = somme_formule(n)
    
    print(f"\n Vérification : Les deux méthodes donnent le même résultat ? {resultat_boucle == resultat_formule}")
    print(f" Résultat : {resultat_formule:,}")
    
    # Test 2 : Avec paramètres **kwargs
    print("\n\n2. TEST AVEC **kwargs :")
    print("-" * 35)
    
    message = saluer("Hermes", fois=3)
    print(f" Retour de la fonction : {message}")
    
    print("\n" + "=" * 60)
    print("TESTS TERMINES AVEC SUCCES !")
    print("=" * 60)