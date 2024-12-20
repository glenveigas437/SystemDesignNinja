# Getting Started with [S](#1-single-responsibility-principle).[O](#2-open-close-principle).[L](#3-liskov-substitution-principle).[I](#4-interface-segregation-principle).[D](#5-dependancy-inversion-principle) Principles


Have a look at this example,

```
class OnlineStore:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def checkout(self, payment_method, customer):
        # Process payment
        if payment_method == "credit_card":
            print(f"Processing credit card payment for {customer}")
        elif payment_method == "cash":
            print(f"Processing cash payment for {customer}")
        
        # Send notification
        if "@" in customer:
            print(f"Sending email notification to {customer}")
        else:
            print(f"Sending SMS notification to {customer}")

        # Update inventory
        for item in self.items:
            print(f"Updating inventory for {item}")

# Usage:
store = OnlineStore()
store.add_item("Laptop")
store.checkout("credit_card", "customer@example.com")
```

### Output
```
Processing credit card payment for customer@example.com
Sending email notification to customer@example.com
Updating inventory for Laptop                               
```

This design violates several key principles that make it hard to maintain, scale, and adapt over time. The SOLID principles are a set of five guidelines to help you design software that is flexible, maintainable, and scalable. Each letter stands for a different principle, and together they help you create clean and robust code. Here’s an easy explanation of each principle and we'll be fixing the code for each violation that occurs.

## 1) Single Responsibility Principle
**Definition**: A class should have only one reason to change, meaning it should only have one job or responsibility.

**In simple terms:** Each class should do one thing and do it well.

**Violation in the above code**:
- **Problem**: The OnlineStore class is doing too many things:
  - It handles item management (add_item).
  - It processes payments in the checkout method.
  - It sends notifications (decides whether to send an email or SMS).
  - It updates the inventory.
  - 
- **Why it's bad**:
A class should only have one reason to change. If you want to change the way payments are handled, or how notifications are sent, or how inventory is updated, you'll end up modifying this class, which can introduce bugs in unrelated functionality.
This makes the class harder to understand and maintain because multiple responsibilities are bundled into one.

here's how you can fix it

We’ll refactor the OnlineStore class so that it only manages the cart and checkout process. We'll delegate payment processing, notification sending, and inventory management to separate classes.

```
class InventoryManager:
    def update_inventory(self, items):
        for item in items:
            print(f"Updating inventory for {item}")

class PaymentProcessor:
    def process_payment(self, payment_method, customer):
        if payment_method == "credit_card":
            print(f"Processing credit card payment for {customer}")
        elif payment_method == "cash":
            print(f"Processing cash payment for {customer}")

class NotificationService:
    def send_notification(self, customer, message):
        if "@" in customer:
            print(f"Sending email to {customer}: {message}")
        else:
            print(f"Sending SMS to {customer}: {message}")

class OnlineStore:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def checkout(self, payment_method, customer):
        payment_processor = PaymentProcessor()
        payment_processor.process_payment(payment_method, customer)

        inventory_manager = InventoryManager()
        inventory_manager.update_inventory(self.items)

        notification_service = NotificationService()
        notification_service.send_notification(customer, "Thank you for your purchase!")
```

Output
```
Updating inventory for Laptop
Sending email to customer@example.com: Thank you for your purchase!
```

Now, each class has a single responsibility.

**Real-World Example:**
Imagine separating tasks in a store: the **cashier** handles payments, the **inventory manager** handles stock updates, and the communications team sends out notifications. No one is doing multiple jobs at once.


## 2) Open Close Principle
Open & Close display polarity in their literal meanings and so is this concept emulating something similar to their literal meanings. 
- Open: Open to extention of functionalities
- Close: Close to modification of existing functions

**Violation in the above code**:
**Problem**: The checkout method is not open for extension but open for modification. Every time a new payment method or notification type is introduced (e.g., adding PayPal, or sending push notifications), you’ll need to modify the existing method.

**Why it's bad:**

Every time you change the logic inside checkout, you risk breaking the current functionality. The system should allow new features (like new payment methods) to be added without modifying the existing code.
This design is rigid and not future-proof.

We’ll make the system open for extension by abstracting the payment methods into separate classes. This way, we can easily add new payment types without modifying the existing OnlineStore class.

This is the interface
```
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process(self, customer):
        pass

class CreditCardPayment(PaymentMethod):
    def process(self, customer):
        print(f"Processing credit card payment for {customer}")

class CashPayment(PaymentMethod):
    def process(self, customer):
        print(f"Processing cash payment for {customer}")

class OnlineStore:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def checkout(self, payment_method: PaymentMethod, customer):
        payment_method.process(customer)

        inventory_manager = InventoryManager()
        inventory_manager.update_inventory(self.items)

        notification_service = NotificationService()
        notification_service.send_notification(customer, "Thank you for your purchase!")
```

```
online_store = OnlineStore()
online_store.add_item('Laptop')
online_store.checkout(CreditCardPayment(), 'customer@example.com')
```

**OUTPUT**
```
Processing credit card payment for customer@example.com
Updating inventory for Laptop
Sending email to customer@example.com: Thank you for your purchase!
```

In this manner we are open to adding new payment methods like Cash On Delivery, PayPal or Apple Pay, etc. but in the same manner we are not editing any of the pre-existing code.

```
class PayPalPayment(PaymentMethod):
    def process(self, customer):
        print(f"Processing PayPal payment for {customer}")
```

**Real-World Example:**
In a store, imagine you have different payment terminals for credit cards, cash, and PayPal. The terminals don’t need to be modified when a new payment method is introduced; you just add a new terminal.


## 3) Liskov Substitution Principle
**Definition**: Objects of a subclass should be replaceable with objects of the superclass without breaking the system.

**In simple terms:** If class B is a subclass of class A, then B should be able to replace A without any issues.

**Problem:** In this case, although it's not explicitly written, the violation will happen when you try to replace this with a different class. For example, if you subclass OnlineStore and change how checkout works but it no longer supports the add_item method in the same way, or doesn't update the inventory correctly, that would violate LSP.

Let’s assume you extend the store to support different types of stores (e.g., physical store vs. online store). You need to ensure that subclasses can be used interchangeably without breaking the system.

```
class Store(ABC):
    @abstractmethod
    def checkout(self, payment_method, customer):
        pass

class OnlineStore(Store):
    def checkout(self, payment_method, customer):
        print(f"Processing online store checkout for {customer}")

class PhysicalStore(Store):
    def checkout(self, payment_method, customer):
        print(f"Processing physical store checkout for {customer}")
```

Both stores now support checkout, and the system can substitute an OnlineStore with a PhysicalStore without any issues.

**In the real world:**

**Example**: Suppose in a warehouse, you use robots for inventory updates. If one robot is replaced by another, it should work the same way. If the replacement robot can't access the stockroom or update the inventory correctly, it would cause chaos.

## 4) Interface Segregation Principle

**Definition:** A class should not be forced to implement interfaces it does not use.

**In simple terms:** Don’t make classes implement methods they don’t need.


**Problem:** There’s no clear interface segregation here, but when this code expands, adding more and more unrelated features to OnlineStore, the class will start to become overburdened. If you later want to reuse parts of the system (say for payment or notification handling), you'll be forced to deal with unnecessary methods that you don't need.

**In the real world:

Example:** Imagine if a payment terminal in a store is also responsible for turning on the lights or controlling the store's air conditioning. The device would be overloaded with responsibilities it doesn't need.

We’ll break down large, unwieldy interfaces into smaller, more specific ones. This way, classes only implement what they actually need.

You can apply the Interface Segregation Principle (ISP) by creating separate authentication mechanisms for different payment methods—one for SMS-based authentication and another for PIN-based authentication. This approach will allow each payment method to use the appropriate authentication class without being burdened by unnecessary methods or logic.

```
from abc import ABC, abstractmethod

class AuthenticationInterface(ABC):
    @abstractmethod
    def authenticate(self, customer):
        pass

class SMSAuth(AuthenticationInterface):
    def authenticate(self, customer):
        print(f"Sending SMS to {customer} for authentication.")

class PINAuth(AuthenticationInterface):
    def authenticate(self, customer):
        print(f"Requesting PIN from {customer} for UPI authentication.")


class PaymentMethod(ABC):
    def __init__(self, auth_method: AuthenticationInterface):
        self.auth_method = auth_method
    
    @abstractmethod
    def process_payment(self, customer):
        pass

class CreditCardPayment(PaymentMethod):
    def process_payment(self, customer):
        print(f"Processing credit card payment for {customer}")
        self.auth_method.authenticate(customer)

class DebitCardPayment(PaymentMethod):
    def process_payment(self, customer):
        print(f"Processing debit card payment for {customer}")
        self.auth_method.authenticate(customer)

class UPIPayment(PaymentMethod):
    def process_payment(self, customer):
        print(f"Processing UPI payment for {customer}")
        self.auth_method.authenticate(customer)
```

```
# Creating instances with specific authentication mechanisms
credit_payment = CreditCardPayment(SMSAuth())
debit_payment = DebitCardPayment(SMSAuth())
upi_payment = UPIPayment(PINAuth())

# Simulating the payment process
credit_payment.process_payment("customer@example.com")
debit_payment.process_payment("customer2@example.com")
upi_payment.process_payment("customer3@example.com")
```

**OUTPUT**
```
Processing credit card payment for customer@example.com
Sending SMS to customer@example.com for authentication.

Processing debit card payment for customer2@example.com
Sending SMS to customer2@example.com for authentication.

Processing UPI payment for customer3@example.com
Requesting PIN from customer3@example.com for UPI authentication.
```


## 5) Dependancy Inversion Principle

Definition: High-level modules should not depend on low-level modules. Both should depend on abstractions (interfaces).

In simple terms: Instead of classes depending directly on concrete implementations, they should rely on interfaces or abstract classes.


**Problem:** The checkout method directly depends on low-level details like sending emails or processing payments. There are no abstractions, making the OnlineStore tightly coupled with these implementations. If you want to change the notification method (e.g., to send push notifications), you'll have to modify the class.

**In the real world:

Example:** In a store, instead of manually sending a message to customers after each purchase, you’d want a system where different communication channels can be easily swapped in and out without changing the whole store’s operation.

```
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount}")

class DebitCardPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing debit card payment of {amount}")

class UPIPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing UPI payment of {amount}")


class OnlineStore:
    def __init__(self, payment_processor: PaymentProcessor):
        self.payment_processor = payment_processor

    def checkout(self, amount):
        self.payment_processor.process_payment(amount)


# Creating instances with different payment methods
credit_store = OnlineStore(CreditCardPayment())
debit_store = OnlineStore(DebitCardPayment())
upi_store = OnlineStore(UPIPayment())

# Process payments
credit_store.checkout(100)  # Processing credit card payment of 100
debit_store.checkout(200)   # Processing debit card payment of 200
upi_store.checkout(300)     # Processing UPI payment of 300
```

**OUTPUT**
```
Processing credit card payment of 100
Processing debit card payment of 200
Processing UPI payment of 300
```
**Real World:** 
Imagine a restaurant:

Instead of the cashier knowing how to process different payment methods (credit, debit, cash, UPI), the cashier just hands the payment to a payment device.
The payment device (abstraction) handles the payment processing based on the payment method.
The cashier doesn’t care how the payment is processed, they just know that they hand it off to a device that processes it.
If the restaurant later adds a new payment method (e.g., digital wallets), the cashier's behavior doesn't change—they still hand it off to the same payment device (abstraction), which now knows how to handle the new method.

This decoupling keeps the process flexible and extendable.

## Conclusion
That's all for S.O.L.I.D Principles, these principles are very essential in order to write clean, comprehensive code and as we keep writing code we don't have to remember these principles rather we can just integrate them on the go.




