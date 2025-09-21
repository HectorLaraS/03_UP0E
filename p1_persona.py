class person:
    def __init__(self, name:str = "Jon", last:str="Doe"):
        self._name: str = name
        self._last: str = last

    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self, value:str):
        self._name = value

    @property
    def Last(self):
        return self._last

    @Last.setter
    def Last(self, value:str):
        self._last = value

    def __str__(self):
        return f"{self.Name} {self.Last}"
