# class Laptop
class Laptop:
    # init method
    def __init__(self, company, model):
        # self
        self.company = company
        self.model = model

# creating instances for the class Laptop
laptop_one = Laptop('Lenevo', 'ideapad320')
laptop_two = Laptop('Dell', 'Vostro2348')
# printing the properties of the instances
print(f"Laptop One: {laptop_one.company}")
print(f"Laptop Two: {laptop_two.model}")
