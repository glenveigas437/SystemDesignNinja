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

Prototype Pattern is good for when creating new objects that require a lot of resources than required. In prototype pattern you just create a copy of the object and store it in memory.

In Prototype Pattern, there is an interface that has a clone method and then multiple concrete classes have their independent clone methods.

Here is an example of prototype pattern.
In Amazon App there are many small applications, now instead of creating a new object of the concrete App classes, we make a copy of these applications and then access their content.

```
from abc import ABC, abstractmethod
import copy

class AmazonApp(ABC):
    def __init__(self):
        self.id = None
        self.type = None
    
    @abstractmethod
    def application(self):
        pass
    
    def getID(self):
        return self.id
    
    def getType(self):
        return self.type
    
    def setID(self, newId):
        self.id=newId
    
    def clone(self):
        return copy.copy(self)

class AmazonFresh(AmazonApp):
    def __init__(self):
        super().__init__()
        self.type='Grocery Shopping'
    
    def application(self):
        return f"This is a {self.type} App"
 
 class AmazonTV(AmazonApp):
    def __init__(self):
        super().__init__()
        self.type='Video Channel'
    
    def application(self):
        return f"This is a {self.type} app"

class AmazonPrime(AmazonApp):
    def __init__(self):
        super().__init__()
        self.type='OTT Platform'
    
    def application(self):
        return f"This is a {self.type} app"
        
class AmazonAppCache():
    
    cache={}
    
    @staticmethod
    def getApp(appId):
        App=AmazonAppCache.cache.get(appId, None)
        return App.clone()
    
    @staticmethod
    def load():
        fresh=AmazonFresh()
        fresh.setID(1)
        AmazonAppCache.cache[fresh.getID()]=fresh
    
        ATV=AmazonTV()
        ATV.setID(2)
        AmazonAppCache.cache[ATV.getID()]=ATV
        
        prime=AmazonPrime()
        prime.setID(3)
        AmazonAppCache.cache[prime.getID()]=prime
        
def startApp():
    AmazonAppCache().load()
    
    for key, value in AmazonAppCache().cache.items():
        print(key, ":", value)
    
    choice = int(input("Select App: "))
    if choice==1:
        fresh=AmazonAppCache.getApp(choice)
        print("Selected FRESH")
        print(fresh.application())
    
    elif choice==2:
        ATV=AmazonAppCache.getApp(choice)
        print("Selected TV")
        print(ATV.application())
    
    else:
        prime=AmazonAppCache.getApp(choice)
        print("Selected PRIME")
        print(prime.application())
 
startApp()
```

### OUTPUT

```
1 : <__main__.AmazonFresh object at 0x107827220>
2 : <__main__.AmazonTV object at 0x107827190>
3 : <__main__.AmazonPrime object at 0x1072b8040>

Select App: 3

Selected PRIME
This is an OTT Platform app

```

## 5 - Builder Pattern

he Builder Pattern is a creational pattern whose intent is to separate the construction of a complex object from its representation so that you can use the same construction process to create different representations.

The Builder Pattern tries to solve,

How can a class that includes creating a complex object be simplified?
How can a class create different representations of a complex object?
The Builder and Factory patterns are very similar in the fact they both instantiate new objects at runtime. The difference is when the process of creating the object is more complex, so rather than the Factory returning a new instance of ObjectA, it calls the builders director constructor method ObjectA.construct() that goes through a more complex construction process involving several steps. Both return an Object/Product.

The Key terminologies in this pattern are
1) Builder  - (interface, concrete builder)
2) Director - (The place where the concrete builder is called)
3) Client - (Invokes the director)
4) Product - (The product being built)

<ins>Builder Interface</ins>: The skeleton of the entire Application
<ins>Director</ins>: Inherits the Builder Interface
<ins>Client</ins>: Calls the director and builds the product

Here is an example with Amazon Prime Video

```
from abc import ABC, abstractmethod

#Interface
class MovieBuilderInterface(ABC):
    
    @abstractmethod
    def setMovieGenre(genre):
        pass
    
    @abstractmethod
    def setMovieDescription(desc):
        pass
    
    @abstractmethod
    def setMovieAgeLimit(ageLimit):
        pass
    
    @abstractmethod
    def setNumberOfActors(actors):
        pass
    
    @abstractmethod
    def getResult():
        pass
 
 #Product
 class Movie():
    def __init__(self, genre='Genre', desc='Desc', ageLimit=0, actors=0):
        self.genre = genre
        self.desc = desc
        self.ageLimit = ageLimit
        self.actors = actors
    
    def constructor(self):
        print(f"This is a movie of {self.genre} where {self.desc} and is only for audience above {self.ageLimit} years of age, also this movie has {self.actors} movie stars in it.")


#Builder
class MovieBuilder(MovieBuilderInterface):
    def __init__(self):
        self.movie = Movie()
    
    def setMovieGenre(self, genre):
        self.movie.genre = genre
        return self
    
    def setMovieDescription(self, desc):
        self.movie.desc = desc
        return self
        
    def setMovieAgeLimit(self, ageLimit):
        self.movie.ageLimit = ageLimit
        return self
    
    def setNumberOfActors(self, actors):
        self.movie.actors = actors
        return self
    
    def getResult(self):
        return self.movie
        
#Director
class Avengers:
    @staticmethod
    def construct():
        return MovieBuilder()\
                .setMovieGenre('Adventure')\
                .setMovieDescription('This is a superhero action Movie')\
                .setMovieAgeLimit(12)\
                .setNumberOfActors(8)\
                .getResult()

#Object
avengers=Avengers.construct()
avengers.constructor()

```

### OUTPUT

```
This is a movie of Adventure where This is a superhero action Movie and is only for audience above 12 years of age, also this movie has 8 movie stars in it.
```

In this example you can see that the end Product we are building is a Movie, to be specific the details of the movie
With ```MovieBuilderInterface``` describing the skeleton of the Movie and ```MovieBuilder``` loading the details of the movie and the Product ```Movie``` being called in.


## 6 - Strategy Pattern

the strategy pattern (also known as the policy pattern) is a behavioral software design pattern that enables selecting an algorithm at runtime. Instead of implementing a single algorithm directly, code receives run-time instructions as to which in a family of algorithms to use.[


For example
Consider a class Named Vehicle which has an abstract method named drive, now each type of vehicle - Bus, Truck, Car have their own implementation of drive methods, we observe that the the dirve nethod of Bus and Truck is the same, this problem doesn't promote the reusability of code.

To solve this problem we further divide the drive method based on their characteristics and define them as derived classes.

Below is an example of Amazon Shopping site displaying the discount of products.


```
from abc import ABC, abstractmethod



#Statergy
class DiscountStrategy(ABC):
    
    @abstractmethod
    def givenDiscount(self):
        pass

#Different Types of discount strategies
class FlatHalfDiscountStrategy(DiscountStrategy):
    
    def givenDiscount(self):
        return f"The Discount value is 50% of the given price"


class FlatQuarterDiscountStrategy(DiscountStrategy):
    
    def givenDiscount(self):
        return f"The Discount value is 25% of the given price"
        

class BigDiscountStrategy(DiscountStrategy):
    
    def givenDiscount(self):
        return f"The Discount value is 75% of the given price"




class Discount(ABC):
    
    def __init__(self, obj):
        self.obj = obj
    
    def discountConstruct(self):
        return self.obj.givenDiscount()




class FlatHalfDiscount(Discount):
    def __init__(self):
        super().__init__(FlatHalfDiscountStrategy())




class FlatQuarterDiscount(Discount):
    def __init__(self):
        super().__init__(FlatQuarterDiscountStrategy())



class FlatBigDiscount(Discount):
    def __init__(self):
        super().__init__(BigDiscountStrategy())



class Product(ABC):
    def __init__(self, productName, productDiscount):
        self.productName = productName
        self.productDiscount = productDiscount


class Phone(Product):
    def __init__(self):
        super().__init__('iPhone 13', FlatQuarterDiscount())


class Laptop(Product):
    def __init__(self):
        super().__init__('MacBook Pro', FlatHalfDiscount())


class Tablet(Product):
    def __init__(self):
        super().__init__('iPad Air',FlatBigDiscount())



class Main:
    def __init__(self, product):
        self.product = product()
    
    def getDiscountPrice(self):
        return f"{self.product.productName} - {self.product.productDiscount.discountConstruct()}"





phone=Main(Phone)
laptop=Main(Laptop)
tablet=Main(Tablet)



print(phone.getDiscountPrice())
print(laptop.getDiscountPrice())
print(tablet.getDiscountPrice())
```

### OUTPUT

```
iPhone 13 - The Discount value is 25% of the given price
MacBook Pro - The Discount value is 50% of the given price
iPad Air - The Discount value is 75% of the given price
```
