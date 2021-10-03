my_atm_pin, attempt_count, my_account_balance = 1234, 0, 180000
print("******************** Welcome to SMS Bank ********************")
atm_pin = int(input("Enter Your 4 Digit ATM PIN And Press Enter\n"))
# Check ATM Pin For 4 Attempt
while True:
    attempt_count += 1
    if atm_pin == my_atm_pin:
        break
    elif attempt_count == 4:
        print("Exceeded Maximum Attempts- Try Again")
        exit()
    atm_pin = int(input("Enter Your 4 Digit ATM PIN And Press Enter\n"))

# When ATM Pin Passed
attempt_count = 0
withdrawal_amount = int(input("Enter Your Amount To Withdrawal And Press Enter-:\n"))
currency_value = int(input("Enter Maximum Currency Value-:\n"))
list_of_choice = [1000, 500, 200, 100, 50]

# Note Count Logic
while True:
    attempt_count += 1
    if (withdrawal_amount % 50) == 0 and withdrawal_amount <= 20000 and withdrawal_amount <= my_account_balance:
        break
    elif attempt_count == 4:
        print("Exceeded Maximum Attempts- Try Again")
        exit()

    print("Amount is Not Valid. No Divisible of 50 And Less Than\n")
    withdrawal_amount = int(input("Please Enter The Amount Again-:\n"))

# Logic For Currency Note Choice
starting_index = list_of_choice.index(currency_value)
# Get Notes Count
for indx in range(starting_index, len(list_of_choice)):
    if withdrawal_amount == 0:
        break
    choice_value = list_of_choice[indx]
    quotient, remainder_value = divmod(withdrawal_amount, choice_value)
    calculated_amount = quotient * choice_value # Amount = count * value
    withdrawal_amount = remainder_value
    print(f'Count {choice_value} $ Notes is {quotient} value remaining is {withdrawal_amount}')

