from enum import Enum


class Certificate(Enum):
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

