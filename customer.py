# Imports the shared function used to add a new booking record to the file.
from Regestration import append_regestrations


# Display available car wash services
def view_services():
    # Opens the services file to read the available car wash services.
    file = open("services.txt", "r")

    # Reads each record from the file.
    for line in file:
        # Removes extra spaces and the newline character.
        line = line.strip()
        # Separates the record into individual fields.
        parts = line.split("|")
        # Displays the service name, price, and duration.
        print(parts[1], float(parts[2]), parts[3], "minutes")
    file.close()


# Display available booking slots
def view_available_slots():
    # Gets the requested booking date.
    date = input("Enter date (DD-MM-YYYY): ")

    # Stores the available booking time slots.
    slots = [
        "09:00", "09:45", "10:30", "11:15",
        "12:00", "12:45", "13:30", "14:15",
        "15:00", "15:45", "16:30", "17:15",
        "18:00", "18:45", "19:30", "20:15" 
    ]
    # Creates a list to store slots that are already booked.
    booked_slots = []

    # Opens the bookings file to check existing bookings.
    file = open("bookings.txt" , "r")

    # Reads each record from the file.
    for line in file:
        # Removes extra spaces and the newline character.
        line = line.strip()
        # Separates the record into individual fields.
        parts = line.split("|")

        # Checks whether the booking is for the selected date.
        if parts[3] == date:
            # Adds the booked time to the list of unavailable slots.
            booked_slots.append(parts[4])

    file.close()

    # Displays the available slots heading.
    print("Available_SLots:")

    # Checks each possible booking slot.
    for slot in slots:
        # Displays the slot only if it has not been booked.
        if slot not in booked_slots:
            print(slot)


# Submit a booking request
def request_booking():
    # Gets the customer ID for the request.
    customer_id = input("Enter customer ID: ")
    # Gets the service ID selected by the customer.
    service_id = input("Enter service ID: ")
    # Gets the requested booking date.
    date = input("Enter date (DD-MM-YYYY): ")
    # Gets the requested booking time.
    time = input("Enter time (HH:MM): ")

    # Opens the services file to read the available car wash services.
    file = open("services.txt", "r")

    # Keeps track of whether the selected service was found.
    service_found = False

    # Reads each record from the file.
    for line in file:
        # Removes extra spaces and the newline character.
        line = line.strip()
        # Separates the record into individual fields.
        parts = line.split("|")

        # Checks whether the service ID matches the entered ID.
        if parts[0] == service_id:
            # Confirms that the service exists.
            service_found = True

    file.close()

    # Stops the request if the service does not exist.
    if not service_found:
        print("Service not found.")
        return
       
    # Stores the available booking time slots.
    slots = [
        "09:00", "09:45", "10:30", "11:15",
        "12:00", "12:45", "13:30", "14:15",
        "15:00", "15:45", "16:30", "17:15",
        "18:00", "18:45", "19:30", "20:15"
    ]

    # Checks whether the entered time is a valid booking slot.
    if time not in slots:
        print("Invalid time.")
        return

    # Keeps track of whether the selected date and time are already booked.
    booked = False

    # Opens the bookings file to check for an existing booking.
    booking_file = open("bookings.txt", "r")

    # Reads each booking record from the file.
    for line in booking_file:
        # Removes extra spaces and the newline character.
        line = line.strip()
        # Separates the record into individual fields.
        parts = line.split("|")

        # Checks whether another booking uses the same date and time.
        if parts[3] == date and parts[4] == time:
            # Marks the selected time as booked.
            booked = True

    booking_file.close()

    # Stops the request if the selected time is already booked.
    if booked:
        print("This time is already booked.")
        return

    # Starts the booking number from 1000.
    booking_number = 1000

    file = open("bookings.txt", "r")

    # Reads each record from the file.
    for line in file:
        # Removes extra spaces and the newline character.
        line = line.strip()
        # Separates the record into individual fields.
        parts = line.split("|")

        number = int(parts[0][1:])

        # Keeps the highest booking number found.
        if number > booking_number:
            booking_number = number

    file.close()

    # Increases the number to create the next booking ID.
    booking_number = booking_number + 1
    # Creates the new booking ID using the B prefix.
    booking_id = "B" + str(booking_number)

    status = "Pending"        

    # Creates the booking record before saving it to the file.
    data = [booking_id, customer_id, service_id, date, time, status]

    # Adds the new booking record to the bookings file.
    append_regestrations("bookings.txt", data)

    print("Booking requested successfully.")
    print("Booking ID:", booking_id)


# Display the customer's service history
def view_service_history():
    # Gets the customer ID for the request.
    customer_id = input("Enter customer ID: ")

    # Keeps track of whether the customer ID exists.
    customer_found = False

    # Opens the customers file to validate the customer.
    customer_file = open("customers.txt", "r")

    for line in customer_file:
        # Removes extra spaces and the newline character.
        line = line.strip()
        # Separates the record into individual fields.
        parts = line.split("|")

        # Checks whether the entered customer ID exists.
        if parts[0] == customer_id:
            customer_found = True

    customer_file.close()

    # Stops the function if the customer does not exist.
    if not customer_found:
        print("Customer not found.")
        return

    file = open("bookings.txt", "r")

    # Reads each record from the file.
    for line in file:
        # Removes extra spaces and the newline character.
        line = line.strip()
        # Separates the record into individual fields.
        parts = line.split("|")

        if parts[1] == customer_id:
            print("Booking ID:", parts[0])
            print("Customer ID:", parts[1])
            print("Current Date:", parts[3])
            print("Current Time:", parts[4])
            print("Status:", parts[5])

            if parts[5] == "Extension Requested":
                print("Requested Date:", parts[6])
                print("Requested Time:", parts[7])

    file.close()


# Display the customer's invoices
def view_invoices():
    # Gets the customer ID for the request.
    customer_id = input("Enter customer ID: ")

    # Keeps track of whether the customer ID exists.
    customer_found = False

    # Opens the customers file to validate the customer.
    customer_file = open("customers.txt", "r")

    for line in customer_file:
        # Removes extra spaces and the newline character.
        line = line.strip()
        # Separates the record into individual fields.
        parts = line.split("|")

        # Checks whether the entered customer ID exists.
        if parts[0] == customer_id:
            customer_found = True

    customer_file.close()

    # Stops the function if the customer does not exist.
    if not customer_found:
        print("Customer not found.")
        return

    # Opens the bookings file to check for an existing booking.
    booking_file = open("bookings.txt", "r")

    # Creates a list to store the customer booking IDs.
    customer_bookings = []

    # Reads each booking record from the file.
    for line in booking_file:
        # Removes extra spaces and the newline character.
        line = line.strip()
        # Separates the record into individual fields.
        parts = line.split("|")

        if parts[1] ==customer_id:
            # Stores the booking ID for matching with payment records.
            customer_bookings.append(parts[0])

    booking_file.close()

    # Opens the payments file to find invoices linked to the customer bookings.
    payment_file = open("payments.txt", "r")

    for line in payment_file:
        # Removes extra spaces and the newline character.
        line = line.strip()
        # Separates the record into individual fields.
        parts = line.split("|")

        # Checks whether the payment belongs to one of the customer bookings.
        if parts[1] in customer_bookings:
            # Displays the invoice and payment information.
            print("Payment ID:", parts[0])
            print("Booking ID:", parts[1])
            print("Amount:", parts[2])
            print("Date:", parts[3])
            print("Status:", parts[4])
            print("--------------------")

    payment_file.close()              


# Request an extension for an existing booking
def request_extension():
    # Gets the customer ID for the request.
    customer_id = input("Enter customer ID: ")
    # Gets the booking ID that the customer wants to extend.
    booking_id = input("Enter booking ID: ")
    # Gets the new date requested by the customer.
    new_date = input("Enter new date (DD-MM-YYYY): ")
    # Gets the new time requested by the customer.
    new_time = input("Enter new time (HH:MM): ")

    file = open("bookings.txt", "r")

    # Creates a list to store all booking records.
    bookings = []
    # Keeps track of whether the selected booking was found.
    booking_found = False

    # Reads each record from the file.
    for line in file:
        # Removes extra spaces and the newline character.
        line = line.strip()
        # Separates the record into individual fields.
        parts = line.split("|")

        # Checks whether the booking belongs to the selected customer.
        if parts[0] == booking_id and parts[1] == customer_id:
            # Changes the booking status to show that an extension was requested.
            parts[5] = "Extension Requested"
            parts.append(new_date)
            parts.append(new_time)
            booking_found = True

        # Stores the booking record in the list.
        bookings.append(parts)

    file.close()

    if not booking_found:
        print("Booking not found.")
        return

    # Opens the bookings file in write mode to save the updated records.
    file = open("bookings.txt", "w")

    # Writes all booking records back to the file.
    for booking in bookings:
        # Joins the fields back together using the | separator.
        line = "|".join(booking) + "\n"
        file.write(line)

    file.close()

    print("Extension request submitted successfully.")
    print("Booking ID:", booking_id)


# Display the customer menu
def customer_menu():

    # Keeps the customer menu running until the customer chooses Exit.
    while True:
        print("\n==== Customer Menu ====")
        print("1. View Services")
        print("2. View Available Slots")
        print("3. Request Booking")
        print("4. View Service History")
        print("5. View Invoices")
        print("6. Request Extension")
        print("7. Exit")  

        choice = input("Enter your choice: ")  

        if choice == "1":
            view_services()

        elif choice == "2":
            view_available_slots()

        elif choice == "3":
            request_booking()

        elif choice == "4":
            view_service_history()

        elif choice == "5":
            view_invoices()

        elif choice == "6":
            request_extension()

        # Ends the customer menu when the customer chooses Exit.
        elif choice == "7":
            print("Goodbye.")
            break

        # Handles an invalid menu option.
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")



#view_services()     
#view_available_slots() 
#request_booking()    
#view_service_history()
#view_invoices()
#request_extension()
customer_menu()
