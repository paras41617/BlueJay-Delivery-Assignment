import pandas as pd

# Load the Excel file into a DataFrame
file_name = "Assignment_Timecard.xlsx"
df = pd.read_excel(file_name)

# Assuming that the columns are named as follows, adjust if necessary
# You may need to adjust the column names based on your actual data
# Columns: Position ID, Position Status, Timecard Hours, Pay Cycle Start Date, Pay Cycle End Date, Employee Name, File Number

# Initialize variables to track consecutive days and previous row information
consecutive_days = 1
prev_employee = None
prev_date = None
prev_hours = None

cons_seven_days = set()
ten_hours_between_shifts = set()
fourteen_hours_single_shift = set()

# Iterate through the DataFrame and analyze the data
for index, row in df.iterrows():
    employee = row['Employee Name']
    # print("employee : ", employee)
    position_id = row['Position ID']
    # print("position id : ", position_id)
    time_str = str(row['Timecard Hours (as Time)'])
    timecard_hours = 0.0
    if(time_str != "nan"):
        # Split the string into hours and minutes
        hours, minutes = map(int, time_str.split(":"))

        # Calculate the float value
        timecard_hours = hours + (minutes / 60.0)

        # print("timecard : ", type(timecard_hours))

    if(timecard_hours > 14):
        fourteen_hours_single_shift.add(employee + " " + position_id)

    # Check if it's the same employee as the previous row
    if employee == prev_employee:
        # Check for consecutive days
        consecutive_days += 1
        if(consecutive_days >= 7):
            cons_seven_days.add(employee + " " + position_id)
        # Check for less than 10 hours between shifts but greater than 1 hour
        prev_hours += timecard_hours
        if(prev_hours <10 and prev_hours > 1):
            ten_hours_between_shifts.add(employee + " " + position_id)
    # If it's a different employee, reset consecutive days count
    else:
        consecutive_days = 1

    # Update previous row information
    prev_employee = employee
    prev_hours = timecard_hours

print("worked for 7 consecutive days", end=' ')
print(" ")
print(cons_seven_days)
print(" ")
print("has less than 10 hours of time between shifts but greater than 1 hour", end=' ')
print(" ")
print(ten_hours_between_shifts)
print("worked for more than 14 hours in a single shift", end=' ')
print(" ")
if(len(fourteen_hours_single_shift) == 0):
    print("No Entry who has worked for more than 14 hours in a single shift ")
else:
    print(fourteen_hours_single_shift)
# Close the Excel file
# Assuming you've opened it with 'with' to ensure proper closing
# with pd.ExcelFile(file_name) as xls:
#     df = pd.read_excel(xls)

# Additional assumptions:
# - The Excel file is well-formatted with the specified column names.
# - Date format in the 'Pay Cycle Start Date' column is consistent and can be compared.
# - Timecard Hours is in the format "X.XX hours" and can be converted to a numeric format.
# - The program assumes that you have installed the 'pandas' library.

