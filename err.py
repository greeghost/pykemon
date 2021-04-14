"""This is a simple module defining a few runtime errors linked to Pykemon."""


class _PykemonError(Exception):
    pass


class InvalidPokemonName(_PykemonError):
    """Error thrown when a request for a Pokemon was made, but the Pokemon is not found.

    Usage : raise(InvalidPokemonName(name))
    """

    def __init__(self, value):
        self.invalid_name = value

    def __str__(self):
        return f"{self.invalid_name} is not a known pokemon"
