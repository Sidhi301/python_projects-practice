# inventory management

dict1 ={}

class inventory:

    def check_availability(self, item):
        if item in dict1:
            print(f"{item} is available")
            print("Category:", dict1[item][0])
            print("Quantity:", dict1[item][1])
            print("Price:", dict1[item][2])
        else:
            print(f"{item} is not available")

    def add_items(self, item, category, quantity, price):
        if item in dict1:
            print("Item already exists, updating quantity")
            dict1[item][1]+=quantity
        else:
            dict1[item] = [category, quantity, price]
            print("Item added successfully")
        print(dict1)

    def delete_item(self, item, quantity):
        if item not in dict1:
            print("Item not found")
        else:
            dict1[item][1] -= quantity
            if dict1[item][1]<= 0:
                del dict1[item]
                print("Item removed completely")
        print(dict1)


i1 = inventory()

while True:
    print("1. Check item")
    print("2. Add item")
    print("3. Delete item")
    print("4. Exit")

    c = int(input("Enter choice: "))

    if c == 4:
        break

    if c == 2:
        item = input("Enter item: ")
        category = input("Enter category Fruits or Vegetables: ")
        q = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        i1.add_items(item, category, q, price)

    elif c == 1:
        item = input("Enter item: ")
        i1.check_availability(item)

    elif c == 3:
        item = input("Enter item: ")
        q = int(input("Enter quantity to delete: "))
        i1.delete_item(item, q)