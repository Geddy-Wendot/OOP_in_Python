from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def authorize_payment(self, amount):
        pass

    @abstractmethod
    def make_payment(self,amount):
        pass

class CreditCardPayment(PaymentMethod):
    def __init__(self, amount):
        super().__init__()
        self.amount = amount

    def authorize_payment(self, amount):
        print(f"Authorizing payment of {amount} from your card...")
        print("Authorization complete")

    def make_payment(self, amount):
        # ensure authorization and then process the payment
        self.authorize_payment(amount)
        print(f"Processing card payment of {amount}... Done")

class PaypalPayment(PaymentMethod):
    def __init__(self, amount):
        super().__init__()
        self.amount=amount

    def authorize_payment(self, amount):
        print(f"Authorizing {amount} from your paypal account")
        print("Authorization complete.")

    def make_payment(self, amount):
        self.authorize_payment(amount)
        print("Payment successfull")

class CryptoPayment(PaymentMethod):
    def __init__(self, amount):
        super().__init__()
        self.amount=amount

    def authorize_payment(self, amount):
        print(f"Authorizing tranfer of {amount} in crypto from your wallet")
        print("Transfer authorized")

    def make_payment(self, amount):
        self.authorize_payment(amount)
        print(f"Processing crypto payment of {amount} coins... Done")

payment = [CreditCardPayment(1000), PaypalPayment(4000), CryptoPayment(40)]

for p in payment:
    print(f"{p.__class__.__name__}:")
    p.make_payment(p.amount)