# Reads data from text file
def read_regestrations (filename):
    regestrations = []
    file = open(filename , "r")
    for line in file :
        line = line.strip()
        if line != "":
            # Splits text by | into a list
            regestrations.append(line.split("|"))
    # Closes the file
    file.close()
    return regestrations

# Appends a new record to the file
def append_regestrations(filename, data):
    #Joins list items with | and adds a new line
    line = "|".join(data) + "\n"
    # Opens file in append mode
    file = open(filename, "a")
    # Writes the line and closes the file
    file.write(line)
    file.close()

# Displays main system menu
def menu ():
    # Loops through menu options until user chooses to exit
    while True :
     print("Welcom to Crystal Car Managment")
     print("1.System Administrator")
     print("2.Booking Officer")
     print("3.Accountant")
     print("4.Customer")
     print("5.Detailing Staff")
     print("6.Exit")
     service =int(input("Which service would you choose : "))
   
     if service == 1 :
         print("Welcome to Crystal Car Administrator")
         service_menu()
                
     elif service == 2 :
         print("Welcom to Crystal Car Booking Officer")
         booking_officer_menu()
                
     elif service == 3 :
         print ("Welcome to Crystal Car Accountant")
         accountant()

     elif service == 4 :
         print("Welcome to Crystal Car Customer")
         customer_menu()
     elif service == 5 :
         print("Welcom to Crystal Car Deataling service")
         maintenance_menu()
     elif service == 6 :
         print("Thank you for choose Crystal Car")
         break


 # Manages service administrative tasks     
def service_menu ():
    print("1.Veiw services")
    print("2.Add Service")
    print("3.Modify Service")
    print("4.Delet service")
    print("5.Back to Main Menu")
    service_update = int(input("Hi service admin what do u want : "))
     # Loops until admin chooses to return to main menu
    while service_update <= 5:
     # Option 1: Displays all available services
     if service_update == 1:
        data = read_regestrations("services.txt")
        for x in data:
           print(*x)
        print("1.Veiw services")
        print("2.Add Service")
        print("3.Modify Service")
        print("4.Delet service")
        print("5.Back to Main Menu")
        service_update = int(input("Hi service admin what do u want : "))
     # Option 2: Adds a new service record
     elif service_update == 2:
        code = input("Enter service code : ")
        name = input("Enter service name : ")
        price = (input("Enter service price : "))
        duration = (input("Enter service duration : "))
        new_service = [code,name,price,duration]
        append_regestrations("services.txt", new_service)
        print("Service has been added succesfully ")
        print("1.Veiw services")
        print("2.Add Service")
        print("3.Modify Service")
        print("4.Delet service")
        print("5.Back to Main Menu")
        service_update = int(input("Hi service admin what do u want : "))
     # Option 3: Modifies an existing service record
     elif service_update == 3:
        data = read_regestrations("services.txt")
        code =input ("Wich service you would modifiy it (Enter service code ) : ")
        found = False
        for service in data:
            if service[0] == code:
                service[1] = input("Enter the new service : ")
                service[2] = input("Enter the price : ")
                service[3] = input("Enter the duration : ")
                found = True
                break

        if found:
            file = open("services.txt", "w")
            for item in data:
                line = "|".join(item) + "\n"
                file.write(line)
            file.close()
            print("Service has been modifiy succesfully")
        else:
            print("Service not found")

        print("1.Veiw services")
        print("2.Add Service")
        print("3.Modify Service")
        print("4.Delet service")
        print("5.Back to Main Menu")
        service_update = int(input("Hi service admin what do u want : "))
     # Option 4: Deletes a service from the file
     elif service_update == 4:
        data = read_regestrations("services.txt")
        service_delet = input("Which service would u delet (Enter the code): ") 
        found = False
        for service in data:
           if service[0]== service_delet:
              data.remove(service)
              found = True
              break
      # Rewrites the file without the deleted service  
        if found:
                file = open("services.txt", "w")
                for item in data:
                    line = "|".join(item) + "\n"
                    file.write(line)
                file.close()
                print("Service has been deleted succesfully")
        else:
                print("Service not found")
        print("1.Veiw services")
        print("2.Add Service")
        print("3.Modify Service")
        print("4.Delet service")
        print("5.Back to Main Menu")        

        service_update = int(input("Hi service admin what do u want : "))
         # Option 5: Exits to main menu
     elif service_update == 5:
        break

def accountant():
     # Stores the loyalty discount rate for eligible cutomers.
     Loyalty_Discount = 0.10
     print("<<<~Accountant Menu~>>>")
     print("1- Check Customer Bookings & Loyalty Discount")
     print("2- Update Payment Status")
     print("3- Add New Payment")
     print("4- Monthly Financial Report & Outstanding Payments")
     print("5- Back to Main Menu")
     choice = 0
     while choice <= 5:
      choice = int(input("Enter your choice: "))
      if choice == 1:
         # Initializes the booking counter for the selected customer.
         booking_number = 0
          # Opens the bookings file to count the customer's bookings.
         file=open("bookings.txt", "r")
         # Gets the customer ID to identify the customer's bookings.
         customerID = input("Enter a customer_id:")

         # Reads each booking record, removes extra spaces and the newline character, and separates the record into fields.
         for line in file:
            line = line.strip()
            parts = line.split("|")
            customer_id = parts[1]

            # Checks whether the booking belongs to the selected customer and increases the booking count.
            if customer_id == customerID:
                booking_number = booking_number + 1
            # Displays the total number of bookings for the selected customer.        
         print(booking_number)

      elif choice == 2: 
         # Opens the payments file to read and update payment records.
         file=open("payments.txt", "r")
         # Initializes the income and outstanding payment totals.
         income = 0
         Outstanding = 0
         # Gets the payment ID that needs to be updated.
         payment_id = input("Enter payment_id:")
         # Gets the new payment status.
         new_status = input("Enter the new_status:")
         # Creates an empty list to store the updated payment records.
         save = []
         # Cleans each payment record and separates it into individual fields.
         for line in file:
            line = line.strip()
            print(line)
            parts= line.split("|")
            # Checks whether the current payment record matches the entered payment ID.
            if payment_id == parts[0]:
                # Gets the payment ID, booking ID, and amount from the selected payment record.
                payment_id=parts[0]
                booking_id=parts[1]
                amount=float(parts[2])
                # Opens the bookings file to find the customer linked to the selected booking.
                booking_file = open("bookings.txt", "r")
                # Reads each booking record and separates it into individual fields.
                for booking_line in booking_file:
                    booking_line = booking_line.strip()
                    booking_parts = booking_line.split("|")

                    # Finds the customer ID linked to the selected booking.
                    if booking_id == booking_parts[0]:
                        customer_id = booking_parts[1]
                # Closes the bookings file after finding the customer ID.
                booking_file.close()

                # Resets the booking counter before counting the customer's bookings.
                booking_number = 0
                # Opens the bookings file to count all bookings for the selected customer.
                booking_file = open("bookings.txt", "r")

                # Reads each booking record to count bookings for the selected customer.
                for booking_line in booking_file:
                    booking_line = booking_line.strip()
                    booking_parts = booking_line.split("|")

                    # Checks whether the booking belongs to the selected customer.
                    if booking_parts[1] == customer_id:
                        # Increases the booking count for the selected customer.
                        booking_number = booking_number + 1
                # Closes the bookings file after counting the customer's bookings.
                booking_file.close()
                # Checks whether the customer has exactly five bookings to qualify for the loyalty discount.
                if booking_number == 5:
                    # Calculates the loyalty discount and subtracts it from the payment amount.
                    discount_amount = amount * Loyalty_Discount
                    final_amount = amount - discount_amount
                    amount = final_amount

                payment_date=parts[3]
                payment_status=parts[4]
                # Updates the payment status with the new status entered by the user.
                parts[4] = new_status
                # Updates the payment amount with the final amount.
                parts[2] = str(amount)
                # Rebuilds the payment record using the updated fields.
                line = "|".join(parts)
                # Adds the payment amount to the appropriate total based on the payment status.
                if parts[4] == "Paid":
                    income = income + amount
                if parts[4] == "Outstanding":
                    Outstanding = Outstanding + amount
            # Stores the updated payment record in the list.
            save.append(line)
         # Closes the payments file after reading all records.
         file.close()
         # Opens the payments file in write mode to save the updated records.
         file = open("payments.txt", "w")
         # Writes all saved payment records back to the payments file.
         for data in save:
            # Writes each payment record on a new line.
            file.write(data + "\n")
         # Closes the payments file after saving the updated records.
         file.close()
         # Displays the total income and outstanding payment amounts.
         print(income)
         print(Outstanding)

      elif choice == 3: 
        
         # Gets the payment ID for the new payment.
         payment_id = input("Enter paymentID:")
         # Gets the booking ID linked to the payment.
         booking_id = input("Enter BookingID:")

         # Gets the payment amount from the user. 
         amount = float(input("Enter Amount:"))

         print(amount)
         # Gets the payment date and payment status from the user.
         payment_date = input("Enter paymentDate:")
         payment_status = input("Enter paymentStatus:")
         # Converts the payment amount to text for storing in the file.
         amount = str(amount)
         # Creates the new payment record.
         data = [payment_id, booking_id, amount, payment_date, payment_status]
         # Adds the new payment record to the payments file.
         append_regestrations("payments.txt", data)

      elif choice == 4: 
         # Initializes the income and outstanding payment totals.
         income = 0
         Outstanding = 0

         # Opens the payments file to calculate the financial summary.
         file = open("payments.txt", "r")
         # Gets the month and year to calculate the financial summary for.
         target_month = input("Enter the month and year:")
         # Initializes the monthly income total.
         monthly_income = 0
         
         # Reads each payment record, cleans it, and separates it into fields for processing.
         for line in file:
            line = line.strip()
            if line != "":
                parts = line.split("|")
                # Gets the payment date from the payment record.
                payment_date = parts[3]
                # Extracts the month and year from the payment date.
                month = payment_date[0:7]

                # Checks whether the payment belongs to the selected month and year.
                if target_month == month:
                    # Converts the payment amount to a number and adds it to the monthly income.
                    amount = float(parts[2])
                    monthly_income = monthly_income + amount

                # Adds the payment amount to the appropriate total based on the payment status.
                amount = float(parts[2])
                if parts[4] == "Paid":
                    income = income + amount
                if parts[4] == "Outstanding":
                    Outstanding = Outstanding + amount
         # Closes the payments file after calculating the financial summary.
         file.close()
         # Displays the monthly income, total income, and outstanding payment amounts.
         print(monthly_income)
         print(income)
         print(Outstanding)

         file = open("payments.txt", "r")
         # Reads each payment record, cleans it, and separates it into fields.
         for line in file:
            line = line.strip()
            parts = line.split("|")
            # Checks whether the payment is outstanding.
            if parts[4] == "Outstanding":
                # Displays the outstanding payment record.
                print(line)
      elif choice == 5:
          break

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

# Reads a file and returns its records (empty list if the file does not exist yet)
def read_file(filename):
    try:
        return read_regestrations(filename)
    except FileNotFoundError:
        return []
    except OSError:
        print("Error: could not read", filename)
        return []


# Saves all the equipment back into maintenance.txt
def save_equipment(equipment):
    try:
        file = open("maintenance.txt", "w")
        for item in equipment:
            file.write("|".join(item) + "\n")
        file.close()
        return True
    except OSError:
        print("Error: could not save maintenance.txt")
        return False


# Saves one line in activity_log.txt so there is a record of daily operations
def log_activity(date, action, details):
    try:
        append_regestrations("activity_log.txt", [date, action, details])
    except OSError:
        print("Warning: could not write to activity_log.txt")


# Asks for text that is not empty and has no | (| separates the data in the files)
def get_text(message):
    while True:
        text = input(message + " (0 = back): ").strip()
        if text == "0":
            return None
        if text == "" or "|" in text:
            print("Invalid input. It cannot be empty or contain |")
        elif len(text) > 30:
            print("Too long. Please use 30 characters or less.")
        else:
            return text


# Shows a numbered list and returns the option the user picks
def choose_option(title, options):
    print("\n" + title)
    for i in range(len(options)):
        print(str(i + 1) + ".", options[i])
    while True:
        choice = input("Select an option (0 = back): ").strip()
        if choice == "0":
            return None
        if choice.isdigit() and int(choice) >= 1 and int(choice) <= len(options):
            return options[int(choice) - 1]
        print("Invalid choice. Enter a number from 1 to", len(options))


# Checks that the date is real and written as YYYY-MM-DD (e.g. 2026-10-08)
def is_valid_date(date):
    if len(date) != 10 or date[4] != "-" or date[7] != "-":
        return False
    year = date[0:4]
    month = date[5:7]
    day = date[8:10]
    if not year.isdigit() or not month.isdigit() or not day.isdigit():
        return False

    year = int(year)
    month = int(month)
    day = int(day)
    if year < 2000 or month < 1 or month > 12:
        return False

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    max_day = days_in_month[month - 1]
    # February has 29 days in a leap year
    if month == 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        max_day = 29
    return day >= 1 and day <= max_day


# Asks for a date until it is valid and not before the 'earliest' date
# Returns None if the user types 0 to go back
def get_date(message, earliest=""):
    while True:
        date = input(message + " YYYY-MM-DD (0 = back): ").strip()
        if date == "0":
            return None
        if not is_valid_date(date):
            print("Invalid date. Example: 2026-10-08")
        elif earliest != "" and date < earliest:
            # YYYY-MM-DD dates can be compared as text
            print("The date cannot be before", earliest)
        else:
            return date


# 1. Display all the equipment
def view_equipment():
    equipment = read_file("maintenance.txt")
    if len(equipment) == 0:
        print("No equipment found.")
        return

    print("\nID    Equipment                       Status            Last Maintenance")
    for item in equipment:
        if len(item) == 4:
            print(item[0].ljust(6) + item[1].ljust(32) + item[2].ljust(18) + item[3])


# 2. Add new equipment (the ID is created automatically: M01, M02, M03 ...)
def add_equipment():
    equipment = read_file("maintenance.txt")

    name = get_text("\nEnter equipment name")
    if name is None:
        return
    for item in equipment:
        if len(item) == 4 and item[1].lower() == name.lower():
            print("This equipment already exists.")
            return

    status = choose_option("Current status:",
                           ["Good", "Serviced", "Needs Repair", "Under Repair", "Out of Service"])
    if status is None:
        return
    date = get_date("Last maintenance date")
    if date is None:
        return

    # new ID = biggest ID number + 1
    biggest = 0
    for item in equipment:
        if len(item) == 4 and item[0][1:].isdigit():
            if int(item[0][1:]) > biggest:
                biggest = int(item[0][1:])
    new_id = "M" + str(biggest + 1).zfill(2)

    # save the whole list again instead of adding to the end of the file,
    # so the new record is always written on its own line
    equipment.append([new_id, name, status, date])
    if not save_equipment(equipment):
        return

    log_activity(date, "EQUIPMENT", new_id + " " + name + " added")
    print(name, "added successfully with ID", new_id)


# 3. Update the maintenance status of a piece of equipment
#    The change is saved in maintenance.txt and recorded in maintenance_log.txt
def update_status():
    equipment = read_file("maintenance.txt")
    if len(equipment) == 0:
        print("No equipment found.")
        return
    view_equipment()

    # keep asking until the user enters an ID that exists
    selected = None
    while selected is None:
        equipment_id = get_text("\nEnter equipment ID")
        if equipment_id is None:
            return
        for item in equipment:
            if len(item) == 4 and item[0].lower() == equipment_id.lower():
                selected = item
        if selected is None:
            print("Equipment not found. Check the ID in the list above.")

    print("\nSelected:", selected[1], "| Current status:", selected[2])

    work_type = choose_option("Type of maintenance:", ["Repair", "Service", "Inspection"])
    if work_type is None:
        return
    new_status = choose_option("New status:",
                               ["Good", "Serviced", "Needs Repair", "Under Repair", "Out of Service"])
    if new_status is None:
        return

    # the new date cannot be before the last maintenance date
    last_date = ""
    if is_valid_date(selected[3]):
        last_date = selected[3]
    date = get_date("Maintenance date", last_date)
    if date is None:
        return
    note = get_text("Short note (e.g. replaced hose)")
    if note is None:
        return

    old_status = selected[2]
    selected[2] = new_status
    selected[3] = date
    if not save_equipment(equipment):
        return

    try:
        append_regestrations("maintenance_log.txt",
                             [selected[0], work_type, old_status, new_status, date, note])
    except OSError:
        print("Warning: could not save the maintenance log.")

    log_activity(date, "MAINTENANCE", selected[0] + " " + old_status + " -> " + new_status)
    print(selected[1], "updated to", new_status, "successfully.")


# 4. Display the maintenance log (history of all maintenance work)
def view_maintenance_log():
    logs = read_file("maintenance_log.txt")
    if len(logs) == 0:
        print("No maintenance records yet.")
        return

    print("\nID    Type        Old Status        New Status        Date        Note")
    for log in logs:
        if len(log) == 6:
            print(log[0].ljust(6) + log[1].ljust(12) + log[2].ljust(18)
                  + log[3].ljust(18) + log[4].ljust(12) + log[5])


# 5. Maintenance summary report
def maintenance_report():
    equipment = read_file("maintenance.txt")
    logs = read_file("maintenance_log.txt")

    # only count lines that have the right number of columns
    valid_equipment = []
    for item in equipment:
        if len(item) == 4:
            valid_equipment.append(item)
    valid_logs = []
    for log in logs:
        if len(log) == 6:
            valid_logs.append(log)

    print("\n===== Maintenance Summary Report =====")
    print("Total equipment:", len(valid_equipment))
    for status in ["Good", "Serviced", "Needs Repair", "Under Repair", "Out of Service"]:
        count = 0
        for item in valid_equipment:
            if item[2] == status:
                count = count + 1
        print("  " + status + ":", count)

    print("Total maintenance records:", len(valid_logs))
    for work_type in ["Repair", "Service", "Inspection"]:
        count = 0
        for log in valid_logs:
            if log[1] == work_type:
                count = count + 1
        print("  " + work_type + ":", count)


def maintenance_menu():
    while True:
        print("\n===== Maintenance Staff Menu =====")
        print("1. View Equipment")
        print("2. Add New Equipment")
        print("3. Update Equipment Status")
        print("4. View Maintenance Log")
        print("5. Maintenance Summary Report")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_equipment()
        elif choice == "2":
            add_equipment()
        elif choice == "3":
            update_status()
        elif choice == "4":
            view_maintenance_log()
        elif choice == "5":
            maintenance_report()
        elif choice == "6":
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


menu()