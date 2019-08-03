from enum import Enum


class Certificate(Enum):
    """
    A class that holds all the certificate that a player can hold in the gane
    """
    # Grandma marriage certificate, get at (8,0)
    GRANDMA = "grandma"

    # Integrity certificate, get at (5,2)
    INTEGRITY = "integrity"

    # Birth certificate, get at (11,3)
    BIRTH = "birth"

    # ID certificate, get at (1,4)
    ID = "id"

    # Passport picture , get at (8,4)
    PASSPORT = "passport"

    # Tax certificate , get at (0,1)
    TAX = "tax"

    # Port entrance certificate , get at (6,7)
    PORT = "port"

    # Get a haircut certificate
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

