class Product:

    pass
class Car(Product):
    def __init__(self, model, volume, price):
        self.model = model
        self.volume = volume
        self.price = price

    def display_info(self):
        print('Model:', self.model, '\tVolume:', self.volume, '\tPrice:', self.price)

prod = Car('Peugeot', 20, 15.23)
prod.display_info()