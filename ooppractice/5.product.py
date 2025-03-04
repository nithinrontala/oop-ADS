class Product:
    def __init__(self,pid,name,price,stock):
        self.productID = pid
        self.name = name
        self.price = price
        self.quantityInStock = stock

    def updateStock(self,q):
        self.quantityInStock+=q

    def getProductInfo(self):
        return f"id:{self.productID}, name: {self.name}, price: {self.price}, quantity: {self.quantityInStock}"
    
class Inventory:
    def __init__(self,p):
        self.products = p
    
    def updateProductStock(self,id,qu):
        for i in self.products:
            if i.productID == id:
                i.quantityInStock+=qu
                return True
        return False
    
    def addProduct(self,p):
        self.products.append(p)

    def listProducts(self):
        return self.products

        
def main():
    # Create products
    prod1 = Product(1, "Laptop", 1500.0, 10)
    prod2 = Product(2, "Smartphone", 800.0, 20)
    inventory = Inventory([])
    # Test adding products
    inventory.addProduct(prod1)
    inventory.addProduct(prod2)
    if len(inventory.listProducts()) != 2:
        print("Error: Products not added correctly.")
    # Test updating stock
    update_success = inventory.updateProductStock(1, 5)
    print("Updated stock for product 1 (add 5):", update_success)
    update_failure = inventory.updateProductStock(3, 5)
    print("Attempt update for non-existent product:", update_failure)
    # Test listing products
    print("Products in inventory:")
    for p in inventory.listProducts():
        print(p.getProductInfo())
if __name__ == '__main__':
    main()