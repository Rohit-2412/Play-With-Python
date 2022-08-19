tuition_fees = 196000
hostel_fees = 60000
mess_fees = 30000
scholarship = 0
marks = eval(input("Enter percentage obtained in 12th class: "))

if 70 <= marks <= 80:
    scholarship = 30
elif 81 <= marks <= 90:
    scholarship = 40
else:
    scholarship = 50
total_fees = 0
admission_year = int(input("Enter year in you are taking admission: "))
for i in range(admission_year - 2020):
    tuition_fees += tuition_fees * 0.05
    hostel_fees += hostel_fees * 0.10
    mess_fees += mess_fees * 0.08
    total_fees = tuition_fees + hostel_fees + mess_fees

total_fees -= total_fees * scholarship / 100
print(f"Total cost for the student will be {total_fees}")
