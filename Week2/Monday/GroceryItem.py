class GroceryItem: 
    def __init__(self, title, quantity, price = ""):
        self.title = title
        self.quantity = quantity
        self.price = price

    @staticmethod
    def intake_grocery_item():
        grocery_list_title = input("Enter an item to add to your list: ")
        grocery_list_quantity = input("Enter the quantity of this item you need to buy: ")
        grocery_list_price = input("Enter the price of the item you need to buy or press \"Enter\" to continue: ")
        return (grocery_list_title, grocery_list_quantity, grocery_list_price)

    @staticmethod
    def create_grocery_item(title, quantity, price):
        grocery_item = GroceryItem(title, quantity, price)
        return grocery_item
