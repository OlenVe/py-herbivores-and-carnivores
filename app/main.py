
class Animal:
    alive = []

    def __init__(self, name: str,
                 health: int = 100,
                 hidden: bool = False
                 ) -> None:
        self.name = name
        self. health = health
        self.hidden = hidden
        type(self).alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self) -> None:
        if not self.hidden:
            self.hidden = True
        else:
            self.hidden = False


class Carnivore(Animal):

    def bite(self, target: Herbivore) -> None:
        if not isinstance(target, Carnivore) and target.hidden is False:
            target.health = target.health - 50
        if target.health <= 0:
            Animal.alive.remove(target)
