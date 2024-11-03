class Human:
    def __init__(self):
        self.name = ''
        self.gender = ''
        self.age = 0
        self._say = "Hi"

    def say(self):
        print(self._say)


class Moomin(Human):
    def __init__(self):
        super().__init__()
        self.name = 'moomin'
        self.age = 27
        self.gender = "Man"

    def say(self):
        self._say = "Hello"
        print(self._say)


me = Moomin()
me.say()

# Hello