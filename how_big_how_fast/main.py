from src.how_big import HowBig
from src.how_fast import HowFast

menu = {
    0: "Quit",
    1: "How many binary digits (bit) are required for the unsigned representation of an unsigned integer?",
    2: "How much space is required to store the names, addresses, and a phone number for residences?",
    3: "How many nodes and levels can I expect the binary tree to store all of my integers?",
    4: "How much space that all of my integers will occupy on a 32-bit architecture (x32)?",
    5: "How long world a book take to send it over modem line?",
    6: "How long world to take to search a binary tree?",
    7: "How long world to brute force an unix password?",
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
        print(
            f"To store {n} integers in binary tree need {n} nodes and {result} levels"
        )
    elif option == 4:
        print("This option is not ready to support")
    elif option == 5:
        number_of_pages = int(input("Enter number of page: "))
        baud_rate = int(input("Enter baud rate: "))
        modem_coeficient = int(input("Enter modem coeficient: "))
        result = HowFast().compute_tranmission_time(
            number_of_pages, baud_rate, modem_coeficient
        )
        print(
            f"To send a book {number_of_pages} pages over {baud_rate} "
            f"baud modem line, you need {result}s (~ {result//60}m)"
        )
    elif option == 6:
        number_of_records = int(input("Enter number of records: "))
        result = HowFast().compute_binary_search_tree_time(number_of_records)
        print(
            f"To search a binary tree {number_of_records} records, "
            f"you need {result}ms"
        )
    elif option == 7:
        hash_length = int(input("Enter hash string length: "))
        result = HowFast().compute_brute_force_time(hash_length)
        print(
            f"To brute force an unix password with hash string length = {hash_length}, "
            f"you need {result}ms (~ {result//31536000000} years)"
        )
    else:
        print("Invalid option!")
