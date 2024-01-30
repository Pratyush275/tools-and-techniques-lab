paisa_amount = int(input("Enter the amount in paisa: "))

rupees = paisa_amount // 100
paise = paisa_amount % 100

print(f"{paisa_amount} paisa is equivalent to {rupees} rupees and {paise} paise.")