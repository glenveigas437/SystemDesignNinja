# 1 - Creational Design Patterns

Creational Design Patterns are responsible for efficient object creation mechanisms, which increase the flexibility and reusibility of existing code.

## 1 - Factory Pattern

- Factory Pattern is also called virtual constructor, to describe in simple terms Factory Patterns allow an interface or a class to create an object, but let the subclasses decide which class or object to instantiate. 
- Here, objects are created without exposing the logic to the client, and for creating the new type of object, the client uses the same common interface.

Example:
Amazon Shopping App.

Amazon has 2 types of membership with the premium member subscription (Amazon Prime) providing a lot of benefits like 1-Day/Same Day Delivery, discounts, access to amazing video content and also on-demand music streaming, while the regular members do not receive these perks.

So consider that before Amazon could come up with the concept of Prime, they just built one class for the Regular members but now with the inception of Amazon Prime it comes with its own benefits.

```
from abc import ABC, abstractmethod
from datetime import datetime

class Membership(ABC):
    @abstractmethod
    def deliveryDates(self, orderDate):
        pass

class Regular(Membership):
    def __init__(self, age):
        self.age = age
        
    def deliveryDates(self, orderDate):
        return f'Delivery Date is: {orderDate.day + (10%30)} - {orderDate.month} - {orderDate.year}'

class Prime(Membership):
    def __init__(self,age):
        self.age = age
        
    
    def getCost(self):
        if self.age<=24:
            return f'Subscription Price is: 499'
        else:
            return f'Subscription Price is: 999'
    
    def deliveryDates(self, orderDate):
        return f'Delivery Date is: {orderDate.day} - {orderDate.month} - {orderDate.year}'

class Member:
    def __init__(self, name, age, city, isPrime):
        self.name = name
        self.age = age
        self.city = city
        self.isPrime = isPrime

member1 = Member('Ronaldo', 37, 'Lisbon', True)
member2 = Member('Messi', 34, 'Rosario', False)

def checkDeliveryDate(member):
    if member.isPrime:
        primeMember=Prime(member.age)
        return primeMember.deliveryDates(datetime(2022, 8, 12)), primeMember.getCost()
    else:
        return Regular(member.age).deliveryDates(datetime(2022, 8, 12))
        

checkDeliveryDate(member1)
checkDeliveryDate(member2)

```

Output
```
('Delivery Date is: 12 - 8 - 2022', 'Subscription Price is: 999')

'Delivery Date is: 22 - 8 - 2022'
```

So, as we can see in the above example, we have created 2 subclasses of the the interface/Abstract class Membership along with the Regular and Prime Membership subclasses that have an abstract method of displaying the delivery dates of the orders placed, now based on their membership status the subclasses were called.


## 2 - Abstract Factory Pattern

Abstract Factory Pattern is combination or a set of multiple factory patterns, Now a factory pattern is created in the client side, but what if we want to create additional objects of new interfaces then we need to make changes in the client, what if there is a pattern where we don't have to mess with the client side, so we can add another layer of abstraction that can handle these changes.

in the example above we made use of an if-else condition to check for delivery dates of a prime and regular Amazon account user.
Now, let's look at the example below


```
from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def description(self):
        pass
        
class Shirt(Product):
    def description(self, brand, price):
        return f"This is a dress shirt by {brand} worth Rs. {price}"

class Trousers(Product):
    def description(self, brand, price):
        return f"This is a trouser by {brand} worth Rs. {price}"
 
class Kurti(Product):
    def description(self, brand, price):
        return f"This is a Floral Top by {brand} worth Rs. {price}"

class Leggings(Product):
    def description(self, brand, price):
        return f"This is a Legging by {brand} worth Rs. {price}"

class Factory(ABC):
    @abstractmethod
    def getOutfit(self):
        pass

class MensClothingFactory(Factory):
    def getOutfit(self, bill):
        if bill.typeOfOutfit=='Top':
            return Shirt().description(bill.brand, bill.price)
        if bill.typeOfOutfit=='Pant':
            return Trousers().description(bill.brand, bill.price)

class WomensClothingFactory(Factory):
    def getOutfit(self, bill):
        if bill.typeOfOutfit=='Top':
            return Kurti().description(bill.brand, bill.price)
        if bill.typeOfOutfit=='Pant':
            return Leggings().description(bill.brand, bill.price)
            
class Customer:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Bill:
    def __init__(self, brand, price, typeOfOutfit, customer):
        self.brand = brand
        self.price = price
        self.typeOfOutfit = typeOfOutfit
        self.customer = customer
 
c1 = Customer('Chris', 'Male')
c2 = Customer('Elsa', 'Female')

b1 = Bill('Van Heusen', 1000, 'Top', c1)
b2 = Bill('Gucci', 900, 'Top', c2)
b3 = Bill('Allen Solly', 800, 'Pant', c1)
b4 = Bill('Armani', 500, 'Pant', c2)

def getBills(bill):
    if bill.customer.gender=='Male':
        return MensClothingFactory().getOutfit(bill)
    else:
        return WomensClothingFactory().getOutfit(bill)

print(f"{getBills(b1)} \n {getBills(b3)}")
print(f"{getBills(b2)} \n {getBills(b4)}")
```

#### OUTPUT

```
This is a dress shirt by Van Heusen worth Rs. 1000 
This is a trouser by Allen Solly worth Rs. 800
This is a Floral Top by Gucci worth Rs. 900 
This is a Legging by Armani worth Rs. 500
```

In the example above, There is one interface for different types of clothes which is wrapped into one factory based on the dressing style, for e.g. if the customer is a man then it returns the factory of shirts and trousers, while dress and leggings are returned based on a woman's shopping preferences.

So we can infer that if there are multiple items under one category we can wrap those items in Factory.

## 3 - Singleton Pattern

A Singleton is an object with two main characteristics:

- It can have at most one instance
- It should have global accessibiility in the program
These properties are both important, although in practice you'll often hear people calling something a Singleton even if it has only one of these properties.

Having only one instance is usually a mechanism for controlling access to some shared resource. For example, two threads may work with the same file, so instead of both opening it separately, a Singleton can provide a unique access point to both of them.

Global accessibility is important because after your class has been instantiated once, you'd need to pass that single instance around in order to work with it. It can't be instantiated again. That's why it's easier to make sure that whenever you try to instantiate the class again, you just get the same instance you've already had.

Have a look at the example below,
Gaming companies these days restrict the installation of the software to multiple PCs, so let's try and implement something similar in this case.

There is a class named ```Game```, with it's instance set to None.
We create an obeject named ```user1``` as the sole user of the game, if another user is created then this Game won't be installed.

```
class Game:
   __instance__ = None

   def __init__(self):
       """ Constructor.
       """
       if Game.__instance__ is None:
           Game.__instance__ = self
       else:
           raise Exception("You cannot create another user to the play this game")

   @staticmethod
   def get_instance():
       """ Static method to fetch the current instance.
       """
       if not Game.__instance__:
           Game()
       return Game.__instance__

```

```
user1 = Game()
user1.getInstance()

#Creating another object leading to an Exception
user2 = Game()
```

### OUTPUT

```
#Object for user1
<__main__.Game at 0x10628cf10>

#for object user2
Exception: You cannot create another user to the play this game

```

## 4 - Prototype Pattern


