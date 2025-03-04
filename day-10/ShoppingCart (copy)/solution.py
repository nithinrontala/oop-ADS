class ShoppingCart:
    def __init__(self):
        self.name = ""
        self.price = 0.0
        self.quantity = 1.0

class Cart:
    def __init__(self):
        self.items = {}
        self.c = ShoppingCart()
        self.pri = self.c.price

    def add_items(self, item, price, quantity):
        self.pri += int(price) * int(quantity)
        self.quantity = quantity

        if item in self.items:
            self.items[item][1] += int(quantity)
            return f"Quantity updated for item: {item}"
        else:
            self.items[item] = [price, quantity]

        return f"Item added to cart: {item}"
    
    def viewingCart(self):
        if len(self.items) == 0:
            return "Cart is empty."
        else:
            final_cart_summary = "Items in Cart:\n"
            total_price = 0.0
            for k, v in self.items.items():
                item_total = float(v[0]) * float(v[1])
                total_price += item_total
                final_cart_summary += f"{k} - ${float(v[0]):.2f} × {int(v[1])} = ${item_total:.2f}\n"
            
            final_cart_summary += f"Total Amount: ${total_price:.2f}"
            return final_cart_summary.strip()
    
    def removeitems(self, item):
        if item in self.items:
            a = int(self.items[item][0]) * int(self.items[item][1])
            self.pri -= float(a)
            self.items.pop(item)
            return f"Item removed from cart: {item}"
        else:
            return f"Item not found in the cart: {item}"
        
    def applyDiscount(self):
        discount = 0.10
        a = self.pri
        a -= self.pri * discount 
        return f"Total after 10% discount: ${a:.2f}"

    def Shopping(self):
        while True:
            try:
                s = input().split()
                if not s:
                    continue
                if s[0] == "Remove":
                    print(self.removeitems(s[2].strip(",")))
                elif s[0] == "DisplayCart":
                    print(self.viewingCart())
                elif s[0] == "Add":
                    print(self.add_items(s[2].strip(","), int(s[3].strip(",")), int(s[4].strip())))                    
                elif s[0] == "ApplyDiscount":
                    print(self.applyDiscount())
            except:
                break

s = Cart()
s.Shopping()
