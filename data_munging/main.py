from src.soccer import Soccer
from src.weather import Weather

menu = {
    0: "Quit",
    1: "Get the day with the smallest temperature spread",
    2: "Get the name of the team with the smallest difference goals.",
    3: "Get both (DRY fusion)",
}

while True:
    for key in menu.keys():
        print(key, "-", menu[key])
    option = int(input("Enter your choice: "))
    if option == 0:
        exit()
    elif option == 1:
        result = Weather().get_the_smallest_temperature_spread_day()
        day = result["day"]
        spread = result["spread"]
        print(f"Day {day} has the smallest temperature spread with {spread}*")
    elif option == 2:
        result = Soccer().get_the_smallest_goal_difference_team()
        team = result["team"]
        difference = result["difference"]
        print(f"Team {team} has the smallest difference goals with {difference} goals")
    elif option == 3:
        print("This option is not ready to support")
    else:
        print("Invalid option!")
    print("-" * 100)
