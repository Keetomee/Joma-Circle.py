class customer(object):
    def __init__(self):
        self.name = ""
        self.Destnation = ""
        self.vehicleClass = ""
        self.tollFee = ""

    def customer_info(self):
        self.name = input("NAME: ")
        self.Destination = input("Destination: ")

        class1Vehicle = {"Car", "Jeepney", "Van", "Pickup", "Motorcycle"}
        class2Vehicle = {"Bus", "Truck"}
        class3Vehicle = {"Tanker", "Trailer"}
        while True:
            self.vehicleClass = input("Vehicle Type: ")
            if self.vehicleClass in class1Vehicle:
                self.vehicleClass = "Class 1 Vehicle"
                self.tollFee = "P50.0"
                break
            elif self.vehicleClass in class2Vehicle:
                self.vehicleClass = "Class 2 Vehicle"
                self.tollFee = "P100.0"
                break
            elif self.vehicleClass in class3Vehicle:
                self.vehicleClass = "Class 3 Vehicle"
                self.tollFee = "P150.0"
                break
            else:
                print("Invalid vehicle type. Please try again.")
                continue
    def show_data(self):
        print("Name: " + self.name)
        print("Destination: " + self.Destination)
        print("Vehicle Class:  " + self.vehicleClass)
        print("Toll Booth Fee: " + self.tollFee)

receipt = []
for i in range(1):
    details = customer()
    details.customer_data()
    receipt.append(details)
for i in range(1):
    receipt[i].show_data()

