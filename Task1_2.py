# Lesson 1: Python Dictionaries
# 2. Advanced Data Handling with Python

class HotelBookingSystem:
    def __init__(self):
        # Initialize the hotel room structure
        self.hotel_rooms = {
            "101": {"status": "available", "customer": ""},
            "102": {"status": "booked", "customer": "John Doe"}
        }

    def book_room(self, room_number, customer_name):
        """
        Book a room by marking it as booked and assigning a customer name.
        """
        if room_number in self.hotel_rooms:
            if self.hotel_rooms[room_number]["status"] == "available":
                self.hotel_rooms[room_number]["status"] = "booked"
                self.hotel_rooms[room_number]["customer"] = customer_name
                print(f"Room {room_number} has been booked by {customer_name}.")
            else:
                print(f"Room {room_number} is already booked.")
        else:
            print(f"Invalid room number: {room_number}")

    def check_out(self, room_number):
        """
        Check out a customer by marking the room as available and removing the customer name.
        """
        if room_number in self.hotel_rooms:
            if self.hotel_rooms[room_number]["status"] == "booked":
                customer_name = self.hotel_rooms[room_number]["customer"]
                self.hotel_rooms[room_number]["status"] = "available"
                self.hotel_rooms[room_number]["customer"] = ""
                print(f"{customer_name} has checked out from Room {room_number}.")
            else:
                print(f"Room {room_number} is already available.")
        else:
            print(f"Invalid room number: {room_number}")

    def display_status(self):
        """
        Display the status of all rooms.
        """
        print("Hotel Room Status:")
        for room_number, room_info in self.hotel_rooms.items():
            print(f"Room {room_number}: {room_info['status']} ({room_info['customer']})")


# Example usage
if __name__ == "__main__":
    hotel_system = HotelBookingSystem()
    hotel_system.book_room("103", "Alice")
    hotel_system.check_out("102")
    hotel_system.display_status()
