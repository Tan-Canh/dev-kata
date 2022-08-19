from src.how_big import HowBig

menu = {
    0: "Quit",
    1: "How many binary digits (bit) are required for the unsigned representation of an unsigned integer?",
    2: "How much space is required to store the names, addresses, and a phone number for residences?",
    3: "How many nodes and levels can I expect the binary tree to store all of my integers?",
    4: "How much space that all of my integers will occupy on a 32-bit architecture (x32)?",
}

while True:
    for key in menu.keys():
        print(key, "-", menu[key])
    option = int(input("Enter your choice: "))
    if option == 0:
        exit()
    elif option == 1:
        n = int(input("Enter your number: "))
        result = HowBig().count_bit(number=n)
        print(f"Number of binary digits (bit) to representation of {n} is {result}")
    elif option == 2:
        n = int(input("Enter number of residences: "))
        result = HowBig().compute_storage_space(record_count=n)
        print(f"To store {n} residences need {result} bytes (~ {result//1024}MB)")
    elif option == 3:
        n = int(input("Enter number of integers you want to store in binary tree: "))
        result = HowBig().get_binary_level_by_number_of_node(node_count=n)
        print(f"To store {n} integers in binary tree need {n} nodes and {result} levels")
    elif option == 4:
        pass
    else:
        print("Invalid option!")
