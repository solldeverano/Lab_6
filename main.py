from typing import List

class IActt:
    def attach_customer(self, customer):
        pass

    def detach_customer(self, customer):
        pass

    def notify_customers(self):
        pass


class AccountProxy(IActt):
    def __init__(self):
        self.customers = []
        self.balance = 0

    def attach_customer(self, customer):
        self.customers.append(customer)

    def detach_customer(self, customer):
        self.customers.remove(customer)

    def notify_customers(self):
        for customer in self.customers:
            customer.notify(self)

    def deposit(self, amount):
        self.balance += amount
        self.notify_customers()


class Customer:
    def notify(self, account_proxy):
        pass

    def withdraw(self, amount):
        pass


class BankCustomer(Customer):
    def __init__(self, name):
        self.name = name

    def notify(self, account_proxy):
        print(f"{self.name}, you have received a money transfer. Your new balance is: {account_proxy.balance}")
        self.withdraw(50)

    def withdraw(self, amount):
        print(f"{self.name} is withdrawing {amount} from the account.")


def main():
    account = AccountProxy()

    customer1 = BankCustomer("John")
    customer2 = BankCustomer("Alice")

    account.attach_customer(customer1)
    account.attach_customer(customer2)

    account.deposit(1000)

    account.detach_customer(customer1)
    account.deposit(500)


if __name__ == "__main__":
    main()
