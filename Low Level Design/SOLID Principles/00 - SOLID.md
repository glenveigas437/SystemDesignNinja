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


## 3) Liskov Substitution Principle
What if 2 of the payment methods like Debit and Credit Card required security codes and PayPal required email address for authentication purpose, so we would now how to change the entire piece of code for every Payment Method child classes we have created, seems right? but No, this violates the Liskov Substitution Principle instead we need to create initializers for the authentication types we are creating.

Liskov Substitution Principle states that if we have objects in the program then we need to replace those objects with instances or sub-classes without altering the correctness of the program.

Now instead of providing ```securityKey``` while paying via PayPal we use email address for validation and to achieve this we make use of initializers

Here's the fix to it.

Removing the ```secretKey``` variable from each function as a parameter and initializing it for Debit, credit and UPI payment methods

```
class DebitCardPayment(PaymentMethod):
    def __init__(self, secretKey):
        self.secretKey = secretKey
    
    def pay(self, order):
        print("Paying via Debit Card")
        print(f"Authenticating {self.secretKey}")
        order.status = "Paid"
 
class CreditCardPayment(PaymentMethod):
    def __init__(self, secretKey):
        self.secretKey = secretKey
        
    def pay(self, order):
        print("Paying via Credit Card")
        print(f"Authenticating {self.secretKey}")
        order.status = "Paid"

class UPI(PaymentMethod):
    def __init__(self, secretKey):
        self.secretKey = secretKey
    
    def pay(self, order):
        print("Paying via UPI")
        print(f"Authenticating {self.secretKey}")
        order.status = "Paid"
        
class PayPal(PaymentMethod):
    def __init__(self, emailAddress):
        self.emailAddress = emailAddress
        
    def pay(self, order):
        print("Paying via PayPal")
        print(f"Authenticating {self.emailAddress}")
        order.status = "Paid"
        
order1=Order()
order2=Order()

order1.addItem('MacBook Pro M1 2022', 1, 1000)
order1.addItem('iPhone 13', 2, 1500)
order1.addItem('iPad Pro 2022', 1, 700)
order1.addItem('MacBook Air M2 2022', 1, 1200)

order2.addItem('Apple Watch Series 7', 1, 400)
order2.addItem('iPhone 13', 3, 1500)
order2.addItem('MacBook Pro M2 2022', 1, 1400)

order1.totalPrice()

PayPal('abc@gmail.com').pay(order1)

order2.totalPrice()
CreditCardPayment(437).pay(order2)

```


## OUTPUT
### Order1
Your Total Bill is $5900

Paying via PayPal

Authenticating abc@gmail.com

### Order2
Your Total Bill is $6300

Paying via Credit Card

Authenticating 437


## 4) Interface Segregation Principle

Interface Segregation Principle states that instead of having one general purpose interface we can multiple interfaces so the subclasses have more meaningful behaviour.

When you pay via Debit Card and PayPal you need to authenticate the payment via SMS but not via Credit Card.

So we now add another abstract method in our PaymentMode Interface in order to add another layer of authentication of SMS

```
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self):
        pass
    
    @abstractmethod
    def authenticateSMS(self):
        pass
```

So, now we add this in our sub classes as well

```
class DebitCardPayment(PaymentMethod):
    def __init__(self, secretKey):
        self.secretKey = secretKey
        self.verified = False
    
    def authenticateSMS(self):
        print("authenticated via SMS)
        self.verified = True
    
    def pay(self, order):
        print("Paying via Debit Card")
        print(f"Authenticating {self.secretKey}")
        order.status = "Paid"
 
class CreditCardPayment(PaymentMethod):
    def __init__(self, secretKey):
        self.secretKey = secretKey
    
    def authenticateSMS(self):
        raise Exception(f"No Authentication required via SMS")
    
    def pay(self, order):
        print("Paying via Credit Card")
        print(f"Authenticating {self.secretKey}")
        order.status = "Paid"

class UPI(PaymentMethod):
    def __init__(self, secretKey):
        self.secretKey = secretKey
    
    def authenticateSMS(self):
        raise Exception(f"No Authentication required via SMS")
        
    def pay(self, order):
        print("Paying via UPI")
        print(f"Authenticating {self.secretKey}")
        order.status = "Paid"
        
class PayPal(PaymentMethod):
    def __init__(self, emailAddress):
        self.emailAddress = emailAddress
        self.verified = True
    
    def authenticateSMS(self):
        print("authenticated via SMS)
        self.verified = True
        
    def pay(self, order):
        print("Paying via PayPal")
        print(f"Authenticating {self.emailAddress}")
        order.status = "Paid"

```

Adding another function does satisfy Interface Segregation Principle but violates Liskov Substitution Principle, now the general objective of following the S.O.L.I.D Principles is that while satisfying the need of one principle the other principles should not be compromised. So this solution above is not acceptbale, instead we can create another class and extend the PaymentMethod interface in order to add another layer of authentication of SMS verification.

```
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self):
        pass
```

```
class SMSAuthenticator(PaymentMethod)
    @abstractmethod
    def authenticateSMS(self):
        pass
```


```
class DebitCardPayment(SMSAuthenticator):
    def __init__(self, secretKey):
        self.secretKey = secretKey
        self.verified = False
    
    def authenticateSMS(self):
        print("authenticated via SMS)
        self.verified = True
    
    def pay(self, order):
        if not self.verified:
            raise Exception(f"Not verified")
        print("Paying via Debit Card")
        print(f"Authenticating {self.secretKey}")
        order.status = "Paid"
 
class CreditCardPayment(PaymentMethod):
    def __init__(self, secretKey):
        self.secretKey = secretKey
    
    def pay(self, order):
        print("Paying via Credit Card")
        print(f"Authenticating {self.secretKey}")
        order.status = "Paid"

class UPI(PaymentMethod):
    def __init__(self, secretKey):
        self.secretKey = secretKey
    
    def pay(self, order):
        print("Paying via UPI")
        print(f"Authenticating {self.secretKey}")
        order.status = "Paid"
        
class PayPal(SMSAuthenticator):
    def __init__(self, emailAddress):
        self.emailAddress = emailAddress
        self.verified = True
    
    def authenticateSMS(self):
        print("authenticated via SMS)
        self.verified = True
        
    def pay(self, order):
        print("Paying via PayPal")
        print(f"Authenticating {self.emailAddress}")
        order.status = "Paid"


order1=Order()

order1.addItem('MacBook Pro M1 2022', 1, 1000)
order1.addItem('iPhone 13', 2, 1500)
order1.addItem('iPad Pro 2022', 1, 700)
order1.addItem('MacBook Air M2 2022', 1, 1200)


order1.totalPrice()

pp1=PayPal('abc@gmail.com')
pp1.authenticateSMS()
pp1.pay(order1)
```

### OUTPUT

Your Total Bill is $5900

Authenticating via SMS!

Paying via PayPal

Authenticating abc@gmail.com

Instead of applying this solution with classes and sub-classes we can make use of compositions which is usefull and better for this solution.

we create a separate class named ```SMSAuth``` that handles authentication
this class has 2 methods 1) to verify the code 2) to check authorization

```
class SMSAuth:
    authorized = False
    
    def verifyCode(self, code):
        print(f"{code} has been verified")
        self.authorized = True
     
    def isAuthorized(self):
        return self.authorized
```
```
class DebitCardPayment(SMSAuthenticator):

    def __init__(self, secretKey, authorizer):
        self.authorizer = authorizzer
        self.secretKey = secretKey
    
    def authenticateSMS(self):
        print("authenticated via SMS)
        self.verified = True
    
    def pay(self, order):
        if not authorizer.isAuthorized:
            raise Exception(f"Not verified")
        print("Paying via Debit Card")
        print(f"Authenticating {self.secretKey}")
        order.status = "Paid"


order1=Order()

order1.addItem('MacBook Pro M1 2022', 1, 1000)
order1.addItem('iPhone 13', 2, 1500)
order1.addItem('iPad Pro 2022', 1, 700)
order1.addItem('MacBook Air M2 2022', 1, 1200)


order1.totalPrice()

authorizer=SMSAuth
dbc=DebitCardPayment(437, authorizer)
authorizer.verifyCode(437)
dbc.pay(order1)
```



## 5) Dependancy Inversion Principle

Dependency Inversion means that the code should be dependant on abstractions not on any subclasses. The solution above violates this principle.

In this example, we will create another class named ```Authorizer``` that will be extended in the  ```SMSAuth``` class

```
class Authorizer
    @abstractmethod
    def isAuthorized(self):
        pass
```

```
class SMSAuth(Authorizer):
    authorized = False
    
    def verifyCode(self, code):
        print(f"{code} has been verified")
        self.authorized = True
     
    def isAuthorized(self):
        return self.authorized
```
```
class DebitCardPayment(SMSAuthenticator):

    def __init__(self, secretKey, authorizer):
        self.authorizer = authorizzer
        self.secretKey = secretKey
    
    def authenticateSMS(self):
        print("authenticated via SMS)
        self.verified = True
    
    def pay(self, order):
        if not authorizer.isAuthorized:
            raise Exception(f"Not verified")
        print("Paying via Debit Card")
        print(f"Authenticating {self.secretKey}")
        order.status = "Paid"


order1=Order()

order1.addItem('MacBook Pro M1 2022', 1, 1000)
order1.addItem('iPhone 13', 2, 1500)
order1.addItem('iPad Pro 2022', 1, 700)
order1.addItem('MacBook Air M2 2022', 1, 1200)


order1.totalPrice()

authorizer=SMSAuth
dbc=DebitCardPayment(437, authorizer)
authorizer.verifyCode(437)
dbc.pay(order1)
```

The output for Principle 4 and 5 remain the same
So, now if we add another Authorizer we can extend the Authorizer class and not create a new Authorization class.


## Conclusion
That's all for S.O.L.I.D Principles, these principles are very essential in order to write clean, comprehensive code and as we keep writing code we don't have to remember these principles rather we can just integrate them on the go.




