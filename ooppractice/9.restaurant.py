class MenuItem:
    def __init__(self, id, name, price):
        self.itemID = id
        self.name = name
        self.price = price

    def getItemDetails(self):
        return f"item: {self.itemID}, name: {self.name}, price: {self.price}"

class Order:
    def __init__(self, oid, items, tno):
        self.orderID = oid
        self.items = items
        self.tableNumber = tno

    def addItem(self, item):
        self.items.append(item)

    def calculateTotal(self):
        totalprice = 0
        for i in self.items:
            totalprice += float(i.price)
        return totalprice

    def removeItem(self, item_id):
        for item in self.items:
            if item.itemID == item_id:
                self.items.remove(item)
                return True
        return False

class OrderManager:
    def __init__(self,o):
        self.order = o

    def createOrder(self, order):
        self.order.append(order)

    def cancelOrder(self, oi):
        for i in self.order:
            if i.orderID == oi:
                self.order.remove(i)
                return True
        return False

    def getOrder(self, id):
        for i in self.order:
            if i.orderID == id:
                return i
        return None

def main():
    # Create menu items
    item1 = MenuItem(1, "Burger", 8.5)
    item2 = MenuItem(2, "Fries", 3.0)
    item3 = MenuItem(3, "Soda", 2.0)
    # Create an order and add items
    order = Order(101, [], 5)
    order.addItem(item1)
    order.addItem(item2)
    order.addItem(item3)
    total = order.calculateTotal()
    print("Calculated total:", total)
    # Remove an item and recalc total

    removed = order.removeItem(2)
    print("Item 2 removed:", removed)
    print("New total after removal:", order.calculateTotal())
    # Test OrderManager functionality
    om = OrderManager([])
    om.createOrder(order)
    retrieved_order = om.getOrder(101)
    print("Retrieved order for table", retrieved_order.tableNumber)
    cancelled = om.cancelOrder(101)
    print("Order cancellation status:", cancelled)
if __name__ == '__main__':
    main()
