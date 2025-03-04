class Vehicle:
    def __init__(self,vid,model,rr,rented):
        self.vehicleID = vid
        self.model = model
        self.rentalRate = rr
        self.isRented = rented

    def rentVehicle(self):
        if self.isRented == False:
            self.isRented = True
            return True
        return False
    
    def returnVehicle(self):
        self.isRented = False

    
class Rental:
    def __init__(self,rid,vid,customerName,duartion):
        self.rentalID = rid
        self.vehicleID = vid
        self.customerName = customerName
        self.rentalDuration = duartion

    def getRentalDetails(self):
        return f"id: {self.rentalID}, vid: {self.vehivcleID}, name: {self.customerName}, duration: {self.rentalDuration}"
    
class RentalService:
    def __init__(self,v,r):
        self.vehicles = v
        self.rentals = r

    def createRental(self, rental):
        for vehicle in self.vehicles:
            if vehicle.vehicleID == rental.vehicleID and vehicle.rentVehicle():
                self.rentals.append(rental)
                return True
        return False

    def endRental(self, rid):
        for rental in self.rentals:
            if rental.rentalID == rid:
                self.rentals.remove(rental)
                for vehicle in self.vehicles:
                    if vehicle.vehicleID == rental.vehicleID:
                        vehicle.returnVehicle()
                        return True
        return False
    


def main():
# Create a vehicle and test rental and return
    vehicle = Vehicle(1, "Sedan", 40.0, False)
    print("Vehicle rented (should be True):", vehicle.rentVehicle())
    print("Vehicle rented again (should be False):", vehicle.rentVehicle())
    vehicle.returnVehicle()
    print("Vehicle available after return:", not vehicle.isRented)
    # Create a rental record and service
    rental = Rental(1, vehicle.vehicleID, "Anna", 3)
    service = RentalService([vehicle], [])
    created = service.createRental(rental)
    print("Rental created:", created)
    # End the rental and verify
    ended = service.endRental(1)
    print("Rental ended:", ended)
    print("Vehicle available after ending rental:", not vehicle.isRented)
if __name__ == '__main__':
    main()