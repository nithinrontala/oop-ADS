class Review:
    def __init__(self,rid,pid,rt,r):
        self.reviewID = rid
        self.productID = pid
        self.reviewText = rt
        self.rating = r

    def getReviewSummary(self):
        return f"Rating: {self.rating}, Review: {self.reviewText}"
    
class Product:
    def __init__(self,pid,name,price):
        self.productID = pid
        self.name = name
        self.price  =price

    def getProductInfo(self):
        return f"Product: {self.name}, Price: ${self.price}"
    
class ReviewManager:
    def __init__(self,r):
        self.reviews = r

    def addReview(self,rev):
        self.reviews.append(rev)

    def getReviewsByProduct(self,pid):
        r = []
        for i in self.reviews:
            if i.productID == pid:
                r.append(i)
        return r
            
    
def main():
    # Create reviews
    review1 = Review(1, 101, "Great product!", 5)
    review2 = Review(2, 101, "Not bad", 4)
    review3 = Review(3, 102, "Poor quality", 2)

    # Create products
    product1 = Product(101, "Smart Watch", 199.99)
    product2 = Product(102, "Fitness Tracker", 99.99)
    # Create ReviewManager and add reviews
    rm = ReviewManager([])
    rm.addReview(review1)
    rm.addReview(review2)
    rm.addReview(review3)
    # Display reviews for product1 and product2
    print("Reviews for product 101:")
    for r in rm.getReviewsByProduct(101):
        print(r.getReviewSummary())
    print("Reviews for product 102:")
    for r in rm.getReviewsByProduct(102):
        print(r.getReviewSummary())
    # Display product info
    print("Product 101 info:", product1.getProductInfo())
    print("Product 102 info:", product2.getProductInfo())
if __name__ == '__main__':
    main()