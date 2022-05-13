from src.my_module import *

"""
input_dates = [
    "Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)",
    "Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)",
    "Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)",
    "Rewards: 01Mar2009(fri), 02Mar2009(sat), 03Mar2009(mon)",
    "Rewards: 26Mar2009(wed), 27Mar2009(thur), 28Mar2009(fri)",
    "Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)",
]
"""

input_dates = [input("example: Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)\ninsert data here:")]


for i in range(len(input_dates)):
    number = input_dates[i]
    cheapest_hotel = get_cheapest_hotel(number)
    print(cheapest_hotel)
