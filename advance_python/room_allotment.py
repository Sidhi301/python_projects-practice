rooms = {}  
total_rooms = 5
available_rooms = list(range(1, 1 + total_rooms))  

while True:
    choice = input("Do you want  a room: ").lower()
    if choice != "yes":
        break
    
    if not available_rooms:
        print("Sorry, no rooms available.")
        break
    
    name = input("Enter name: ")
    members = int(input("Enter number of members: "))
    
    
    room_number = available_rooms.pop(0)
    rooms[room_number] = {"Name": name, "Members": members}
    
    print(f"Room {room_number} allotted to {name} for {members} members.")
    print(rooms)


print("\nAll Room Allotments:")
for room, info in rooms.items():
    print(f"Room {room}: {info['Name']} ({info['Members']} members)")
