class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if isinstance(new_age, int) & (new_age > 0) & (new_age < 120):
            self._age = new_age

    def get_name(self):
        return self._name

    def __str__(self):
        return 'Person[' + str(self._name) + '] is ' + str(self._age)


if __name__ == '__main__':
    person = Person('John', 54)
    person._name = "Lautaro"
    person._age = -1
    print(person)
    print(person.get_age())
    print(person.get_name())
