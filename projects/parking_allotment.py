# 1. Parking Lot Management: Track vehicle entry/exit, available spots, and compute parking fees.
parking_areas={}
total_slot=[1,2,3,4,5]
class parking:
    def vehicle_entry(self,name,vehicle_no):
        parking_fee=1001
        if len(total_slot)==0:
            print("no parking slot is available")
        else:
            if vehicle_no in [i[1] for i in parking_areas.values()]:
                print("vehicle with this number is already parked")
                return
            slot=total_slot.pop(0)
            parking_areas[slot]=[name,vehicle_no,parking_fee]
            print(f"vehicle is alloted to slot {slot} with parking fee {parking_fee}")
   
    def vehicle_exit(self,vehicle_no):
        for slot,details in parking_areas.items():
            if details[1]==vehicle_no:
                print(f"vehicle with number {vehicle_no} is exiting from slot {slot}")
                total_slot.append(slot)
                del parking_areas[slot]
                break
        else:
            print("vehicle not found")
  

    def alloted_slots(self):
        if len(parking_areas)==0:
            print("no vehicle is parked")
        else:
            for slot,details in parking_areas.items():
                print(f"slot {slot} is alloted to {details[0]} with vehicle number {details[1]}")
                  
obj=parking()

while(True):
    print("choose the option")
    print("1:vehicle entry")
    print("2:vehicle exit")
    print("3:show alloted slots")
    print("4:available slots")
    print("5:exit")
    ch=int(input())
    
    
    if ch==1:
        name=input("enter the name of the owner")
        vehicle_no=input("enter the vehicle number")
        obj.vehicle_entry(name,vehicle_no)
    elif ch==2:
        vehicle_no=input("enter the vehicle number")
        obj.vehicle_exit(vehicle_no)
    elif ch==3:
        obj.alloted_slots()
    elif ch==4:
        print(f"available slots are {total_slot}")
    elif ch==5:
        break

    
        

