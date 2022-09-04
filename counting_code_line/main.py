from src.java_code import JavaCode

menu = {
    0: "Quit",
    1: "Count number of lines java file",
    2: "Print java file with code only",
}

while True:
    for key in menu.keys():
        print(key, "-", menu[key])
    option = int(input("Enter your choice: "))
    if option == 0:
        exit()
    elif option == 1:
        file_name = input(
            "Enter your java file name (ex: test1.java, test2.java, test3.java): "
        )
        result = JavaCode().get_valid_lines(file_name)
        print(f"Number of code lines: {len(result)} lines")
    elif option == 2:
        file_name = input(
            "Enter your java file name (ex: test1.java, test2.java, test3.java): "
        )
        result = JavaCode().get_valid_lines(file_name)
        for line in result:
            print(line)
    else:
        print("Invalid option!")
    print("-" * 100)
