class Calculatrice :
    def __init__(self):
        self.resultat = 0;

    def addition(self):
        self.resultat = self.x + self.y
        self.afficher("+")

    def additionV2(self, op1, op2):
        self.x = op1
        self.y = op2
        self.addition()

    def afficher(self, operateur):
        print(self.x,operateur,self.y,"=",self.resultat)

    def multiplication(self, num1, num2):
        self.x = num1
        self.y = num2
        self.resultat = num1 * num2
        self.afficher("x")



p1 = Calculatrice()
p1.x=10
p1.y=10
p1.addition()
p1.additionV2(3,5)
p1.multiplication(6,2)
print ( p1.resultat )
