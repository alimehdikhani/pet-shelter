class AnimalNotFoundError(Exception):
    pass


class DuplicateAnimalError(Exception):
    pass


class AnimalAlreadyAdoptedError(Exception):
    pass


class MaximumAdoptionReachedError(Exception):
    pass