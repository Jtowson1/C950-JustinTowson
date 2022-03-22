# Package class for transforming the csv information into an actual class

class Packages:

    # Constructor for the package class

    def __init__(self, packageid, address, city, state, zipcode, deadline, weight, special):
        self.special = special
        self.weight = weight
        self.deadline = deadline
        self.zip = zipcode
        self.state = state
        self.city = city
        self.address = address
        self.packageId = packageid
