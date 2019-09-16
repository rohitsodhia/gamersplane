class Model:

    _fields = []
    _values = {}

    def __init__(self, **props):
        for key, value in props.items():
            setattr(self, key, value)

    def __setattr__(self, name, value):
        if name not in self._fields:
            return
        self._values[name] = value

    def __getattr__(self, name):
        if name in ["_fields", "_values"]:
            return getattr(self, name)
        try:
            return self._values[name]
        except AttributeError:
            raise

    @classmethod
    def get_fields(cls):
        return cls._fields
