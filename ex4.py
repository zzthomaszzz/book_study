# Total number of car (100) is stored in this variable(car)
cars = 100
# Space available in each car (4.0) is stored in this variable(space_in_a_car)
space_in_a_car = 4.0
# Number of driver(30) for today assigned in the variable drivers
drivers = 30
# Number of passenger(90) stored in this variable (passengers)
passengers = 90
# This variable(cars_not_driven) calculate the number of cars remaining after the drivers get into their cars)
cars_not_driven = cars - drivers
# This variable(cars_driven) stores the number of cars being used
cars_driven = drivers
# This variable(carpool_capacity) stores the number of passengers the cars can take
carpool_capacity = cars_driven * space_in_a_car
# This variable(average_passengers_per_car) calculates the average people in each car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("we need to put about", average_passengers_per_car, "in each car.")
