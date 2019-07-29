from enum import Enum


class Certificate(Enum):
    GRANDMA = "grandmas_marriage_certificate"
    INTEGRITY = "integrity_certificate"
    BIRTH = "birth_certificate"
    ID = "id"
    RABIES = "rabies_certificate"
    PASSPORT = "passport_photo"
    MILITARY = "military_pad"
    TAX = "tax_payment_authorization"
    PORT = "entrance_to_port"
    GLASSES = "glasses"
    HAT = "hat"
    HAIRCUT = 'haircut'
    PACKAGE = "package"


certificates = [Certificate.GRANDMA,
                Certificate.INTEGRITY,
                Certificate.BIRTH,
                Certificate.ID,
                Certificate.RABIES,
                Certificate.PASSPORT,
                Certificate.MILITARY,
                Certificate.TAX,
                Certificate.PORT,
                Certificate.GLASSES,
                Certificate.HAT,
                Certificate.HAIRCUT,
                Certificate.PACKAGE]