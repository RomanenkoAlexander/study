from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = float(weight)
        self.category = category

    def __str__(self):
        return(f'{self.name}, {self.weight}, {self.category}')


class Shop:
    __file_name = 'products.txt'

    def __init__(self):
        pass

    def get_products(self):
        file = open(Shop.__file_name, 'r')
        content = file.read()
        return content

    def add(self, *products):
        Shop.get_products(self)

        for i in products:
            # print(str(i))
            if str(i) in Shop.get_products(self):
                print(f'Продукт {str(i)} уже есть в магазине')
            else:
                file = open(Shop.__file_name, 'a')
                file.write(f'{str(i)}\n')
                file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
