1 - Creational Design Patterns
Creational Design Patterns are responsible for efficient object creation mechanisms, which increase the flexibility and reusibility of existing code.

1 - Factory Pattern
Definition**:** The Factory Pattern offers a method to create objects without requiring the direct instantiation of their specific classes. Rather than calling a class constructor directly, the responsibility for object creation is given to a factory method that decides which class to instantiate based on given criteria.

Purpose**:** This pattern supports loose coupling by allowing code to depend on an interface or an abstract class instead of particular concrete classes. It provides flexibility and extensibility in creating new objects without needing to alter existing code, making the system easier to scale and modify.

Real-world Analogy: Think of ordering a coffee at a café. You don’t specify if a barista or a machine should make it—you just ask for the coffee. The café (acting as the factory) determines the best way to fulfill your request based on current conditions, like staff availability.

Example: In the context of a food delivery app, the Factory Pattern can be used to create instances of different types of FoodItem classes based on user orders. This pattern helps manage the creation of various food item objects, such as Pizza, Burger, or Pasta, without requiring the client code to know the specific classes that are being instantiated.

The Factory Pattern consists of several key components that work together to create objects in a flexible and decoupled way. Here are the primary components:

Product Interface (or Abstract Product): This defines the common interface or abstract class that all concrete products should implement. It provides a template for the behavior and properties expected in each product. In the food delivery example above, this would be the FoodItem abstract class, which includes the methods prepare() and package().

Concrete Products: These are the specific implementations of the Product Interface. Each concrete product class provides its unique implementation of the methods defined by the Product Interface. In the example, Pizza, Burger, and Pasta are the concrete products that implement the FoodItem interface.

Factory: This is the class responsible for creating instances of the concrete products based on the given parameters. The Factory encapsulates the object creation logic, allowing the client to request objects without needing to know which concrete class is being instantiated. In the example, the FoodFactory class is the factory that creates and returns instances of Pizza, Burger, or Pasta based on the input.

Client Code: The client code interacts with the factory to obtain instances of the Product Interface. The client does not need to know about the concrete classes or how the objects are created; it only interacts with the factory and the Product Interface. In the example, the order_food function represents the client code that uses the factory to get instances of FoodItem.

from abc import ABC, abstractmethod

# Step 1: Define the Abstract Product
class FoodItem(ABC):
    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def package(self):
        pass


# Step 2: Create Concrete Products
class Pizza(FoodItem):
    def prepare(self):
        return "Preparing a delicious Pizza."

    def package(self):
        return "Packaging the Pizza in a pizza box."


class Burger(FoodItem):
    def prepare(self):
        return "Grilling the Burger patty."

    def package(self):
        return "Packaging the Burger in a wrapper."


class Pasta(FoodItem):
    def prepare(self):
        return "Boiling pasta and preparing sauce."

    def package(self):
        return "Packaging the Pasta in a container."


# Step 3: Create the Factory
class FoodFactory:
    @staticmethod
    def create_food_item(food_type):
        if food_type == "Pizza":
            return Pizza()
        elif food_type == "Burger":
            return Burger()
        elif food_type == "Pasta":
            return Pasta()
        else:
            raise ValueError(f"Unknown food type: {food_type}")


# Client Code
def order_food(food_type):
    food_item = FoodFactory.create_food_item(food_type)
    print(food_item.prepare())
    print(food_item.package())


# Testing the Factory Pattern in a food delivery context
order_food("Pizza")
order_food("Burger")
order_food("Pasta")

Output

Preparing a delicious Pizza.
Packaging the Pizza in a pizza box.

Grilling the Burger patty.
Packaging the Burger in a wrapper.

Boiling pasta and preparing sauce.
Packaging the Pasta in a container.
So, as we can see in the above example, we have created 2 subclasses of the the interface/Abstract class Membership along with the Regular and Prime Membership subclasses that have an abstract method of displaying the delivery dates of the orders placed, now based on their membership status the subclasses were called.

2 - Abstract Factory Pattern
Definition The Abstract Factory Pattern is a creational design pattern that provides an interface for creating families of related or dependent objects without specifying their concrete classes. It allows clients to create multiple objects that belong to a specific "family" of objects and ensures that only compatible products are created together.

Components

Abstract Factory Interface: Declares methods for creating each type of product in the family.
Concrete Factories: Implement the abstract factory interface to create specific types of related products.
Abstract Product Interfaces: Define the interfaces for each type of product that the factory produces. Each family of products has a separate interface.
Concrete Products: These are the actual implementations of the product interfaces, created by concrete factories. They belong to a specific product family.
Client Code: Uses the abstract factory interface to interact with the factory and create products, without needing to know the specific concrete classes.
Purpose The Abstract Factory Pattern is useful for creating families of related objects, such as a group of UI components or different types of food items, that must work together in a system. It promotes consistency by ensuring that only compatible objects are created together, making it easier to swap entire families of objects while keeping the system consistent and decoupled from concrete implementations.

Real World Analogy Imagine a restaurant that serves different cuisines, like Italian and Mexican. Each cuisine has a specific set of dishes—an Italian set with pizza and pasta, and a Mexican set with tacos and burritos. The restaurant manager (Abstract Factory) can request either the Italian or Mexican kitchen (Concrete Factories) to prepare an entire set of dishes. Each kitchen (Concrete Factory) knows how to create its own related dishes (Concrete Products) that fit well together.

Example In a food delivery app, the Abstract Factory Pattern could be used to manage different types of meal categories. For example, you might have VeganMealFactory and NonVeganMealFactory for different dietary preferences. Each factory would produce products like MainCourse, SideDish, and Dessert specific to the dietary preference.

Here's how this would look in code:

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
OUTPUT
Vegan Meal:
Preparing vegan tofu stir-fry.
Preparing vegan salad.

Non-Vegan Meal:
Preparing grilled chicken.
Preparing fries.
3 - Singleton Pattern
Definition The Singleton Pattern is a creational design pattern that ensures a class has only one instance, while providing a global point of access to that instance. This pattern restricts the instantiation of a class to a single object, making it ideal for resources that should be shared throughout an application.

Components

Singleton Class: The class that implements the Singleton Pattern by controlling its instantiation and ensuring that only one instance exists.
Private Constructor: The constructor is often made private (or controlled) to prevent direct instantiation outside the class.
Static Instance Variable: Holds the single instance of the class.
Public Access Method: A method (often get_instance) that provides access to the instance, creating it if it doesn’t already exist.
Purpose The purpose of the Singleton Pattern is to control access to a resource that should have only one instance within a system. Examples include database connections, configuration settings, and logging services. By ensuring only one instance exists, the pattern promotes resource sharing and reduces unnecessary overhead.

Real World Analogy Consider a food delivery app where all orders go through a single OrderManager service that coordinates the assignment of orders to delivery personnel. Regardless of how many users are using the app, there is only one OrderManager to ensure that orders are processed and assigned in a consistent, centralized way.

Example In a food delivery app, a DatabaseConnection could be implemented as a Singleton to ensure that all parts of the app use the same database connection instance, preventing issues with multiple connections and improving resource management.

Here’s how it could look in code:

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
OUTPUT
Executing 'SELECT * FROM Orders' on the single database instance.
Executing 'SELECT * FROM Customers' on the single database instance.
Same instance: True

4 - Prototype Pattern
Definition The Prototype Pattern is a creational design pattern that enables the creation of new objects by copying or cloning an existing object, called the prototype. This approach allows for efficient creation of objects when direct instantiation is costly or complicated.

Components

Prototype Interface: Defines a method for cloning objects. This is often a clone or copy method.
Concrete Prototype: Implements the prototype interface and defines how to create a copy of itself.
Client Code: Uses the prototype to create new objects by cloning existing ones instead of instantiating new objects directly.
Purpose The Prototype Pattern is particularly useful when creating an object is resource-intensive or when there are numerous configurations of an object. Cloning provides a quick way to replicate objects with similar properties while allowing further modifications as needed, without creating each one from scratch.

Real World Analogy Consider a food delivery app that allows users to save custom orders as "templates." When a user wants to reorder, they can simply clone their saved template, customize it (e.g., add extra toppings), and place the order. The saved template acts as a prototype for the new customized order.

Example In a food delivery app, suppose we have a class representing a FoodOrder that has details about the items in an order, customer preferences, and delivery instructions. Using the Prototype Pattern, the app can create new orders by cloning an existing FoodOrder object, which can then be modified before submission.

Here's a code example:

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
OUTPUT
Original Order:
Items: ['Pizza', 'Salad']
Notes: Extra cheese on pizza
Delivery Address: 123 Food Street

Cloned Order with Modifications:
Items: ['Pizza', 'Salad']
Notes: No cheese on pizza
Delivery Address: 456 Main Avenue
5 - Builder Pattern
Definition The Builder Pattern is a creational design pattern that allows the construction of complex objects step by step. This pattern separates the construction of an object from its representation, enabling the same construction process to create different representations or configurations of the object.

Components

Builder Interface: Declares the steps required to build the product. These steps are often defined as separate methods for configuring different aspects of the product.
Concrete Builder: Implements the Builder interface, providing specific implementations for each building step. This class is responsible for assembling the product.
Product: The complex object that is being built. The builder gradually assembles it.
Director: (Optional) Orchestrates the building steps in a particular sequence, guiding the builder to construct a specific product configuration.
Client Code: Initiates the building process by interacting with the Director or directly with the Builder to create the product.
Purpose The Builder Pattern is useful for constructing complex objects that require multiple configuration steps, especially when the object needs to be built in different ways. This pattern provides a clear, controlled, and flexible way to assemble parts of an object step-by-step, ensuring the final product is consistent and meets specific criteria.

Real World Analogy In a food delivery app, think of building a customized meal. A MealBuilder allows users to choose different components, such as a main dish, side, and drink, to create a meal that suits their preferences. This pattern lets the app construct different types of meals (e.g., vegan, non-vegan) using the same interface and structure.

Example In a food delivery app, a user might want to customize a meal by selecting specific items, sides, and drinks. The Builder Pattern could help structure this process, allowing the creation of various meal configurations.

Here’s how it could look in code:

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
OUTPUT
Vegan Meal:
Main Course: Vegan Burger
Side: Salad
Drink: Smoothie

Non-Vegan Meal:
Main Course: Chicken Burger
Side: Fries
Drink: Soda

