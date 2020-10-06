class Noeud:
    def __init__(self, texteEtiquette, noeudGauche = None, noeudDroit = None):
        self.etiquette = texteEtiquette
        self.droit = noeudDroit
        self.gauche = noeudGauche

    def __repr__(self):
        return " ("+str(self.gauche)+"/"+str(self.etiquette)+"\\"+str(self.droit)+") "
    
arbre1 = Noeud(10,Noeud(8,Noeud(3),Noeud(15,Noeud(20),None)),Noeud(5,Noeud(4),None))

print(arbre1)
