from enum import Enum


class Certificate(Enum):
    """
    Different kinds of certificates the player must be asked to present while playing the game
    """
    GRANDMA = "grandma"
    INTEGRITY = "integrity"
    BIRTH = "birth"
    ID = "id"
    PASSPORT = "passport"
    TAX = "tax"
    PORT = "port"
    HAIRCUT = 'haircut'

    @staticmethod
    def list():
        return [Certificate.GRANDMA,
                Certificate.INTEGRITY,
                Certificate.BIRTH,
                Certificate.ID,
                Certificate.PASSPORT,
                Certificate.TAX,
                Certificate.PORT,
                Certificate.HAIRCUT]

