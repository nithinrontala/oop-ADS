class Movie:
    def __init__(self,mid,title,duration):
        self.movieID = mid
        self.title = title
        self.duration = duration
    
    def getTitle(self):
        return self.title
    
class Ticket:
    def __init__(self,tid,mid,sno,price):
        self.ticketid = tid
        self.mid = mid
        self.seatno = sno
        self.price = price

    def getTicketInfo(self):
        return f"ticketid: {self.ticketid}, movieID: {self.mid}, price: {self.price}, seatno: {self.seatno}"
    
class Booking:
    def __init__(self,ti):
        self.tickets = ti
    
    def bookTicket(self,t):
        self.tickets.append(t)
    
    def cancelTicket(self,tid):
        for i in self.tickets:
            if i.ticketid == tid:
                self.tickets.remove(i)
                return True
        return False
    
    def getBookingDetails(self):
        return self.tickets
    
def main():
# Create a movie and multiple tickets
    movie = Movie(1, "Inception", 148)
    ticket1 = Ticket(101, movie.movieID, "A10", 12.5)
    ticket2 = Ticket(102, movie.movieID, "A11", 12.5)
    booking = Booking([])
    # Test booking tickets
    booking.bookTicket(ticket1)

    booking.bookTicket(ticket2)
    if len(booking.getBookingDetails()) != 2:
        print("Error: Tickets not booked correctly.")
    # Test ticket cancellation
    cancel_valid = booking.cancelTicket(101)
    print("Ticket 101 cancelled:", cancel_valid)
    cancel_invalid = booking.cancelTicket(999)
    print("Attempt cancellation of non-existent ticket:", cancel_invalid)
    # Final booking details
    print("Remaining tickets:")
    for t in booking.getBookingDetails():
        print(t.getTicketInfo())
if __name__ == '__main__':
    main()