#Import the append_regestrations function to append text files.
from Regestration import append_regestrations

#Import the read_regestrations function to open and read text files.
from Regestration import read_regestrations

#This function create a menu allowing the user to navigate through different option.
def booking_officer_menu():
    while True:      #Show the different menu options.
        print("\n=== BOOKING OFFICER MENU ===")
        print("1. Register Customer")
        print("2. Create Booking")
        print("3. View Bookings")
        print("4. View Customer History")
        print("5. Cancel Booking")
        print("6. Reschedule Booking")
        print("7. Manage Requests")
        print("8. Back")
        choice = input("Enter choice: ") #Run the correct function that fulfill the user input.
        if choice == "1":
            register_customer()
        elif choice == "2":
            create_booking()
        elif choice == "3":
            view_bookings()
        elif choice == "4":
            view_customer_history()
        elif choice == "5":
            cancel_booking()
        elif choice == "6":
            reschedule_booking()
        elif choice == "7":
            manage_requests()
        elif choice == "8":
            break
        else:
            print("Invalid choice.")       #Tell the user that the input is invalid

#This function allow the user to register a new customer in the database.
def register_customer():
    while True:  #Get the information about the new customer.
        customer_id = input("Enter Customer ID (0 to go back): ")
        if customer_id == "0":#Allow the user to get back to the previous menu if he enter 0
            return
        customers = read_regestrations("customers.txt")
        for customer in customers:
            if customer[0] == customer_id:#Stop the process if the ID already exist, to avoid error.
                print("Customer ID already exists.")
                return
        #Reject all the empty input and send an explanation message.
        if customer_id != "":
            break
        print("Customer ID cannot be empty.")
    while True:
        name = input("Enter Customer Name: ")
        if name != "":
            break
        print("Name cannot be empty.")
    while True:
        phone = input("Enter Phone Number: ")
        if phone != "":
            break
        print("Phone Number cannot be empty.")
    data = [customer_id, name, phone]
    append_regestrations("customers.txt", data) #Convert and save the new Data.
    print("Customer registered successfully.")

#This function automatically generate a booking ID while performing a booking.
def generate_booking_id():
    bookings = read_regestrations("bookings.txt")
    booking_count = len(bookings)#Generate a booking ID based on the booking count starting from 1001 
    new_id = "B" + str(booking_count + 1001)
    return new_id

#This function allow the user to create and add a new booking to the database.
def create_booking():
    booking_id = generate_booking_id()# Call the function to assign a booking ID.
    while True:#Get and check(Not empty) the booking's information.
        customer_id = input("Enter Customer ID (0 to go back): ")
        if customer_id == "0":
            return
        if customer_id != "":
            break
        print("Customer ID cannot be empty.")
    while True:
        service_id = input("Enter Service ID: ")
        if service_id != "":
            break
        print("Service ID cannot be empty.")
    while True:
        date = input("Enter Date (YYYY-MM-DD): ")
        if date != "":
            break
        print("Date cannot be empty.")
    while True:
        time = input("Enter Time (HH:MM): ")
        if time != "":
            break
        print("Time cannot be empty.")
    status = "Confirmed"
    data = [           #Convert the data in other to save them.
        booking_id,
        customer_id,
        service_id,
        date,
        time,
        status
    ]
    append_regestrations("bookings.txt", data)# Update the Database.
    print("Booking created successfully.")
    print("Booking ID:", booking_id)

#This function shows all the all the bookings from the database.
def view_bookings():
    bookings = read_regestrations("bookings.txt")#Call the function to read the data from the Text file.
    for booking in bookings: #Convert and show the data in a better way.
        print("Booking ID:", booking[0])
        print("Customer ID:", booking[1])
        print("Service ID:", booking[2])
        print("Date:", booking[3])
        print("Time:", booking[4])
        print("Status:", booking[5])
        print()

#This function reads and shows a customer's booking history from the database.
def view_customer_history():
    customer_id = input("Enter Customer ID (0 to go back): ")#Get the right customer.
    if customer_id == "0": #(Reject invalid input)
        return
    bookings = read_regestrations("bookings.txt")
    found = False
    for booking in bookings:
        if booking[1] == customer_id: #Look for matching ID
            print("Booking ID:", booking[0])#Convert and show the data in a better way.
            print("Service ID:", booking[2])
            print("Date:", booking[3])
            print("Time:", booking[4])
            print("Status:", booking[5])
            print()
            found = True
    if found == False:
        print("No booking history found.")

#This function allow the user to cancel a booking.
def cancel_booking():
    booking_id = input("Enter Booking ID (0 to go back): ")#Get the right booking.
    if booking_id == "0":
        return
    bookings = read_regestrations("bookings.txt")#Go through all the bookinds.
    found = False
    for booking in bookings:  #Go through all the bookinds.
        if booking[0] == booking_id:   #Look for matching ID.
            if booking[5] == "Cancelled": #reject if the booking already cancelled.  
                print("Booking already cancelled.")
                return
            booking[5] = "Cancelled"#Update the booking status.
            found = True
    if found:
        file = open("bookings.txt", "w") #Convert and Save the updates in the database.
        for booking in bookings:
            line = "|".join(booking)
            file.write(line + "\n")
        file.close()
        print("Booking cancelled successfully.")
    else:
        print("Booking not found.")

#This function allow the user to reshedule a booking.
def reschedule_booking():
    booking_id = input("Enter Booking ID (0 to go back): ")#Get the right booking.
    if booking_id == "0":
            return
    while True: #Get the new date and new time.
        new_date = input("Enter New Date (YYYY-MM-DD): ")
        if new_date != "":
            break
        print("Date cannot be empty.")
    while True:
        new_time = input("Enter New Time (HH:MM): ")
        if new_time != "":
            break
        print("Time cannot be empty.")
    bookings = read_regestrations("bookings.txt")
    found = False
    for booking in bookings:  #Go through all the bookinds.
        if booking[0] == booking_id: #Look for matching ID.
            if booking[5] == "Cancelled":#reject if the booking is cancelled.
                print("Cannot reschedule a cancelled booking.")
                return
            booking[3] = new_date   #Update the booking status.
            booking[4] = new_time
            found = True
    if found:
        file = open("bookings.txt", "w")  #Convert and Save the updates in the database.
        for booking in bookings:
            line = "|".join(booking)
            file.write(line + "\n")
        file.close()
        print("Booking rescheduled successfully.")
    else:
        print("Booking not found.")

#This function manages request from customers.
def manage_requests():
    print("\n=== MANAGE REQUESTS ===")   #Open a sub-menu asking the user which kind of request he would like to manage.
    print("1. Booking Requests")
    print("2. Extension Requests")
    print("3. Back")
    choice = input("Enter choice: ")  #Call a function based on the selected option.
    if choice == "1":
        manage_booking_requests()
    elif choice == "2":
        manage_extension_requests()
    elif choice == "3":
        return
    else:
        print("Invalid choice.")
#This function manages booking request from customers.
def manage_booking_requests():
    bookings = read_regestrations("bookings.txt")
    found = False
    print("\n=== PENDING BOOKING REQUESTS ===")
    for booking in bookings: # Show all the bookings with the pending status.
        if booking[5] == "Pending": #Look for matches.
            found = True
            print(
                booking[0], "|",
                booking[1], "|",
                booking[2], "|",
                booking[3], "|",
                booking[4]
            )
    if not found:  #Show a message if there is no pending request.
        print("No pending booking requests.")
        return
    booking_id = input("\nEnter Booking ID to manage (0 to go back): ")# Ask the user to choose the right booking.
    if booking_id == "0":
        return
    for booking in bookings:
        if booking[0] == booking_id and booking[5] == "Pending": #Look for matching.
            decision = input("Approve (A) or Reject (R): ")#Ask the user whether he wants to appove or reject.
            if decision.upper() == "A": #Use upper so the user can enter A or a.
                booking[5] = "Confirmed"
            elif decision.upper() == "R":
                booking[5] = "Rejected"
            else:
                print("Invalid choice.") #Show message for invalid input.
                return
            save_bookings(bookings)
            print("Request updated successfully.")
            return
    print("Pending request not found.") #Show message is no match was found.
#This function manages extension request from customers.
def manage_extension_requests():
    bookings = read_regestrations("bookings.txt")
    found = False
    print("\n=== EXTENSION REQUESTS ===")
    for booking in bookings:  # Show all the bookings with the Extension request status.
        if booking[5] == "Extension Requested":
            found = True
            print("\nBooking ID:", booking[0])
            print("Customer ID:", booking[1])
            print("Current Date:", booking[3])
            print("Current Time:", booking[4])
            print("Requested Date:", booking[6])  #Show the requested time and day.
            print("Requested Time:", booking[7])
    if not found:   #Show message if there is no extension request.
        print("No extension requests.")
        return
    booking_id = input("\nEnter Booking ID to manage (0 to go back): ")  #Ask the user to choose the right booking.
    if booking_id == "0":
        return
    for booking in bookings:
        if booking[0] == booking_id and booking[5] == "Extension Requested":#Look for matching.
            decision = input("Approve (A) or Reject (R): ")#Ask the user whether he wants to appove or reject.
            if decision.upper() == "A":#Use upper so the user can enter A or a.
                booking[3] = booking[6] #Update the booking.
                booking[4] = booking[7]
                booking[5] = "Confirmed"
                booking.pop() #pop is required since Booking[6]&[7] become useless.
                booking.pop()
            elif decision.upper() == "R":
                booking[5] = "Confirmed"
                booking.pop()
                booking.pop()
            else:
                print("Invalid choice.") #Show error message.
                return
            save_bookings(bookings) #Call the function to Save data in the database.
            print("Extension request updated successfully.")
            return
    print("Extension request not found.")
#This function update changes in the booking database.
def save_bookings(bookings):
    file = open("bookings.txt", "w")  #Update or change data in the booking database.
    for booking in bookings:
        line = "|".join(booking)
        file.write(line + "\n")
    file.close()
booking_officer_menu()