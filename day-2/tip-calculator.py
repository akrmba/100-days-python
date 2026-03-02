print("=" * 50)
print("Welcome to Tip Calculator")
print("=" * 50)

# bill = float(input("what was the total of the bill?\n"))
# tip_option = input("How much tip to give? 10, 12 or 15\n")

# if tip_option in ["10", "12", "15"]: 
#     split_value = float(input("how many people to split\n"))
#     a = bill * (int(tip_option)/100)
#     print(a)
#     each_person = (bill + a)/split_value
#     print(f"{each_person:.2f}")
# else:
#     print("invalid entry")

#while loop 
# customer = 0

# while customer == 0:
#     bill = float(input("what was the total of the bill?\n"))
#     tip_option = input("How much tip to give? 10, 12 or 15\n")
#     if tip_option == "10" or tip_option == "12" or tip_option == "15":
#         split_value = float(input("how many people to split\n"))
#         a = bill * (int(tip_option)/100)
#         print(a)
#         each_person = (bill + a)/split_value
#         print(f"{each_person:.2f}")  
#     else:
#         print("invalid entry")

#while inside while

customer = 0

while customer == 0:
    bill = float(input("what was the total of the bill?\n"))
    wrong_entry = 0
    while wrong_entry == 0:
        tip_option = input("How much tip to give? 10, 12 or 15\n")
        if tip_option == "10" or tip_option == "12" or tip_option == "15":
            split_value = float(input("how many people to split\n"))
            a = bill * (int(tip_option)/100)
            print(a)
            each_person = (bill + a)/split_value
            print(f"{each_person:.2f}")
            break
        else:
            print("invalid entry")
    water = input("do you want to continue? y for yes; n for no")
    if water != "y":
        break
