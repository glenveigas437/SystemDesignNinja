class Course:
  def __init__(self, course_name, course_price):
    self.course_name = course_name
    self.course_price = course_price

  
class PaymentMethod:
  def pay(self, payment_method, amount):
    if payment_method == 'Credit Card':
      print(f'Paying {amount} for course via Credit Card')
    
    elif payment_method == 'Debit Card':
      print(f'Paying {amount} for course via Debit Card')

    elif payment_method == 'UPI':
      print(f'Paying {amount} for course via UPI')

class CourseSeller:
  def __init__(self):
    self.courses = []

  def add_course(self, course):
    self.courses.append(course)
  
  def buy_course(self):
    course1 = Course('DSA', 10000)
    self.add_course(course1)

    course2 = Course('System Design', 20000)
    self.add_course(course2)

    payment_method1 = PaymentMethod()
    total_amount = reduce(lambda acc, course: acc + course.course_price, self.courses, 0)
    payment_method1.pay('Credit Card', total_amount)
  
course_seller = CourseSeller()
course_seller.buy_course()
