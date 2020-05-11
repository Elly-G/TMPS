# singleton
class Exchanger(object):

    def __new__(exchangeEuro):         # metoda _new_ creaza obiecte noi
        if not hasattr(exchangeEuro, 'eur'):   #metoda hasattr verifica daca exista atributul 'eur' in obiectul specificat
            exchangeEuro.eur = super(Exchanger, exchangeEuro).__new__(exchangeEuro)
        return exchangeEuro.eur

ex = Exchanger()      # obiectul ex este creat de metoda _new_, care mai sus este verificat daca exista 
print("Euro exchange was created", ex)

ex1 = Exchanger()
print("Euro exchange exists", ex1)
