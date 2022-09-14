travel_log = {}

country = ""
visits = 0
cities = ""

def record_travel(state, travels, places):
    list_of_cities = []
    for x in places.split(','):
        list_of_cities.append(x.lstrip())

    travel_log[state] = {"visits": travels, "cities" : list_of_cities,}
    return travel_log

while True:
    visited_places = len(travel_log)
    if visited_places == 0:
        print("You have no countries visited so far.")
    else:
        print(f"You've got {visited_places} countries visited so far.")
        print(list(travel_log.keys()))
        detailed_view = (input("Do you want to see full details?(y/n) ")).lower()
        if detailed_view == "y":
            print(travel_log)
        else:
            pass

    extend_dict = (input("Do you want to add new place?(y/n) ")).lower()

    if extend_dict == "y":
        country = input("Please, type in country you've visited (one): ")
        visits = int(input("How many times have you visited that country? "))
        cities = input("Write cites you've visited (separate using coma) ")
        record_travel(country, visits, cities)
    else:
        break
