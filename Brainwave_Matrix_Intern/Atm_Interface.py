class Account:
    def __init__(self, user_id, pin, balance=0):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.transactions = []

    def check_pin(self, pin):
        return self.pin == pin

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(('Deposit', amount))
        return f"Deposit successful! Current balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance!"
        else:
            self.balance -= amount
            self.transactions.append(('Withdraw', amount))
            return f"Withdrawal successful! Current balance: {self.balance}"

    def get_transaction_history(self):
        return self.transactions if self.transactions else "No transactions available."

    def transfer(self, target_account, amount):
        if amount > self.balance:
            return "Insufficient balance!"
        else:
            self.withdraw(amount)
            target_account.deposit(amount)
            return f"Transfer successful! Current balance: {self.balance}"


class ATM:
    def __init__(self):
        self.accounts = {}
        self.language = "English"

    def set_language(self):
        print("Choose Language:")
        print("1. English")
        print("2. हिंदी")
        choice = input("Enter your choice: ")
        if choice == '1':
            self.language = "English"
        elif choice == '2':
            self.language = "Hindi"
        else:
            print("Invalid choice, defaulting to English.")
            self.language = "English"

    def create_account(self, user_id, pin, balance=0):
        self.accounts[user_id] = Account(user_id, pin, balance)

    def verify_pin(self, account):
        pin_prompt = "Please re-enter your PIN to confirm: " if self.language == "English" else "कृपया लेन-देन की पुष्टि के लिए अपना पिन दोबारा दर्ज करें: "
        pin = input(pin_prompt)
        return account.check_pin(pin)

    def run(self):
        while True:
            # Welcome message and card insertion
            print("\nWelcome to the ATM!")
            input("Please insert your card to proceed (press Enter): ")

            # Language selection
            self.set_language()

            # After language selection
            welcome_msg = "Welcome to the ATM Interface!" if self.language == "English" else "एटीएम इंटरफ़ेस में आपका स्वागत है!"
            print(welcome_msg)

            # User operations
            user_id_msg = "Enter your user ID: " if self.language == "English" else "अपना यूजर आईडी दर्ज करें: "
            user_id = input(user_id_msg)

            if user_id in self.accounts:
                account = self.accounts[user_id]

                while True:
                    operation_msg = (
                        "\n1. Transaction History\n2. Withdraw\n3. Deposit\n4. Transfer\n5. Check Balance\n6. Quit"
                        if self.language == "English"
                        else "\n1. लेन-देन का इतिहास\n2. निकासी\n3. जमा\n4. स्थानांतरण\n5. बैलेंस जांचें\n6. बाहर निकलें"
                    )
                    operation_prompt = "Choose an operation: " if self.language == "English" else "एक ऑपरेशन चुनें: "
                    print(operation_msg)
                    operation = input(operation_prompt)

                    if operation == '1':  # Transaction history
                        print(account.get_transaction_history())
                    elif operation == '2':  # Withdraw
                        withdraw_msg = "Enter amount to withdraw: " if self.language == "English" else "निकासी के लिए राशि दर्ज करें: "
                        amount = float(input(withdraw_msg))
                        if self.verify_pin(account):
                            print(account.withdraw(amount))
                        else:
                            print("Invalid PIN. Transaction cancelled.")
                    elif operation == '3':  # Deposit
                        deposit_msg = "Enter amount to deposit: " if self.language == "English" else "जमा करने के लिए राशि दर्ज करें: "
                        amount = float(input(deposit_msg))
                        if self.verify_pin(account):
                            print(account.deposit(amount))
                        else:
                            print("Invalid PIN. Transaction cancelled.")
                    elif operation == '4':  # Transfer
                        target_id_msg = "Enter target user ID: " if self.language == "English" else "लक्ष्य उपयोगकर्ता आईडी दर्ज करें: "
                        target_id = input(target_id_msg)
                        transfer_msg = "Enter amount to transfer: " if self.language == "English" else "स्थानांतरण के लिए राशि दर्ज करें: "
                        amount = float(input(transfer_msg))
                        if target_id in self.accounts:
                            if self.verify_pin(account):
                                print(account.transfer(self.accounts[target_id], amount))
                            else:
                                print("Invalid PIN. Transaction cancelled.")
                        else:
                            print("Target account not found." if self.language == "English" else "लक्ष्य खाता नहीं मिला।")
                    elif operation == '5':  # Check balance
                        balance_msg = f"Your current balance is: {account.balance}" if self.language == "English" else f"आपकी वर्तमान बैलेंस है: {account.balance}"
                        print(balance_msg)
                    elif operation == '6':  # Quit
                        print("Returning to card insertion screen..." if self.language == "English" else "कार्ड डालने की स्क्रीन पर लौट रहे हैं...")
                        break
                    else:
                        print("Invalid operation!" if self.language == "English" else "अमान्य ऑपरेशन!")
            else:
                print("Invalid user ID." if self.language == "English" else "अमान्य उपयोगकर्ता आईडी।")


# Create an ATM instance and test accounts
atm = ATM()
atm.create_account('user1', '1234', 1000)
atm.create_account('user2', '5678', 500)

# Run the ATM
atm.run()
