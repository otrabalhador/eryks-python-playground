class Animal(object):
    def __init__(self, peso=None, altura=None, largura=None):
        self.peso = peso
        self.altura = altura
        self.largura = largura

    @property
    def area(self):
        return self.altura * self.largura


class Pet(Animal):
    def __init__(self, peso=None, altura=None, largura=None, name=None, species=None, ):
        self.name = name
        self.species = species

        Animal.__init__(self, peso=peso, altura=altura, largura=largura)

    def get_name(self):
        return self.name

    def get_species(self):
        return self.species

    def __str__(self):
        return "%s is a %s" % (self.name, self.species)


class Dog(Pet):
    def __init__(self, name, chases_cats):
        Pet.__init__(self, name, "Dog")
        self.chases_cats = chases_cats

    def chases_cats(self):
        return self.chases_cats

    def __str__(self):
        return Pet.__str__(self)
        # return "%s. Chases cats: %s" % (self.__str__(), 1)

