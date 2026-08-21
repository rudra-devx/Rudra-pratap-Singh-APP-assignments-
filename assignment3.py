from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass



class CreditCard(Payment):

    def pay(self, amount):
        print("Paid", amount, "using Credit Card")


class PayPal(Payment):

    def pay(self, amount):
        print("Paid", amount, "using PayPal")



class Bitcoin(Payment):

    def pay(self, amount):
        print("Paid", amount, "using Bitcoin")

p1 = CreditCard()
p1.pay(1000)

p2 = PayPal()
p2.pay(2000)

p3 = Bitcoin()
p3.pay(3000)
