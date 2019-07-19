import random

class Package:
    packages = [250, 330, 540, 750, 850,  1050, 1320, 2150, 3680]

    def get_package(self):
        package = random.choice(self.packages)
        self.packages.remove(package)
        return package

