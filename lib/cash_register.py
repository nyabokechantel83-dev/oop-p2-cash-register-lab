class CashRegister:
    def __init__(self, discount=0):
        # Store the discount and initialize the register
        self._discount = 0
        self.discount = discount

        # Start with no items and a total of zero
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        # Only allow discounts between 0 and 100
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        # Add the item's price to the current total
        self.total += price * quantity

        # Add each quantity of the item to the items list
        for i in range(quantity):
            self.items.append(item)

        # Save the transaction so it can be voided later
        transaction = {
            "item": item,
            "price": price,
            "quantity": quantity
        }

        self.previous_transactions.append(transaction)

    def apply_discount(self):
        # Check if there is a discount to apply
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        # Calculate and apply the discount
        self.total = self.total - (self.total * self.discount / 100)

        print(f"After the discount, the total comes to ${self.total:g}.")

    def void_last_transaction(self):
        # Do nothing if there are no previous transactions
        if len(self.previous_transactions) == 0:
            return

        # Get and remove the last transaction
        transaction = self.previous_transactions.pop()

        item = transaction["item"]
        price = transaction["price"]
        quantity = transaction["quantity"]

        # Remove the transaction amount from the total
        self.total -= price * quantity

        # Remove the items from the items list
        for i in range(quantity):
            self.items.remove(item)