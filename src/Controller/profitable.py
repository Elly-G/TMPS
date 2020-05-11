from __future__ import annotations
from abc import ABC, abstractmethod, abstractclassmethod

class Profilable(ABC):
    @abstractmethod
    def getProfile(self) -> str:
        pass

class SimpleProfile(Profilable):
    def getProfile(self) -> str:
        return "Simple Profile"

class PremiumProfile(Profilable):
    def getProfile(self) -> str:
        return "Premium Profile"

class AccountCreator:
    accountData = 'account data'

    def __init__(self, profile: Profilable) -> None:
        self.profile = profile

    def setAccountData(self, data):
        self.accountData = data

    def getAccountData(self) -> str:
        return self.accountData

class Account(AccountCreator):
    def operationImplementation(self) -> str:
        return "concrete Account"

def client_code(account: AccountCreator) -> None:
    print("This client has an account with " + account.getAccountData() + " with " + account.profile.getProfile())

def main():
    profile = SimpleProfile()
    premium = PremiumProfile()
    account = Account(premium)
    another_account = Account(profile)
    print(another_account.profile.getProfile())
    print(account.profile.getProfile())
#     from client side
    client_code(account)

if __name__ == "__main__":
    main()
