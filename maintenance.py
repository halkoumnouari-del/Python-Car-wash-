from Regestration import read_regestrations, append_regestrations

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


# Runs the menu only when this file is opened directly (not when main.py imports it)
if __name__ == "__main__":
    maintenance_menu()