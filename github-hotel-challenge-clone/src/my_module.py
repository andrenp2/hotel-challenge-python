'''
change_string_to_dict -> this function changes the input string,
to a dictionary with client type and weekdays

handle_input_data -> this function removes only the necessary data from the input

get_cheapest_hotel -> returns the cheapest hotel according to customer type and desired dates

'''



def change_string_to_dict(input_string):
    client_type = input_string.split(":")[0]

    input_changed = []

    maxInt = range(len(input_string.split(" ")))

    for i in maxInt:
        a = input_string.split(" ")[i].split(",")[0]
        input_changed.append(a)

    input_changed = input_changed[1:]

    input_dict = {client_type: input_changed}

    return input_dict



def handle_input_data(input_dictionary):

    input_dict = input_dictionary
    client_type_list = list(
        input_dict.keys()
    )  # shows the type of costumer
    new_dict = {}

    for i in range(len(client_type_list)):

        week_days_list = []
        date_list = input_dict[client_type_list[i]]

        for j in range(len(date_list)):
            week_day = (
                input_dict[client_type_list[i]][j]
                .split("2009")[1]
                .split("(")[1]
                .split(")")[0]
            )
            week_days_list.append(week_day)

        week_day_dict = {client_type_list[i]: week_days_list}

        new_dict.update(week_day_dict)

    return new_dict


def get_cheapest_hotel(input_dictionary):  # DO NOT change the function's name

    from operator import itemgetter

    input_string_root = input_dictionary

    dict_input = change_string_to_dict(input_string_root)

    handled_dict = handle_input_data(dict_input)

    client_type_list = list(
        handled_dict.keys()
    )  # shows the costumer type

    week_days = (
        "mon",
        "tues",
        "wed",
        "thru",
        "fri",
    )  
    weekend = ("sat", "sun") 
    count_week = 0
    count_weekend = 0

    for i in range(len(client_type_list)):

        client_type = list(handled_dict.keys())[0]

        ''' ------------------- Regular Costumer ---------------------- '''

        if client_type == "Regular":

            # regular client
            rented_days = handled_dict.get("Regular")

            for i in rented_days:
                if i in week_days:
                    count_week = (
                        count_week + 1
                    )  # count of weekdays that will be reserved

            for j in rented_days:
                if j in weekend:
                    count_weekend = (
                        count_weekend + 1
                    )  # count of weekend days that will be reserved

            lakewood_price = (count_week * 110) + (count_weekend * 90)

            bridgewood_price = (count_week * 160) + (count_weekend * 60)

            ridgewood_price = (count_week * 220) + (count_weekend * 150)

            price_classification = [
                ["Hotel", "Price", "Classification"],
                ["Lakewood", lakewood_price, -3],
                ["Bridgewood", bridgewood_price, -4],
                ["Ridgewood", ridgewood_price, -5],
            ]

            ordered_price = price_classification[0]

            sub_ordered_price = sorted(price_classification[1:], key=itemgetter(1, 2))

            for elem in sub_ordered_price:
                ordered_price.append(elem)

            price_classification = ordered_price

            cheapest_hotel = price_classification[3][0]
            return cheapest_hotel

        ''' ------------------- Rewards Costumer ---------------------- '''

        elif client_type == "Rewards":

            rented_days = handled_dict.get("Rewards")

            for i in rented_days:
                if i in week_days:
                    count_week = (
                        count_week + 1
                    )  

            for j in rented_days:
                if j in weekend:
                    count_weekend = (
                        count_weekend + 1
                    )  

            lakewood_price = (count_week * 80) + (count_weekend * 80)

            bridgewood_price = (count_week * 110) + (count_weekend * 50)

            ridgewood_price = (count_week * 100) + (count_weekend * 30)

            price_classification = [
                ["Hotel", "Price", "Classification"],
                ["Lakewood", lakewood_price, -3],
                ["Bridgewood", bridgewood_price, -4],
                ["Ridgewood", ridgewood_price, -5],
            ]

            ordered_price = price_classification[0]

            sub_ordered_price = sorted(price_classification[1:], key=itemgetter(1, 2))

            for elem in sub_ordered_price:
                ordered_price.append(elem)

            price_classification = ordered_price

            cheapest_hotel = price_classification[3][0]

            return cheapest_hotel

        else:
            print("Something is wrong!")


if __name__ == "__main__":

    input_dates = [
        "Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)",
        "Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)",
        "Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)",
    ]

    for i in range(len(input_dates)):
        number = input_dates[i]
        cheapest_hotel = get_cheapest_hotel(number)
        print(cheapest_hotel)
