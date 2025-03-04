class Reservation:
    def __init__(self,name,roomnum):
        # print("hi")
        self.name = name
        self.rm = roomnum
    
    def pres(self,name):
        # print("hi")
        self.name = name

    def rres(self,name,roomnum):
        # print("hi")
        self.name = name
        self.rm = roomnum

    def getRoom(self):
        # print("n",self.rm)
        return self.rm
    
    def getName(self):
        # print("k", self.name)
        return self.name
    
class Hotel:
    def __init__(self):
        self.rooms = ["0"] *5
    
    def buildRooms(self,num):
        # print("l")
        # print(len(self.rooms),num)
        if len(self.rooms) < num:
            # print("l")
            self.rooms.extend(["0"]*num)
            # return f"Added {num} more rooms."
        
        else:
            # print("k")
            self.rooms = self.rooms[:num]
            # print(self.rooms)

    def buildspecificRooms(self,num):
        # print(len(self.rooms))
            # print("l")
        self.rooms.extend(["0"]*num)
        return f"Added {num} more rooms."

    def reserveRoom(self,person):
        for i in range(len(self.rooms)):
            if self.rooms[i] == "0":
                self.rooms[i] = Reservation(person,i+1)
                # print(self.rooms)
                return f"{person} reserved Room {i+1}"
        return f"Hotel is full. No room available for {person}"
    
    def reservespecific(self,person,roomnum):
        for i in range(len(self.rooms)):
            if self.rooms[i] != "0":
                if roomnum - 1 >= len(self.rooms) or self.rooms[roomnum - 1] != "0":
                    # print(len(self.rooms))
                    # print(self.rooms[roomnum-1])
                    self.rooms[roomnum - 1] = Reservation(person, roomnum)
                    # print("hi")
                    return f"{person} reserved Room {roomnum}" 
            else:
                self.rooms[roomnum - 1] = Reservation(person, roomnum)
                return f"{person} reserved Room {roomnum}"
                

    
    def cancelReservation(self,person):
        for i in range(len(self.rooms)):
            if self.rooms[i] !="0" and self.rooms[i].getName() == person:
                self.rooms[i] = "0"  
        print(f"Cancelled reservations for {person}")

    
    def printReservations(self):
        total_reservations = 0
        available_rooms = 0
        print("Current Reservations:")
        for room in self.rooms:
            if room != "0":
                # print(i)
                # print(i)
                print(f"{room.getName()} - Room {room.getRoom()}")
                # print("j")
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
            # print(s)
            if s[0].isdigit():
                h.buildRooms(int(s[0]))
            else:
                if len(s) <= 2:
                    if s[0] == "reserve":
                        print(h.reserveRoom(s[1]))
                    elif s[0] == "print":
                        # print("entered")
                        h.printReservations() 
                    elif s[0] == "cancel":
                        h.cancelReservation(s[1])
                    elif s[0] == "build":
                        # print("l")
                        print(h.buildspecificRooms(int(s[1])))
                else:
                    if s[0] == "reserve":
                        print(h.reservespecific(s[1],int(s[2])))
        except:
            break
    
if __name__ =="__main__":
    main()