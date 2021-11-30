phone_list = ["98-777-653", "98-742-644", "34-855-326", "34-25-629", "34-489-115", "72-999-563", "9-321-459",
              "72-654-121", "72-4-694", "72-255-313", "98-111-323", "98-433-14", "34-577-342", "98-323-000",
              "98-202-666", "34-5435-454", "34-515-633"]

valid_numbers = []
wrong_numbers = []     

for i in phone_list:
    if len(i) > 10 or len(i) < 10:
        wrong_numbers.append(i) 
    else:
        valid_numbers.append(i) 

print("Valid numbers are: ", valid_numbers)
print("Wrong numbers are: ", wrong_numbers)

help_list = []
list_of_area_codes = []

for j in valid_numbers:
    x = j.rpartition("-")[0]
    help_list.append(x)

for k in help_list:
    y = k.rpartition("-")[0]
    list_of_area_codes.append(y) 

print("Area codes are: ", list_of_area_codes)
print("Valid numbers without area codes are: ", [l[3:] for l in valid_numbers[:]])
print(len(valid_numbers))

unique_area_codes = list(dict.fromkeys(list_of_area_codes))

print("Unique area codes are: ", unique_area_codes)  

valid_numbers_new = [w[:2] for w in valid_numbers[:]]

print("There are", valid_numbers_new.count('98'), "phone numbers in list which are ends 98.") 
print("There are", valid_numbers_new.count('34'), "phone numbers in list which are ends 34.")
print("There are", valid_numbers_new.count('72'), "phone numbers in list which are ends 72.")