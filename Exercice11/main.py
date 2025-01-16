class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Dépôt de {amount} effectué.")
        else:
            print("Le montant doit être positif.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Retrait de {amount} effectué.")
        else:
            print("Retrait échoué : montant invalide ou solde insuffisant.")

    def display_balance(self):
        print(f"Titulaire du compte : {self.account_holder}, Solde : {self.balance}")

# Example usage
account = BankAccount("Alice", 1000)
account.display_balance()
account.deposit(500)
account.withdraw(200)
account.display_balance()
account.withdraw(1500)  # Should fail due to insufficient balance
