from random import randint

class Client(object):
    def __init__(self, name):
        self.name = name
        self.credit = randint(1000, 9000)
        self.creditCard = False
        self.cash = False

    def onCreditCard(self):
        self.creditCard = True
        return self.creditCard

    def onCash(self):
        self.cash = True
        return self.cash

    def getCredit(self):
        return self.credit

    def status(self):
        return (self.cash or self.creditCard)


class Manager(object):
    def __init__(self, client):
        self.managed_client = client
        print('Managing Client: {}'.format(self.managed_client.name))

    def send_client_on(self, typee):
        if typee in ['cash', 'creditCard']:
            if typee == 'cash':
                print('Sending client: {} on accountant'.format(self.managed_client.name))
                self.managed_client.onCash()
            else:
                print('Sending client: {} on manager'.format(self.managed_client.name))
                self.managed_client.onCreditCard()
        else:
            print('Can\'t send client on: {}, it\'s not a valid option!'.format(typee))

    def refuse_client(self, offer):
        print('The credit of the client is: {}'.format(self.managed_client.getCredit()))
        if offer > self.managed_client.getCredit():
            print('Saying we agree {}'.format(self.managed_client.name))
        else:
            print('Saying No to the offer, as the client {} is too expensive!'.format(self.managed_client.name))

if __name__ == '__main__':
    credit = Client('Daniel')
    mgr = Manager(credit)

    # mgr.send_player_on('vacation')
    mgr.send_client_on('creditCard')

    mgr.refuse_client(3000)
