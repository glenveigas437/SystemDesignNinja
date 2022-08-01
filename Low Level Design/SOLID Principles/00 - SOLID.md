# Getting Started with S.O.L.I.D Principles


Have a look at this example,

```
class Order:
    items = []
    quantities = []
    prices = []
    payments = ['Debit Card', 'Credit Card', 'UPI', 'PayPal']
    status = "open"
    
    def addItem(self, item, quantity, price):
        self.items.append(item)
        self.quantities.append(quantity)
        self.prices.append(price)
    
    def totalPrice(self):
        total=0
        for currentItem in range(len(self.items)):
            total+= self.quantities[currentItem]*self.prices[currentItem]
        
        print(f"Your Total Bill is ${total}")
    
    def payOrder(self, paymentMethod, securityCode):
        time.sleep(10)
        print(f"{datetime.datetime.now().day} / {datetime.datetime.now().month} / {datetime.datetime.now().year} - {datetime.datetime.now().hour} : {datetime.datetime.now().minute} : {datetime.datetime.now().second}: Paying for your order via : {paymentMethod}")
        time.sleep(10)
        print(f"{datetime.datetime.now().day} / {datetime.datetime.now().month} / {datetime.datetime.now().year} - {datetime.datetime.now().hour} : {datetime.datetime.now().minute} : {datetime.datetime.now().second}: Verifiying your Security Code: {securityCode}")
        self.status = "Paid"
        if self.status == "Paid":
            print(f"{datetime.datetime.now().day} / {datetime.datetime.now().month} / {datetime.datetime.now().year} - {datetime.datetime.now().hour} : {datetime.datetime.now().minute} : {datetime.datetime.now().second}: SUCCESS!")
        if paymentMethod not in self.payments:
            raise Exception(f"Unsupported Payment Method - {paymentMethod}")

order1=Order()

order1.addItem('MacBook Pro M1 2022', 1, 1000)
order1.addItem('iPhone 13', 2, 1500)
order1.addItem('iPad Pro 2022', 1, 700)
order1.addItem('MacBook Air M2 2022', 1, 1200)

order1.totalPrice()

order1.payOrder('Debit Card', 437)

```

|Output                                                               |
 --------------------------------------------------------------------
| Your Total Bill is $5900                                            |
| 1 / 8 / 2022 - 18 : 30 : 50: Paying for your order via : Debit Card
  1 / 8 / 2022 - 18 : 31 : 0: Verifiying your Security Code: 437
  1 / 8 / 2022 - 18 : 31 : 0: SUCCESS!                                |


this piece of code replicates the functionality of an Online Shopping system like Amazon where there is a class named ```Order```
