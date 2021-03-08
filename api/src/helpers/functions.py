import inflect

infe = inflect.engine()


def pluralize(word):
    return infe.plural(word)
