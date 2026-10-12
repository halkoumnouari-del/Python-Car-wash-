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
         
                
     elif service == 3 :
         print ("Welcome to Crystal Car Accountant")
        

     elif service == 4 :
         print("Welcome to Crystal Car Customer")
         
     elif service == 5 :
         print("Welcom to Crystal Car Deataling service")
         
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
        service_delet = input("Which service would u delet : ") 
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

service_menu()