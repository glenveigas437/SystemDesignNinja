# 1 - Creational Design Patterns

Creational Design Patterns are responsible for efficient object creation mechanisms, which increase the flexibility and reusibility of existing code.

## 1 - Factory Pattern

- Factory Pattern is also called virtual constructor, to describe in simple terms Factory Patterns allow an interface or a class to create an object, but let the subclasses decide which class or object to instantiate. 
- Here, objects are created without exposing the logic to the client, and for creating the new type of object, the client uses the same common interface.

Example:
Amazon Shopping App.

Amazon has 2 types of membership with the premium member subscription (Amazon Prime) providing a lot of benefits like 1-Day/Same Day Delivery, discounts, access to amazing video content and also on-demand music streaming, while the regular members do not receive these perks.

So consider that before Amazon could come up with the concept of Prime, they just built one class for the Regular members but now with the inception of Amazon Prime it comes with its own benefits.



