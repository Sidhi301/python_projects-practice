# 1. Parking Lot Management: Track vehicle entry/exit, available spots, and compute parking fees.
parking_areas={}
total_slot=[5]



class parking:
    

    def vehicle_entry(self,name,vehicle_no):
        alloted_slot=0
        if vehicle_no in parking_areas:
            return "no duplication vehicle numbers .. slot is alloted"
        else:
            alloted_slot+=1
            parking_areas[alloted_slot]=[vehicle_no,name]
            if alloted_slot ==total_slot:
                print("parking full")
                return 
               
        
            print(f"you can store the vehicle in {alloted_slot} slot")
        return alloted_slot
    def vehicle_exit(slef,vehicle_no,alloted_slot):
        if vehicle_no not in  parking_areas:

            return "The vehicle is not present in the area .."
        else:
            del parking_areas[alloted_slot]
            if slot>=total_slot and slot != 0:
                slot-=1
            print("thank you visit again")
        return alloted_slot

    def alloted_slots(self):
        
        for i in range(len(total_slot)):
            print(f"slot{i}-->{parking_areas[alloted_slot]}")

        
obj=parking()

while(True):
    print("choose the option")
    print("1:vehicle entry")
    print("2:vehicle exit")
    print("3:show alloted slots")
    print("exit")
    ch=int(input())
    n=input("enter your name:")
    vn=input("enter your vehicle number:")
    if ch ==1:
        obj.vehicle_entry(n,vn)
    elif ch ==2:
        obj.vehicle_exit(vn)
    elif ch ==3:
        obj.alloted_slots()
    else:
        break
    

    
        

