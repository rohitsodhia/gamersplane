from model import Model


class System(Model):

    _fields = [
        "id",
        "name",
        "sortName",
        "publisher",
        "genres",
        "basics",
        "hasCharSheet",
        "enabled",
        "createdOn",
        "updatedOn",
    ]
