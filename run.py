## THIS CLASS IS FOR MANUAL TESTING AND UNDERSTANDING OF HOW CODE WORKS
## YOU CAN EDIT THIS AS YOU NEED


from flight_trip_class import *
from passenger_subClass import *
from airport_class import *

# Do Not Delete this test_flight - it is used for testing purposes as the default flight
test_flight = Flight("heath10550", "JF1234", "Portugal", "United Kingdom", 4, [])

# These are test passengers. Comment/Un-comment when needed
test_passenger = Passenger("Bob",12345,"AJ8127393","Adult")
"""

new_passenger = Passenger("Glad0s",10010, "TST475839","Advanced A.I")
"""
user_input = ""
new_airport = Airport(0, [], [test_passenger])
new_airport.add_flight(test_flight)
while user_input != "exit":

    # Creating the Main Menu
    print("=====================================================\n"
          "Welcome to the Airport terminal.\n"
          "Please select what options you'd like to access:\n"
          " _____________________________\n"
          "|-[A] Flight Options          |\n"
          "|-[B] Passenger Options       |\n"
          "|-[C] Aircraft Options        |\n")

    # Checking for user input
    user_input = input("Please use the corresponding letter to select your choice here: \n")

    # Giving the user a way to exit the loop
    if (user_input.lower() == "exit"):
        print("Thank you for using the terminal. Good Bye! ")

    # If user doesn't exit, continues with the Sub menu for "Flight options"
    elif (user_input.lower() == "a"):
        print(" _______________________________\n"
              "|FLIGHT OPTIONS                 |\n"
              " _______________________________\n"
              "|-[A] Create new Flight         |\n"
              "|-[B] Get list of flights       |\n"
              "|-[C] Get Flight Origin         |\n"
              "|-[D] Get Flight details        |\n")
        user_input = input("Please choose your option: ")

        # This section creates a new flight and adds it to the total list of flights in the current Airport instance
        if (user_input.lower() == "a"):
            air_id = ""
            flight_num = 0
            origin = ""
            destination = ""
            duration = 0
            passenger_list = []
            print("To begin creating a new flight, I must ask you to enter the appropriate fields.")

            air_id = input("Please enter the Aircraft id: ")
            flight_num = input("Flight number: ")
            origin = input("Flight originating from: ")
            destination = input("Flight destination: ")
            duration = input("Flight duration : ")
            passenger_list.append(input("Any passengers so far? (leave blank if none)"))
            new_flight = Flight(air_id, flight_num, origin, destination, duration, passenger_list)

            new_airport.add_flight(new_flight)

            print(new_airport.flight_list)
            print("-----------------------------------------------------")

        # This section returns the current list of flights in the current Airport instance
        if (user_input.lower() == "b"):
            print(new_airport.get_flights())

        # This section returns a given flight's origin within the current Airport instance
        if (user_input.lower() == "c"):
            usr_flight = input("Please enter the flight number for which you'd like to see the origin: \n")
            for i in new_airport.flight_list:
                if (i.flight_num == usr_flight):
                    print(f"Flight {usr_flight} originates from", i.origin)

        # This section returns all the details for a given flight within the current Airport instance
        if (user_input.lower() == "d"):
            print("This functionality requires Staff access. Please input the staff password: ")
            staff_pass_inp = input()
            count = 5
            while count != 0:
                if (staff_pass_inp == "Special-StaffPa$$"):
                    print("Correct password entered. Please conntinue \n")
                    usr_flight = input("Please enter the flight number for which you'd like to see the details of: \n")
                    new_airport.get_flight_details(usr_flight)
                    print("")
                    print("Finished returning the requried output. \n")
                    break


                else:
                    count -= 1
                    print(f"Incorrect password entered. {count} tries remaining.")


    # This section leads to the Passenger options
    elif (user_input.lower() == "b"):
        print(" _______________________________\n"
              "|PASSENGER OPTIONS              |\n"
              " _______________________________\n"
              "|-[A] Create new Passenger      |\n"
              "|-[B] Get list of Passengers    |\n"
              "|-[C] Get Passenger details     |\n")

        user_input = input("Please choose your option: ")

        # This section creates a new passenger and adds it to the selected flight
        if (user_input.lower() == "a"):
            print("To create a new passenger. Please enter their details: ")
            usr_pass_name = input("Name: ")
            usr_pass_taxNum = input("Tax Number: ")
            usr_pass_passport = input("Passport number: ")
            usr_pass_passenger_type = input("Passenger type(Adult/Child/Infant): ")
            user_passenger = Passenger(usr_pass_name, usr_pass_taxNum, usr_pass_passport, usr_pass_passenger_type)
            print("")
            print(f"New Passenger {user_passenger.name} created.")

            user_input = input("Would you like to add this passenger to the default (new_flight) flight?\n"
                               "If 'No' they'll be added to a waiting list of Passengers. ")
            if user_input.lower() == "y":
                test_flight.add_passenger(user_passenger)
                print(f"{user_passenger.name} successfully added to new_flight()\n")
            else:
                new_airport.add_to_waitingList(user_passenger)

        # This section returns a list of passengers for a given flight
        if (user_input.lower() == "b"):
            print("Please enter the flight,"
                  "for which you'd like to see the Passenger list for: ")
            user_input = input()
            for i in new_airport.flight_list:
                if (i.flight_num == user_input):
                    print(i.get_passengers())

        # This section gets passenger details for a given passenger
        if (user_input.lower() == "c"):
            print("To view a passenger's details, input their name: ")
            user_input = input()
            temp_list = new_airport.get_waitinglist()
            for i in temp_list:
                if i.name == user_input:
                    i.get_details()
                    print("")
        # CODE GOES HERE

    # This section leads to the Aircraft options (NOT SURE IF THIS IS NEEDED YET- INCOMPLETE):

    elif (user_input.lower() == "c"):

        print(" _______________________________\n"
              "|AIRCRAFT OPTIONS               |\n"
              " _______________________________\n"
              "|-[A] THIS IS INCOMPLETE        |\n"
              "|-[B] THESE OPTIONS DON'T WORK  |\n"
              "|-[C] NEEDS TO BE UPDATED       |\n"
              "|-[D] OR REMOVED                |\n")

        user_input = input("Please choose your option: ")
