# list = ["sponge","table","chair","cloth"]
# list.append("knife")
# print(list)


# list = ["sponge","table","chair","cloth","knife"]
# list.remove("knife")
# print(list)

# list = ["sponge","table","chair","cloth","knife"]
# list.sort()
# print(list)

# list = ["sponge","table","chair","cloth","knife"]
# list.reverse()
# print(list)

# list = ["sponge","table","chair","cloth","knife"]
# print(list[0])

# list = ["sponge","table","chair","cloth","knife"]
# print(list[2])

# list = ["sponge","table","chair","cloth","knife"]
# print(list[4])

# list = ["sponge","table","chair","cloth","knife"]
# print(list[-1])


# car = {
#     "AC" : 7,
#     "wall" : "white",
#     "key" : "gold",
# }
# tv = (car["No. of tv's"])=1
# print(tv)

# door = (car["No. of doors"])=4
# print(door)

# print(car)


# store = {
#     "truck" : 7,
#     "wall" : "white",
#     "key" : "sliver",
# }
# tv = (store["No. of machine"])=1
# print(tv)

# door = (store["No. of doors"])=10
# print(door)

# print(store)




# Home = {
#     "family" : 7,
#     "parent" : "black",
#     "children" : "14",
# }
# tv = (Home["children"])=14
# print(tv)

# door = (Home["family"])=6
# print(door)

# print(Home)

# txt_data = "NIIT Ikeja\n24 Oba Akran Avenue, Ikeja, Lagos"
# file_path = "python.txt"

# with open(file_path, "w") as file:
#     file.write(txt_data)
#     print(f"your '{file_path}' has been created")

# with open("python.txt", "r") as file:
#     content: str = file.read()
#     print(content) # prints: NIIT

# store_items = []  # empty list to store items

# print("=== NIIT STORE INVENTORY ===")

# while True:
#     try:
#         item = input("Enter item name to add to store: ")
        
#         # Check if user typed nothing
#         if item == "":
#             raise ValueError("Item name cannot be empty")
        
#         store_items.append(item)  # add to list
#         print(f"'{item}' has been added. Current items: {store_items}")
        
#         choice = input("Add another item? y/n: ")
#         if choice.lower() != "y":
#             break
            
#     except ValueError as e:
#         print(f"Error: {e}")
#     except Exception as e:
#         print(f"Something went wrong: {e}")

# print("\nFinal Store List:")
# for index, item in enumerate(store_items):  # using index
#     print(f"{index}: {item}")


Name = input("Enter your name:")
course = input("Enter your course:")

statement = f"I am {Name}, i am studying {course}"
print(statement)   






 