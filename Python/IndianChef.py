from Chef import Chef
class IndianChef(Chef): #this is how Indian Chef will inherit Chef
    def makeBiryani(self):
        print("Chef makes Biryani")
    def makeSpecialDish(self): #overrides the base class' make special dish
        print("Makes butter chicken")