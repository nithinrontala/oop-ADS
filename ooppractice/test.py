# from librarymanagment import Book, Library
# def main():
# # Create books (including one unavailable)
#     book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "ISBN001", True)
#     book2 = Book("1984", "George Orwell", "ISBN002", True)
#     book3 = Book("Moby Dick", "Herman Melville", "ISBN003", False)
#     library = Library()
#     # Test adding books
#     library.addBook(book1)
#     library.addBook(book2)
#     library.addBook(book3)
#     if len(library.listAllBooks()) != 3:
#         print("Error: Not all books added.")
#     # Test listing all books
#     print("Listing all books:")
#     for b in library.listAllBooks():
#         print(f"Title: {b.getTitle()}, Available: {b.isAvailable()}")
#     # Test search method (existing and non-existing)
#     found = library.searchBookByTitle("1984")
#     print("Found '1984':", found is not None)
#     not_found = library.searchBookByTitle("Nonexistent")
#     print("Search for nonexistent title:", not_found is None)
#     # Test removal (successful and failure)
#     removed_success = library.removeBook("ISBN002")
#     print("Removed ISBN002:", removed_success)
#     removed_failure = library.removeBook("ISBN999")
#     print("Attempted removal of non-existent ISBN:", removed_failure)
#     # Final listing check
#     print("Books remaining:")
#     for b in library.listAllBooks():
#         print(b.getTitle())
# if __name__ == '__main__':
#     main()

# from parkinglot import Car, ParkingLot

# def main():
# # Create car objects
#     car1 = Car("ABC123", "Toyota Camry", "10:00 AM")
#     car2 = Car("XYZ789", "Honda Accord", "10:15 AM")

#     car3 = Car("LMN456", "Ford Focus", "10:30 AM")
#     lot = ParkingLot()
#     # Test parking multiple cars
#     lot.parkCar(car1)
#     lot.parkCar(car2)
#     lot.parkCar(car3)
#     if len(lot.displayCars()) != 3:
#         print("Error: Not all cars parked.")
#     # Validate each car's license plate and model
#     print("Parked cars:")
#     for c in lot.displayCars():
#         print(f"{c.getLicensePlate()} - {c.getModel()}")
#     # Test removing an existing car
#     removed = lot.removeCar("ABC123")
#     print("Car ABC123 removed:", removed)
#     # Attempt to remove non-existent car
#     removed_nonexistent = lot.removeCar("ZZZ999")
#     print("Non-existent car removal:", removed_nonexistent)
#     # Final state of parked cars
#     print("Remaining cars:")
#     for c in lot.displayCars():
#         print(c.getLicensePlate())
# if __name__ == '__main__':
#     main()

# from movie import Movie, Ticket, Booking

# def main():
# # Create a movie and multiple tickets
#     movie = Movie(1, "Inception", 148)
#     ticket1 = Ticket(101, movie.movieID, "A10", 12.5)
#     ticket2 = Ticket(102, movie.movieID, "A11", 12.5)
#     booking = Booking()
#     # Test booking tickets
#     booking.bookTicket(ticket1)

#     booking.bookTicket(ticket2)
#     if len(booking.getBookingDetails()) != 2:
#         print("Error: Tickets not booked correctly.")
#     # Test ticket cancellation
#     cancel_valid = booking.cancelTicket(102)
#     print("Ticket 101 cancelled:", cancel_valid)
#     cancel_invalid = booking.cancelTicket(999)
#     print("Attempt cancellation of non-existent ticket:", cancel_invalid)
#     # Final booking details
#     print("Remaining tickets:")
#     for t in booking.getBookingDetails():
#         print(t.getTicketInfo())
# if __name__ == '__main__':
#     main()

from employee import Employee, Payroll

def main():
# Create employees
    emp1 = Employee(1, "Alice", 20.0)
    emp2 = Employee(2, "Bob", 25.0)
    emp3 = Employee(3, "Charlie", 30.0)
    payroll = Payroll()
    # Hours mapping including an edge case with zero hours
    hours_map = {1: 40.0, 2: 35.0, 3: 0.0}
    pay_results = payroll.processPayroll(hours_map)
    print("Payroll results:")
    for emp_id, pay in pay_results.items():
        print(f"Employee ID {emp_id} earned: {pay}")
if __name__ == '__main__':
    main()