
import random

secret_number = random.randint(1, 10)

try:
    user = int(input("Enter your number (1-10): "))

    if user < 1 or user > 10:
        print("❌ Invalid guess! Enter a number from 1 to 10.")

    elif user == secret_number:
        print("🏆 CORRECT! YOU BEAT THE SYSTEM!")

    elif user < secret_number:
        print("📉 TOO LOW! Guess higher!")

    else:
        print("📈 Too high, bro! Bring that number down!")

except ValueError:
    print("❌ Bro, enter a whole number from 1 to 10!")
