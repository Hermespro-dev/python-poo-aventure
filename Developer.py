class Developer :
    def __init__(self, name, hourly_rate, experience_years):
        # Attributs privés (avec '_')
        self._name = name
        self._hourly_rate = hourly_rate # Notre objectif: 50$/h 
        self._experience_years = experience_years
    
    # Proprièté 1: getter pour le nom
    @property
    def name(self):
        return self._name
    
    # Propriété 2: vérifie si l'objectif de tarif est atteint
    @property
    def target_archieved(self):
        return self._hourly_rate >= 50.0
    
    # Méthode de classe
    @classmethod
    def get_motto(cls):
        return "Apprendre, coder, réussir !"
    
    # Méthode magique __str__ (pour print)
    def __str__(self):
        return f"je m'appelle {self._name}."
    
    # Méthode magique __repr__ (pour le débogage)
    def __repr__(self):
        return f"Developer('{self._name}', {self._hourly_rate}, {self._experience_years})"
    
    
    
# Code pour tester rapidement
if __name__ == "__main__":
    moi = Developer("Hermes", 20, 1)
    print(moi)
    print(f"Objectif atteint ? {moi.target_archieved}")
    print(Developer.get_motto())