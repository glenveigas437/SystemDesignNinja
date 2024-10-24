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


class AuthenticationInterface(ABC):

  @abstractmethod
  def authenticate(self):
    pass

  
class PaymentMethod(ABC):
  def __init__(self, authentication: AuthenticationInterface):
    self.authentication = authentication
  
  @abstractmethod
  def pay(self):
    pass


class SMSAuthentication(AuthenticationInterface):

  def authenticate(self):
    print(f'Authenticating via SMS')

class PINAuthentication(AuthenticationInterface):

  def authenticate(self):
    print(f'Authenticating via PIN')

class TraditionalPaymentMethod(PaymentMethod):

  @abstractmethod
  def pay(self):
    pass

class DigitalPaymentMethod(PaymentMethod):

  @abstractmethod
  def pay(self):
    pass

class DebitCardPayment(DigitalPaymentMethod):
  def pay(self, amount):
    self.authentication.authenticate()
    print(f'Paying {amount} via Debit Card')

class CreditCardPayment(DigitalPaymentMethod):
  def pay(self, amount):
    self.authentication.authenticate()
    print(f'Paying {amount} via Credit Card')

class UPIPayment(DigitalPaymentMethod):
  def pay(self, amount):
    self.authentication.authenticate()
    print(f'Paying {amount} via UPI')

class CashOnDeliveryPayment(TraditionalPaymentMethod):
  def pay(self, amount):
    self.authentication.authenticate()
    print(f'{amount} will be paid to delivery partner')


class CourseSeller:
  def __init__(self, payment_method):
    self.courses = []
    self.payment_method = payment_method

  def add_course(self, course):
    self.courses.append(course)
  
  def buy_course(self):
    total_amount = reduce(lambda acc, course: acc + course.course_price, self.courses, 0)
    self.payment_method.pay(total_amount)

course1 = TechnicalCourse('DSA', 10000)
course2 = NonTechnicalCourse('Public Speaking', 20000)
course3 = TechnicalCourse('System Design', 5000)
course4 = NonTechnicalCourse('Art', 1000)
  
course_seller = CourseSeller(DebitCardPayment(PINAuthentication()))
course_seller.add_course(course1)
course_seller.add_course(course2)
course_seller.buy_course()

print("\n")

course_seller = CourseSeller(CashOnDeliveryPayment(SMSAuthentication()))
course_seller.add_course(course3)
course_seller.add_course(course4)
course_seller.buy_course()
