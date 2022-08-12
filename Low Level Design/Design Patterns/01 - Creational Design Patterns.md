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
        return Prime(member.age).deliveryDates(datetime(2022, 8, 12))
    else:
        return Regular(member.age).deliveryDates(datetime(2022, 8, 12))
        

checkDeliveryDate(member1)
checkDeliveryDate(member2)

```

Output
```
'Delivery Date is: 12 - 8 - 2022'
'Delivery Date is: 22 - 8 - 2022'
```

So, as we can see in the above example, we have created 2 subclasses of the the interface/Abstract class Membership along with the Regular and Prime Membership subclasses that have an abstract method of displaying the delivery dates of the orders placed, now based on their membership status the subclasses were called.

