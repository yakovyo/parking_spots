# a list of all arrivals and departures
schedule = []
# collecting all flight numbers
flights = []
# flight that can't arrive due to overbooking
no_spot_flights = []


# adding a new flight
def new_flight(flight_number, arrival, departure):
    # check for primary flight number
    if flight_number in flights:
        print('we can not accept 2 flight with the same flight number')
    else:
        # adding flight to flight list
        flights.append(flight_number)
    # arrival and flight number - adding a minus sign
    arriving = f"{arrival}: {flight_number}-"
    # departure and flight number - adding a plus sign
    departing = f"{departure}: {flight_number}+"
    # adding flights to schedule
    schedule.append(arriving)
    schedule.append(departing)


def timeline(available_spots):
    # parking spots counter
    available_spots = available_spots
    # this loop is for determining if a flight has an available parking spot
    # for each segment (depart or arrival)
    for x in sorted(schedule):
        # if landing
        if '-' in x:
            if available_spots > 0:
                available_spots = available_spots - 1
                print(f'after the landing of flight {x} the amount of available spots are: {available_spots}')
            elif available_spots == 0:
                print(f'Sorry no spot for {x} at the moment.')
                # add flight to non-arrived flights
                no_spot_flights.append(int(x[6:8]))
        # if departing (based on flight arrived)
        elif '+' in x and int(x[6:8]) not in no_spot_flights:
            available_spots = available_spots + 1
            print(f'after the takeoff of flight {x} the amount of available spots are: {available_spots}')
    print('-----------------------------------------')


new_flight(25, 1500, 1615)
new_flight(29, 1800, 1845)
new_flight(35, 1230, 1435)
new_flight(55, 1530, 1825)
new_flight(15, 1455, 1610)
new_flight(22, 1550, 1625)
new_flight(88, 1330, 1525)
new_flight(91, 1000, 1105)
new_flight(66, 1225, 1336)
new_flight(75, 1705, 1752)
new_flight(62, 1400, 1515)
new_flight(52, 1632, 1716)
new_flight(28, 1505, 1549)
new_flight(36, 1700, 1717)
new_flight(53, 1601, 1723)

timeline(3)
# checking which flight can use my terminal
print(sorted(schedule))
print(sorted(flights))
print((sorted(no_spot_flights)))
