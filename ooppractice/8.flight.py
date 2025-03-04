class Flight:
    def __init__(self, fno, o, des, seaava):
        self.flightno = fno
        self.origin = o
        self.destination = des
        self.seatAvailable = seaava

    def reserveSeat(self):
        if self.seatAvailable > 0:
            self.seatAvailable -= 1
            return True
        return False


class Reservation:
    def __init__(self, rid, fno, pn):
        self.reservationID = rid
        self.flightNumber = fno
        self.passengerName = pn

    def getReservationDetails(self):
        return f"1: {self.reservationID} 2: {self.flightNumber} 3: {self.passengerName}"


class ReservationManager:
    def __init__(self, flights, reservations):
        self.flights = flights
        self.reservations = reservations
        self.reservationID = 1

    def makeReservation(self, fno, pn):
        for i in self.flights:
            if i.flightno == fno:
                if i.reserveSeat():
                    r = Reservation(self.reservationID, fno, pn)
                    self.reservations.append(r)
                    self.reservationID += 1
                    return r
        return None

    def cancelReservation(self, rid):
        for r in self.reservations:
            if r.reservationID == rid:
                self.reservations.remove(r)
                return True
        return False


def main():
    i = Flight("FL123", "New York", "London", 2)
    print("Seat reservation 1:", i.reserveSeat())
    print("Seat reservation 2:", i.reserveSeat())
    print("Seat reservation 3 (should fail):", i.reserveSeat())
    reservation1 = Reservation(1, i.flightno, "John Smith")
    reservation2 = Reservation(2, i.flightno, "Jane Doe")
    rm = ReservationManager([i], [])
    rm.makeReservation(i.flightno, "John Smith")
    rm.makeReservation(i.flightno, "Jane Doe")
    print("Reservation details for ID 1:", reservation1.getReservationDetails())
    cancelled = rm.cancelReservation(1)
    print("Reservation 1 cancelled:", cancelled)


if __name__ == '__main__':
    main()
