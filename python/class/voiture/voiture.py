class Voiture:

    def __init__(self, m = "", mod = "", cou = ""):
        self.marque = m
        self.modèle = mod
        self.couleur = cou

    def klaxonner(self):
        print("tut tut")

    def accelerer(self):
        print("vroooom")


voiture1 = Voiture("renault", "kangoo", "blanc")
voiture2 = Voiture("Peugeot","5008", "noir")

voiture1.couleur = "bleu"
voiture1.klaxonner()


voiture2.couleur = "vert"
voiture2.accelerer()
