class System:
    def __init__(self, **props):
        fields = [
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
        for field in fields:
            self[field] = props.get(field, None)
