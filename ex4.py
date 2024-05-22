# declaring variables and assigning values to it

cars=100
seat_in_a_car=4
drivers=30
passengers=90
cars_not_driven=cars - drivers
cars_driven=drivers
# multiply and divide the variables
carpool_capacity=cars_driven*seat_in_a_car
average_passengers_per_car=passengers/cars_driven

print("there are", cars, "in garage")
print("there are", drivers, "drivers are available")
print("there will be", cars_not_driven,"cars are not driven today")
print("we can transport", carpool_capacity,"people today")
print("we have", passengers,"to carpool today")
print("we need to put about", average_passengers_per_car,"in each car")
