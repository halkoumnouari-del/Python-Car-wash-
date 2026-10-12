# Imports the shared function used to add a new payment record to the file.
from Regestration import append_regestrations

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

accountant()