class Player:
    money = 1500
    has_grandmas_marriage_certificate = False
    has_integrity_certificate = False
    has_birth_certificate = False
    has_id = False
    has_rabies_certificate = False
    has_passport_photo = False
    has_military_pad = False
    has_tax_payment_authorization = False
    has_entrance_to_port = False
    has_glasses = False
    has_hat = False
    has_package = False
    package_cost = 0
    come_back_spots = []

    def pay(self, cost, is_surprise = False):
        if self.money >= cost:
            self.money -= cost
            return True

        if is_surprise:
            self.money -= min(self.money, cost)
            return True

        return False

    def receive_money(self, amount):
        self.money += amount
        return True
