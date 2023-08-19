class User:
    def __init__(self, name: str, email: str, age: int):
        self._name = str(name)
        self._email = str(email)
        self._age = int(age)

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def age(self):
        return self._age

    @property
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
