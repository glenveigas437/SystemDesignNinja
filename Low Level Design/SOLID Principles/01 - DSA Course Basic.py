class CourseSeller:
  def __init__(self):
    self.courses = []
    self.course_price = []

  def add_course(self, course_name):
    self.courses.append(course_name)
  
  def add_price(self, course_amount):
    self.course_price.append(course_amount)
  
  def add_course_to_library(self, course_name, course_amount):
    self.add_course(course_name)
    self.add_price(course_amount)
  
  def get_course_price(self, course_name):
    course_name = course_name
    course_price_index = self.courses.index(course_name)
    course_price = self.course_price[course_price_index]
    return course_price
  
  def buy_course(self, course_name, payment_method):
    course_price = self.get_course_price(course_name)

    if payment_method == 'Credit Card':
      print(f'Paying {course_price} for course {course_name} via Credit Card')
    
    elif payment_method == 'Debit Card':
      print(f'Paying {course_price} for course {course_name} via Debit Card')

    elif payment_method == 'UPI':
      print(f'Paying {course_price} for course {course_name} via UPI')

course_seller = CourseSeller()
course_seller.add_course_to_library('DSA', 10000)
course_seller.add_course_to_library('System Design', 20000)
course_seller.buy_course('DSA', 'UPI')
course_seller.buy_course('System Design', 'Credit Card')
