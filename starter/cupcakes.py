from abc import ABC, abstractmethod

import csv

from pprint import pprint

class Cupcake(ABC):
    size = 'regular'
    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []

    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)
        pass

    @abstractmethod
    def calculate_price(self, num):
        return num * self.price
    
class Mini(Cupcake):
    size = "mini"

    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []

    def calculate_price(self, num):
        return super().calculate_price(num)

class Large(Cupcake):
    size = "large"

    def calculate_price(self, num):
        return super().calculate_price(num)
    
class Regular(Cupcake):

    def calculate_price(self, num):
        return super().calculate_price(num)

def read_csv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        fieldname = 'sprinkles'
        for row in reader:
            pprint(row)

def write_new_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
            else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})

def append_new_cupcake(file, cupcakes):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
            else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})


def get_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader


def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
    return None

def add_cupcake_dictionary(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)

def delete_cupcake_dictionary(file, cupcake):
    cupcakes = get_cupcakes(file)

    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for cup_cake in cupcakes:
            if cup_cake != cupcake:
                writer.writerow(cup_cake)
    return

if __name__ == "__main__":
    read_csv("sample.csv")


    frost = Regular('Frosted Cupcake', 3.00, 'Regular', 'Strawberry', None)
    frost.add_sprinkles('Red', 'Green', 'Blue', 'White')

    mini_frost = Mini('Frosted Cupcake', 3.00, 'Regular', 'Strawberry')
    mini_frost.add_sprinkles('Red')

    large_frost = Large('Chocolate', 2.5, 'Chocolate', 'Vanilla', 'Strawberry')
    large_frost.add_sprinkles('Green', 'Blue')

    cupcake_list = [
        frost, 
        mini_frost,
        large_frost
    ]

    write_new_csv("sample2.csv", cupcake_list)

    print("............")
    read_csv("sample2.csv")