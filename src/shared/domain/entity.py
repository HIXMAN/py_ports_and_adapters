
class Entity:

    def __eq__(self, other):
        return vars(self) == vars(other)