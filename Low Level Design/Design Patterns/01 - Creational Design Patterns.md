# 1 - Creational Design Patterns

Creational Design Patterns are responsible for efficient object creation mechanisms, which increase the flexibility and reusibility of existing code.

##  🚀 Factory Method Pattern

**Definition:**
The Factory Pattern offers a method to create objects without requiring the direct instantiation of their specific classes. Rather than calling a class constructor directly, the responsibility for object creation is given to a factory method that decides which class to instantiate based on given criteria.

**Purpose:**
This pattern supports loose coupling by allowing code to depend on an interface or an abstract class instead of particular concrete classes. It provides flexibility and extensibility in creating new objects without needing to alter existing code, making the system easier to scale and modify.

**Real-world Analogy:**
Think of ordering a coffee at a café. You don’t specify if a barista or a machine should make it—you just ask for the coffee. The café (acting as the factory) determines the best way to fulfill your request based on current conditions, like staff availability.

**🛠️ Components of Factory Method Pattern**

**1️⃣ Product (Interface/Abstract Class)** → Defines the object structure.

**2️⃣ Concrete Products (Subclasses)** → Implements different versions of the product.

**3️⃣ Creator (Factory Class)** → Declares the create_product() method.

**4️⃣ Concrete Creator (Subclasses of Factory)** → Implements create_product() to return specific objects.

**🚀 Example: Music Player Factory**
🔹 We have different music players (Spotify, Apple Music).
🔹 The MusicPlayerFactory creates the right player without modifying client code.

```
from abc import ABC, abstractmethod

# 1️⃣ Product (Interface)
class MusicPlayer(ABC):
    @abstractmethod
    def play_song(self, song):
        pass

# 2️⃣ Concrete Products
class SpotifyPlayer(MusicPlayer):
    def play_song(self, song):
        return f"Playing '{song}' on Spotify 🎵"

class AppleMusicPlayer(MusicPlayer):
    def play_song(self, song):
        return f"Playing '{song}' on Apple Music 🍏"

# 3️⃣ Creator (Factory)
class MusicPlayerFactory:
    @staticmethod
    def get_player(player_type):
        if player_type == "spotify":
            return SpotifyPlayer()
        elif player_type == "apple":
            return AppleMusicPlayer()
        else:
            raise ValueError("Unknown Music Player")

# --- Usage ---
player = MusicPlayerFactory.get_player("spotify")
print(player.play_song("Shape of You"))  # ✅ "Playing 'Shape of You' on Spotify 🎵"

player2 = MusicPlayerFactory.get_player("apple")
print(player2.play_song("Blinding Lights"))  # ✅ "Playing 'Blinding Lights' on Apple Music 🍏"
```

**🔥 Benefits of Factory Method**
✅ **Encapsulation** → Hides object creation logic.
✅ **Scalability** → Easily add new players (YouTube Music, SoundCloud) without modifying factory code.
✅ **Flexibility** → Client code doesn’t depend on specific implementations.

🧐 **Real-World Usage of Factory**
✔ **Database Connection Factory** – Returns MySQL, PostgreSQL, or SQLite connection.
✔ **Notification Factory** – Returns Email, SMS, or Push Notification sender.
✔ **Payment Gateway Factory** – Returns Stripe, PayPal, or Razorpay integration.


## 2 - Abstract Factory Pattern

**Definition**
The Abstract Factory Pattern is a creational design pattern that provides an interface for creating families of related or dependent objects without specifying their concrete classes. It allows clients to create multiple objects that belong to a specific "family" of objects and ensures that only compatible products are created together.

**Components**
- **Abstract Factory Interface:** Declares methods for creating each type of product in the family.
- **Concrete Factories:** Implement the abstract factory interface to create specific types of related products.
- **Abstract Product Interfaces:** Define the interfaces for each type of product that the factory produces. Each family of products has a separate interface.
- **Concrete Products:** These are the actual implementations of the product interfaces, created by concrete factories. They belong to a specific product family.
- **Client Code:** Uses the abstract factory interface to interact with the factory and create products, without needing to know the specific concrete classes.

**Purpose**
The Abstract Factory Pattern is useful for creating families of related objects, such as a group of UI components or different types of food items, that must work together in a system. It promotes consistency by ensuring that only compatible objects are created together, making it easier to swap entire families of objects while keeping the system consistent and decoupled from concrete implementations.

**Real World Analogy**
Imagine a restaurant that serves different cuisines, like Italian and Mexican. Each cuisine has a specific set of dishes—an Italian set with pizza and pasta, and a Mexican set with tacos and burritos. The restaurant manager (Abstract Factory) can request either the Italian or Mexican kitchen (Concrete Factories) to prepare an entire set of dishes. Each kitchen (Concrete Factory) knows how to create its own related dishes (Concrete Products) that fit well together.

**Example** 
In a food delivery app, the Abstract Factory Pattern could be used to manage different types of meal categories. For example, you might have VeganMealFactory and NonVeganMealFactory for different dietary preferences. Each factory would produce products like MainCourse, SideDish, and Dessert specific to the dietary preference.

Here's how this would look in code:

```
from abc import ABC, abstractmethod

# Abstract Products
class MainCourse(ABC):
    @abstractmethod
    def prepare(self):
        pass

class SideDish(ABC):
    @abstractmethod
    def prepare(self):
        pass

# Concrete Products for Vegan
class VeganMainCourse(MainCourse):
    def prepare(self):
        return "Preparing vegan tofu stir-fry."

class VeganSideDish(SideDish):
    def prepare(self):
        return "Preparing vegan salad."

# Concrete Products for Non-Vegan
class NonVeganMainCourse(MainCourse):
    def prepare(self):
        return "Preparing grilled chicken."

class NonVeganSideDish(SideDish):
    def prepare(self):
        return "Preparing fries."

# Abstract Factory
class MealFactory(ABC):
    @abstractmethod
    def create_main_course(self):
        pass

    @abstractmethod
    def create_side_dish(self):
        pass

# Concrete Factories
class VeganMealFactory(MealFactory):
    def create_main_course(self):
        return VeganMainCourse()

    def create_side_dish(self):
        return VeganSideDish()

class NonVeganMealFactory(MealFactory):
    def create_main_course(self):
        return NonVeganMainCourse()

    def create_side_dish(self):
        return NonVeganSideDish()

# Client Code
def order_meal(factory: MealFactory):
    main_course = factory.create_main_course()
    side_dish = factory.create_side_dish()
    print(main_course.prepare())
    print(side_dish.prepare())

# Ordering different types of meals
print("Vegan Meal:")
order_meal(VeganMealFactory())

print("\nNon-Vegan Meal:")
order_meal(NonVeganMealFactory())
```

#### OUTPUT

```
Vegan Meal:
Preparing vegan tofu stir-fry.
Preparing vegan salad.

Non-Vegan Meal:
Preparing grilled chicken.
Preparing fries.
```


## 3 - Singleton Pattern

**Definition**
The Singleton Pattern is a creational design pattern that ensures a class has only one instance, while providing a global point of access to that instance. This pattern restricts the instantiation of a class to a single object, making it ideal for resources that should be shared throughout an application.

**Components**
- **Singleton Class:** The class that implements the Singleton Pattern by controlling its instantiation and ensuring that only one instance exists.
- **Private Constructor:** The constructor is often made private (or controlled) to prevent direct instantiation outside the class.
- **Static Instance Variable:** Holds the single instance of the class.
- **Public Access Method:** A method (often get_instance) that provides access to the instance, creating it if it doesn’t already exist.

**Purpose**
The purpose of the Singleton Pattern is to control access to a resource that should have only one instance within a system. Examples include database connections, configuration settings, and logging services. By ensuring only one instance exists, the pattern promotes resource sharing and reduces unnecessary overhead.

**Real World Analogy**
Consider a food delivery app where all orders go through a single OrderManager service that coordinates the assignment of orders to delivery personnel. Regardless of how many users are using the app, there is only one OrderManager to ensure that orders are processed and assigned in a consistent, centralized way.

**Example**
In a food delivery app, a DatabaseConnection could be implemented as a Singleton to ensure that all parts of the app use the same database connection instance, preventing issues with multiple connections and improving resource management.

Here’s how it could look in code:
```
class DatabaseConnection:
    _instance = None  # Static instance variable

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection = cls._create_connection()
        return cls._instance

    @staticmethod
    def _create_connection():
        # Simulate creating a database connection
        return "Database connection established"

    def query(self, sql):
        return f"Executing '{sql}' on the single database instance."

# Client Code
def main():
    # Getting the single instance
    db1 = DatabaseConnection()
    print(db1.query("SELECT * FROM Orders"))

    # Trying to get another instance
    db2 = DatabaseConnection()
    print(db2.query("SELECT * FROM Customers"))

    # Verifying that db1 and db2 are the same instance
    print("Same instance:", db1 is db2)

main()
```

### OUTPUT

```
Executing 'SELECT * FROM Orders' on the single database instance.
Executing 'SELECT * FROM Customers' on the single database instance.
Same instance: True

```

## 4 - Prototype Pattern

**Definition**
The Prototype Pattern is a creational design pattern that enables the creation of new objects by copying or cloning an existing object, called the prototype. This approach allows for efficient creation of objects when direct instantiation is costly or complicated.

**Components**
- **Prototype Interface:** Defines a method for cloning objects. This is often a clone or copy method.
- **Concrete Prototype:** Implements the prototype interface and defines how to create a copy of itself.
- **Client Code:** Uses the prototype to create new objects by cloning existing ones instead of instantiating new objects directly.

**Purpose**
The Prototype Pattern is particularly useful when creating an object is resource-intensive or when there are numerous configurations of an object. Cloning provides a quick way to replicate objects with similar properties while allowing further modifications as needed, without creating each one from scratch.

**Real World Analogy**
Consider a food delivery app that allows users to save custom orders as "templates." When a user wants to reorder, they can simply clone their saved template, customize it (e.g., add extra toppings), and place the order. The saved template acts as a prototype for the new customized order.

**Example**
In a food delivery app, suppose we have a class representing a FoodOrder that has details about the items in an order, customer preferences, and delivery instructions. Using the Prototype Pattern, the app can create new orders by cloning an existing FoodOrder object, which can then be modified before submission.

Here's a code example:

```
import copy

# Prototype Interface
class FoodOrderPrototype:
    def clone(self):
        return copy.deepcopy(self)

# Concrete Prototype
class FoodOrder(FoodOrderPrototype):
    def __init__(self, items, customer_notes, delivery_address):
        self.items = items  # List of items in the order
        self.customer_notes = customer_notes
        self.delivery_address = delivery_address

    def __str__(self):
        return (f"Items: {self.items}\n"
                f"Notes: {self.customer_notes}\n"
                f"Delivery Address: {self.delivery_address}\n")

# Client Code
def main():
    # Original order template
    original_order = FoodOrder(
        items=["Pizza", "Salad"],
        customer_notes="Extra cheese on pizza",
        delivery_address="123 Food Street"
    )
    print("Original Order:")
    print(original_order)

    # Cloning the order for a new customer with slight changes
    cloned_order = original_order.clone()
    cloned_order.customer_notes = "No cheese on pizza"
    cloned_order.delivery_address = "456 Main Avenue"

    print("Cloned Order with Modifications:")
    print(cloned_order)

main()
```

### OUTPUT

```
Original Order:
Items: ['Pizza', 'Salad']
Notes: Extra cheese on pizza
Delivery Address: 123 Food Street

Cloned Order with Modifications:
Items: ['Pizza', 'Salad']
Notes: No cheese on pizza
Delivery Address: 456 Main Avenue
```

## 5 - Builder Pattern

**Definition**
The Builder Pattern is a creational design pattern that allows the construction of complex objects step by step. This pattern separates the construction of an object from its representation, enabling the same construction process to create different representations or configurations of the object.

**Components**
- **Builder Interface:** Declares the steps required to build the product. These steps are often defined as separate methods for configuring different aspects of the product.
- **Concrete Builder:** Implements the Builder interface, providing specific implementations for each building step. This class is responsible for assembling the product.
- **Product:** The complex object that is being built. The builder gradually assembles it.
- **Director:** (Optional) Orchestrates the building steps in a particular sequence, guiding the builder to construct a specific product configuration.
- **Client Code:** Initiates the building process by interacting with the Director or directly with the Builder to create the product.

**Purpose**
The Builder Pattern is useful for constructing complex objects that require multiple configuration steps, especially when the object needs to be built in different ways. This pattern provides a clear, controlled, and flexible way to assemble parts of an object step-by-step, ensuring the final product is consistent and meets specific criteria.

**Real World Analogy**
In a food delivery app, think of building a customized meal. A MealBuilder allows users to choose different components, such as a main dish, side, and drink, to create a meal that suits their preferences. This pattern lets the app construct different types of meals (e.g., vegan, non-vegan) using the same interface and structure.

**Example**
In a food delivery app, a user might want to customize a meal by selecting specific items, sides, and drinks. The Builder Pattern could help structure this process, allowing the creation of various meal configurations.

Here’s how it could look in code:
```
# Product
class Meal:
    def __init__(self):
        self.main_course = None
        self.side = None
        self.drink = None

    def __str__(self):
        return (f"Main Course: {self.main_course}\n"
                f"Side: {self.side}\n"
                f"Drink: {self.drink}\n")


# Builder Interface
class MealBuilder:
    def add_main_course(self, main_course):
        raise NotImplementedError

    def add_side(self, side):
        raise NotImplementedError

    def add_drink(self, drink):
        raise NotImplementedError

    def get_meal(self):
        raise NotImplementedError


# Concrete Builder
class VeganMealBuilder(MealBuilder):
    def __init__(self):
        self.meal = Meal()

    def add_main_course(self, main_course="Vegan Burger"):
        self.meal.main_course = main_course
        return self

    def add_side(self, side="Salad"):
        self.meal.side = side
        return self

    def add_drink(self, drink="Smoothie"):
        self.meal.drink = drink
        return self

    def get_meal(self):
        return self.meal


class NonVeganMealBuilder(MealBuilder):
    def __init__(self):
        self.meal = Meal()

    def add_main_course(self, main_course="Chicken Burger"):
        self.meal.main_course = main_course
        return self

    def add_side(self, side="Fries"):
        self.meal.side = side
        return self

    def add_drink(self, drink="Soda"):
        self.meal.drink = drink
        return self

    def get_meal(self):
        return self.meal


# Director (Optional)
class MealDirector:
    def __init__(self, builder):
        self.builder = builder

    def create_meal(self):
        return (self.builder
                .add_main_course()
                .add_side()
                .add_drink()
                .get_meal())


# Client Code
def main():
    # Vegan meal
    vegan_builder = VeganMealBuilder()
    director = MealDirector(vegan_builder)
    vegan_meal = director.create_meal()
    print("Vegan Meal:")
    print(vegan_meal)

    # Non-Vegan meal
    non_vegan_builder = NonVeganMealBuilder()
    director = MealDirector(non_vegan_builder)
    non_vegan_meal = director.create_meal()
    print("\nNon-Vegan Meal:")
    print(non_vegan_meal)


main()
```

### OUTPUT

```
Vegan Meal:
Main Course: Vegan Burger
Side: Salad
Drink: Smoothie

Non-Vegan Meal:
Main Course: Chicken Burger
Side: Fries
Drink: Soda
```
