class Hotel:

    def __init__(self):

        self.rooms = {
            101: 2,
            102: 4,
            103: 6,
            104: 2,
            105: 3
        }

        self.bookedRooms = {}

        for roomId in self.rooms:
            self.bookedRooms[roomId] = False

  
        self.number_of_rooms = len(self.rooms)


    def book_room(self, numGuests):

        for roomId in self.rooms:

            room_capacity = self.rooms[roomId]

            
            if (not self.bookedRooms[roomId] and
                    room_capacity >= numGuests):

                self.bookedRooms[roomId] = True

                print(f"Room {roomId} booked for {numGuests} guests.")
                return roomId

        print("No available room for that guest count.")
        return None



    def check_out(self, roomId, nights):

     
        if roomId not in self.rooms:
            print("Invalid room id.")
            return

        if not self.bookedRooms[roomId]:
            print("Room is not currently booked.")
            return

      
        room_capacity = self.rooms[roomId]

        bill = 90 * room_capacity * nights

        print(f"Room {roomId} bill: ${bill}")

   
        self.bookedRooms[roomId] = False

        print(f"Room {roomId} is now available.")