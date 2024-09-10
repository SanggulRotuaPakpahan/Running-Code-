class Bird:
    def fly(self):
        raise NotImplementedError("Subclasses must implement this method")

class Eagle(Bird):
    def fly(self):
        return "Eagle is flying high!"


class Penguin(Bird):
    def fly(self):
        return "Penguins can't fly, they swim!"


def make_bird_fly(bird: Bird):
    print(bird.fly())


eagle = Eagle()
penguin = Penguin()


make_bird_fly(eagle)   
make_bird_fly(penguin)  
