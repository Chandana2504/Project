class Transaction:
    def __init__(self, transaction_id, product_id, quantity, date):
        self.transaction_id = transaction_id
        self.product_id = product_id
        self.quantity = quantity
        self.date = date

class Sale(Transaction):
    def __init__(self, transaction_id, product_id, quantity, sale_price, date):
        super().__init__(transaction_id, product_id, quantity, date)
        self.sale_price = sale_price

class Returns(Transaction):
    def __init__(self, transaction_id, product_id, quantity, reason, date):
        super().__init__(transaction_id, product_id, quantity, date)
        self.reason = reason

