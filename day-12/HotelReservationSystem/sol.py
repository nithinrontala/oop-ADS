class Reservation:
    def __init__(self, name, roomnum):
        self.name = name
        self.rm = roomnum

    def getRoom(self):
        return self.rm
    
    def getName(self):
        return self.name


class Hotel:
    def __init__(self):
        self.rooms = [None] * 5

    def buildRooms(self, num):
        if len(self.rooms) < num:
            self.rooms.extend([None] * (num - len(self.rooms)))
        else:
            self.rooms = self.rooms[:num]
        return f"Total rooms now: {len(self.rooms)}"

    def reserveRoom(self, person):
        for i in range(len(self.rooms)):
            if self.rooms[i] is None:
                self.rooms[i] = Reservation(person, i + 1)
                return f"{person} reserved Room {i+1}"
        return f"Hotel is full. No room available for {person}"

    def reservespecific(self, person, roomnum):
        if roomnum > len(self.rooms) or roomnum < 1:
            return f"Invalid room number {roomnum}."
        if self.rooms[roomnum - 1] is None:
            self.rooms[roomnum - 1] = Reservation(person, roomnum)
            return f"{person} reserved Room {roomnum}"
        return f"Room {roomnum} is already reserved."

    def cancelReservation(self, person):
        found = False
        for i in range(len(self.rooms)):
            if self.rooms[i] is not None and self.rooms[i].getName() == person:
                self.rooms[i] = None
                found = True
        if found:
            print(f"Cancelled reservation for {person}")
        else:
            print(f"No reservation found for {person}")

    def printReservations(self):
        total_reservations = 0
        available_rooms = 0
        print("Current Reservations:")
        for room in self.rooms:
            if room is not None:
                print(f"{room.getName()} - Room {room.getRoom()}")
                total_reservations += 1
            else:
                available_rooms += 1
        print(f"Total Reservations: {total_reservations}")
        print(f"Available Rooms: {available_rooms}")


def main():
    h = Hotel()
    while True:
        try:
            s = input().split()
            if s[0].isdigit():
                print(h.buildRooms(int(s[0])))
            else:
                if len(s) == 2:
                    if s[0] == "reserve":
                        print(h.reserveRoom(s[1]))
                    elif s[0] == "print":
                        h.printReservations()
                    elif s[0] == "cancel":
                        h.cancelReservation(s[1])
                    elif s[0] == "build":
                        print(h.buildRooms(int(s[1])))
                elif len(s) == 3:
                    if s[0] == "reserve":
                        print(h.reservespecific(s[1], int(s[2])))
        except:
            break


if __name__ == "__main__":
    main()
