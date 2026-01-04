""" Exercice : Gestion d’un produit en stock.

Crée une classe Produit avec les attributs :
- nom
- prix_unitaire
- quantite_stock

Ajoutez les méthodes suivantes :
- ajouter_stock(qte)
- retirer_stock(qte)
- valeur_stock() → retourne la valeur totale (prix_unitaire * quantite_stock) """




class Produit:
    def __init__(self):
        self.nom = ""
        self.PU = float
        self.qte = float

    def ajouter_stock(self):
        self.qte = 0
        if self.nom == "":
            self.nom += input("Veuillez entrer le nom du produit que vous désirez ajouter au magasin. (Entrez juste le nom du produit s'il vous plaît !)")
            self.PU = float(input(f"Combien coûte l'unité de {self.nom} ? (Entrez juste le montant s'il vous plaît !)"))
            print(f"Ok ! Je note que vous voulez ajouter le produit {self.nom} dont l'unité coûte {self.PU} XAF.")
            qte_ajoutee = float(input(f"Quelle quantité de {self.nom} désirez-vous ajouter ?"))
            self.qte += qte_ajoutee
            print(f"Acuellement, nous avons {self.qte} de {self.nom} en stock !")
    
    def retirer_stock(self):
        produit_a_retirer = (input("Veuillez entrer le nom du produit que vous souhaitez retirer !"))
        if self.nom == produit_a_retirer:
            if self.qte != 0:
                qte_a_retirer = float(input(f"Quelle quantité de {produit_a_retirer} désirez-vous retirer ?"))
                if qte_a_retirer <= self.qte:
                    self.qte -= qte_a_retirer
                else:
                    print(f"Désolé notre stock de {produit_a_retirer} est insuffisant. Il ne nous en reste que {self.qte} !")
            else:
                print(f"Désolé, nous n'avons plus de {produit_a_retirer} en stock !")
        else:
            print(f"Désolé nous ne disposons pas de {produit_a_retirer} en stock !")

    def valeur_stock(self):
        valeur_produit = self.PU * self.qte
        print(f"Nous avons {self.qte} unité(s) de {self.nom} en stock. Donc {self.nom} a une valeur actuelle de {valeur_produit} XAF dans notre magasin !")


P1 = Produit()

P1.ajouter_stock()
P1.valeur_stock()
P1.retirer_stock()
P1.valeur_stock()