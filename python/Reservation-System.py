# This is Ash.

ascii_art = """
 █████╗ ███████╗██╗  ██╗    ██╗  ██╗ ██████╗ ████████╗███████╗██╗
██╔══██╗██╔════╝██║  ██║    ██║  ██║██╔═══██╗╚══██╔══╝██╔════╝██║
███████║███████╗███████║    ███████║██║   ██║   ██║   █████╗  ██║
██╔══██║╚════██║██╔══██║    ██╔══██║██║   ██║   ██║   ██╔══╝  ██║
██║  ██║███████║██║  ██║    ██║  ██║╚██████╔╝   ██║   ███████╗███████╗
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚══════╝
"""

class Room:
    def __init__(self, room_type, price, available):
        self.type = room_type
        self.price = price
        self.available = available

class Reservation:
    def __init__(self, reservation_id, guest_name, room_type, num_days, is_vip):
        self.reservation_id = reservation_id
        self.guest_name = guest_name
        self.room_type = room_type
        self.num_days = num_days
        self.is_vip = is_vip

room_database = {
    "single": Room("single", 100, True),
    "double": Room("double", 150, True),
    "suite": Room("suite", 200, True)
}

reservations = []
next_reservation_id = 1

def make_reservation(guest_name, room_type, num_days, is_vip):
    if is_VIP == False:
        print("This is the way out!\n")
    elif room_type in room_database and room_database[room_type].available:
        # Calculate the price
        price = num_days * (55 if is_vip else room_database[room_type].price)

        # Update room availability
        room_database[room_type].available = False

        # Create a reservation
        reservation = Reservation(next_reservation_id, guest_name, room_type, num_days, is_vip)

        # Add the reservation to the database
        reservations.append(reservation)

        # Display reservation confirmation
        print("Reservation successful! Your reservation ID is:", reservation.reservation_id)
        print("Total Price: $", price)
        return True
    else:
        print("Sorry, the selected room type is not available.")
        return False

def display_room_availability():
    print("Room Availability:")
    for room_type, room in room_database.items():
        print("Room Type:", room.type, ", Price: $", room.price, "per day")
        if room.available:
            print("❗Status: Available")
        else:
            print("❗Status: Occupied")

is_VIP = True
def VIP():
    global is_VIP
    password = input("\nPlease Give us your VIP password:")
    if password.lower() == "ash":
        print("Thanks for using our reservation service.")
        is_VIP = True
    else:
        print("You lied to us. We can not book you any room.")
        is_VIP = False

def main():
    while True:
        is_VIP = True
        print("\n\nPlease choose an option: ")
        print("1️⃣ Make a reservation")
        print("2️⃣ Display room availability")
        print("3️⃣ Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            guest_name = input("Enter your name: ")
            room_type = input("Choose a room type (single/double/suite): ")
            num_days = int(input("Enter the number of days you want to stay: "))
            is_vip = input("Are you a VIP user (yes/no): ").lower()
            if is_vip == "yes" or is_vip == "y":
                VIP()
                if is_VIP == False:
                    break
            if is_VIP:
                make_reservation(guest_name, room_type, num_days, is_vip)
        elif choice == "2":
            display_room_availability()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please select a valid option.")

print(ascii_art)
print("\n💎 Welcome to Ash Hotel Reservation System")
if __name__ == "__main__":
    main()

