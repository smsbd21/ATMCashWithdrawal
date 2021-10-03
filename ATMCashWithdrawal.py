print("******************** Welcome to SMS Bank ********************")
attempt_count, my_pin, my_balance = 0, 1234, 180000
atm_pin = int(input("Enter Your 4 Digit ATM PIN And Press Enter-:\n"))
# Check ATM Pin For 3 Attempt
while True:
    attempt_count += 1
    if atm_pin == my_pin:
        break
    elif attempt_count == 3:
        print("Exceeded Maximum Attempts- Try Again")
        exit()
    else:
        atm_pin = int(input("Enter Your 4 Digit ATM PIN And Press Enter\n"))

# When ATM Pin Passed
attempt_count = 0
list_of_notes = [1000, 500, 200, 100]
min_notes = list_of_notes[len(list_of_notes)-1]
withdrawal_amount = int(input("Enter Your Withdrawal Amount At Multiplier of 100 And Press Enter-:\n"))
# Notes Count Logic
while True:
    attempt_count += 1
    if (withdrawal_amount % min_notes) == 0 and withdrawal_amount <= 20000:
        if withdrawal_amount <= my_balance:
            break
        elif attempt_count == 3:
            print("Exceeded Maximum Attempts- Try Again")
            exit()
    elif attempt_count == 3:
        print("Exceeded Maximum Attempts- Try Again")
        exit()
    else:
        print("Amount is Not Valid. No Divisible of 100 And Less Than\n")
        withdrawal_amount = int(input("Please Enter The Amount Again-:\n"))

starting_index = 0
# Logic For Currency Note Choice
for i in range(0, len(list_of_notes)):
    if withdrawal_amount >= list_of_notes[i]:
        starting_index = i # currency_value = list_of_notes[cur]
        break

# Get Notes Count
#currency_value = list_of_notes[0]
# #starting_index = list_of_notes.index(currency_value)
for indx in range(starting_index, len(list_of_notes)):
    if withdrawal_amount == 0:
        break
    else:
        choice_value = list_of_notes[indx]
        quotient, remainder_value = divmod(withdrawal_amount, choice_value)
        calculated_amount = quotient * choice_value # Amount = count * value
        withdrawal_amount = remainder_value
        print(f'Count {choice_value}৳ Notes is {quotient} value remaining is {withdrawal_amount}')