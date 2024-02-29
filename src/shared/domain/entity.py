
class Entity:

    def __eq__(self, other):
        return vars(self) == vars(other)

    def __str__(self):
        return "prueba"