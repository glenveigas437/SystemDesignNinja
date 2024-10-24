from abc import ABC, abstractmethod

class Course(ABC):

  @abstractmethod
  def __str__(self):
    pass

class TechnicalCourse(Course):
  def __init__(self, course_name, course_price):
    self.course_name = course_name
    self.course_price = course_price
    self.description = ''

  def get_description(self):
    return self.description
  
  def __str__(self):
    return f'{self.course_name} for {self.course_amount}'

class NonTechnicalCourse(Course):
  def __init__(self, course_name, course_price):
    self.course_name = course_name
    self.course_price = course_price
    self.description = ''

  def get_description(self):
    return self.description
  
  def __str__(self):
    return f'{self.course_name} for {self.course_amount}'

  
class PaymentMethod(ABC):
  
  @abstractmethod
  def pay(self):
    pass

class DebitCardPayment(PaymentMethod):
  def pay(self, amount):
    print(f'Paying {amount} via Debit Card')

class CreditCardPayment(PaymentMethod):
  def pay(self, amount):
    print(f'Paying {amount} via Credit Card')

class UPIPayment(PaymentMethod):
  def pay(self, amount):
    print(f'Paying {amount} via UPI')


class CourseSeller:
  def __init__(self):
    self.courses = []

  def add_course(self, course):
    self.courses.append(course)
  
  def buy_course(self, payment_method):
    total_amount = reduce(lambda acc, course: acc + course.course_price, self.courses, 0)
    payment_method.pay(total_amount)
  

course1 = TechnicalCourse('DSA', 10000)
course2 = NonTechnicalCourse('Public Speaking', 20000)
  
course_seller = CourseSeller()
course_seller.add_course(course1)
course_seller.add_course(course2)
course_seller.buy_course(DebitCardPayment())
