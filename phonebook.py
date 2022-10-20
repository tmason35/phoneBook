from unicodedata import name


class Contact: 
    def __init__(self, name, phoneNumber, email):
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email

    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

    def getPhoneNumber(self):
        return self.phoneNumber
    def setPhoneNumber(self, phoneNumber):
        self.phoneNumber = phoneNumber

    def getEmail(self):
        return self.email
    def setEmail(self, email):
        self.email = email

    def __str__(self):
        return f"{self.name}, {self.phoneNumber}, {self.email}"

def run():
   c1 = Contact("Tyler Mason", "404-903-0676", "tylermason415@gmail.com")
   print(f"Contact's name is {c1.getName()}")
   print(f"Contact's phone number is {c1.getPhoneNumber()}")
   print(f"Contact's email is {c1.getEmail()}")
   print(f"Stringified contact is {c1.__str__()}")

run()

        
