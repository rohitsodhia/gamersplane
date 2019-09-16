from systems.models import System


def generate_systems_sql(basic=False):
    if basic:
        fields = "`id`, `name`, `sortName`"
    else:
        fields = ", ".join(f"`{field}`" for field in System.get_fields())
    return f"SELECT {fields} FROM systems WHERE enabled = 1 ORDER BY `sortName`"
