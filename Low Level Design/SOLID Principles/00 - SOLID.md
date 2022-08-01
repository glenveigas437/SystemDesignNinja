# Getting Started with S.O.L.I.D Principles


Have a look at this example,

```
class Order:
    items = []
    quantities = []
    prices = []
    payments = ['Debit Card', 'Credit Card', 'UPI', 'PayPal']
    status = "open"
    
    def addItem(self, item, quantity, price):
        self.items.append(item)
        self.quantities.append(quantity)
        self.prices.append(price)
    
    def totalPrice(self):
        total=0
        for currentItem in range(len(self.items)):
            total+= self.quantities[currentItem]*self.prices[currentItem]
        
        print(f"Your Total Bill is ${total}")
    
    def payOrder(self, paymentMethod, securityCode):
        time.sleep(10)
        print(f"{datetime.datetime.now().day} / {datetime.datetime.now().month} / {datetime.datetime.now().year} - {datetime.datetime.now().hour} : {datetime.datetime.now().minute} : {datetime.datetime.now().second}: Paying for your order via : {paymentMethod}")
        time.sleep(10)
        print(f"{datetime.datetime.now().day} / {datetime.datetime.now().month} / {datetime.datetime.now().year} - {datetime.datetime.now().hour} : {datetime.datetime.now().minute} : {datetime.datetime.now().second}: Verifiying your Security Code: {securityCode}")
        self.status = "Paid"
        if self.status == "Paid":
            print(f"{datetime.datetime.now().day} / {datetime.datetime.now().month} / {datetime.datetime.now().year} - {datetime.datetime.now().hour} : {datetime.datetime.now().minute} : {datetime.datetime.now().second}: SUCCESS!")
        if paymentMethod not in self.payments:
            raise Exception(f"Unsupported Payment Method - {paymentMethod}")

order1=Order()

order1.addItem('MacBook Pro M1 2022', 1, 1000)
order1.addItem('iPhone 13', 2, 1500)
order1.addItem('iPad Pro 2022', 1, 700)
order1.addItem('MacBook Air M2 2022', 1, 1200)

order1.totalPrice()

order1.payOrder('Debit Card', 437)

```

### Output                                                             
Your Total Bill is $5900                                            

1 / 8 / 2022 - 18 : 30 : 50: Paying for your order via : Debit Card 

1 / 8 / 2022 - 18 : 31 : 0: Verifiying your Security Code: 437      

1 / 8 / 2022 - 18 : 31 : 0: SUCCESS!                                


this piece of code replicates the functionality of an Online Shopping system like Amazon where there is a class named ```Order``` has 3 methods ```addItem```, ```totalPrice```, ```payOrder``` for adding items to the cart, calculating the total price and paying for the order respectively. but this violates certain coding principles we will discuss below


## 1) Single Responsibility Principle
Single Responsibility Principle states that every function/class should be performing a single action only, meaning that classes and functions should be highly coherent

Violation in the above code:
- The Class Order performs actions such as i) adding item to cart ii) calculating order price and iii) paying for the order, here the payment functionality should not be in the Order class rather a different class should be created for handling Payments.

here's how you can fix it

1) Create a separate class named Payment to handle payment processes

```
class Order:
    items = []
    quantities = []
    prices = []
    
    status = "open"
    
    def addItem(self, item, quantity, price):
        self.items.append(item)
        self.quantities.append(quantity)
        self.prices.append(price)
    
    def totalPrice(self):
        total=0
        for currentItem in range(len(self.items)):
            total+= self.quantities[currentItem]*self.prices[currentItem]
        
        print(f"Your Total Bill is ${total}")

```

```
class Payment:
    payments = ['Debit Card', 'Credit Card', 'UPI', 'PayPal']
    
    def payOrder(self, paymentMethod, securityCode):
        time.sleep(10)
        print(f"{datetime.datetime.now().day} / {datetime.datetime.now().month} / {datetime.datetime.now().year} - {datetime.datetime.now().hour} : {datetime.datetime.now().minute} : {datetime.datetime.now().second}: Paying for your order via : {paymentMethod}")
        time.sleep(10)
        print(f"{datetime.datetime.now().day} / {datetime.datetime.now().month} / {datetime.datetime.now().year} - {datetime.datetime.now().hour} : {datetime.datetime.now().minute} : {datetime.datetime.now().second}: Verifiying your Security Code: {securityCode}")
        self.status = "Paid"
        if self.status == "Paid":
            print(f"{datetime.datetime.now().day} / {datetime.datetime.now().month} / {datetime.datetime.now().year} - {datetime.datetime.now().hour} : {datetime.datetime.now().minute} : {datetime.datetime.now().second}: SUCCESS!")
        if paymentMethod not in self.payments:
            raise Exception(f"Unsupported Payment Method - {paymentMethod}")
```

```
order1=Order()

order1.addItem('MacBook Pro M1 2022', 1, 1000)
order1.addItem('iPhone 13', 2, 1500)
order1.addItem('iPad Pro 2022', 1, 700)
order1.addItem('MacBook Air M2 2022', 1, 1200)

order1.totalPrice()

Payment().payOrder('Debit Card', 437)

```

### Output                                                             
Your Total Bill is $5900                                            

1 / 8 / 2022 - 18 : 30 : 50: Paying for your order via : Debit Card 

1 / 8 / 2022 - 18 : 31 : 0: Verifiying your Security Code: 437      

1 / 8 / 2022 - 18 : 31 : 0: SUCCESS!  

So, in this manner if we have to include more payment methods we can just edit the ```Payment``` class and add more functionalities.
```Order``` now has only one functionality whereas ```Payment``` has another functionality this increased the cohesion but also introduced some coupling.

## 2) Open Close Principle
Open & Close display polarity in their literal meanings and so is this concept emulating something similar to their literal meanings. 
- Open: Open to extention of functionalities
- Close: Close to modification of existing functions

Now if I try to edit the class Payment I can add a few more if else conditions when I add new payment methods but this will violate the basic rule of Open Close Principle (i.e editing or modifying the current function/class)

Here is the fix to it
- Create a new interface (Abstract Class in Python) and then extend the interfaces with new Payment Method classes

Interface/Abstract Class
In Python we need to import ABC and abstractmethod from the library abc in order to implement interfaces

This is the interface
```
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self):
        pass
```

Different Payment Classes extending the PaymentMethod interface
```
class DebitCardPayment(PaymentMethod):
    def pay(self, order, secretKey):
        print("Paying via Debit Card")
        print(f"Authenticating {secretKey}")
        order.status = "Paid"

class CreditCardPayment(PaymentMethod):
    def pay(self, order, secretKey):
        print("Paying via Credit Card")
        print(f"Authenticating {secretKey}")
        order.status = "Paid"
        
class UPI(PaymentMethod):
    def pay(self, order, secretKey):
        print("Paying via UPI")
        print(f"Authenticating {secretKey}")
        order.status = "Paid"

class PayPal(PaymentMethod):
    def pay(self, order, secretKey):
        print("Paying via PayPal")
        print(f"Authenticating {secretKey}")
        order.status = "Paid"


PayPal().pay(order1,437)
```

### Output
Paying via PayPal
Authenticating 437

In this manner we are open to adding new payment methods like Cash On Delivery or Apple Pay, etc. but in the same manner we are not editing any of the pre-existing code.









