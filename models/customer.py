class Customer():
    """errorfix"""
    def __init__(self, id, name, address, location_id, email = "", password = ""):
        self.id = id
        self.name = name
        self.address = address
        self.location_id = location_id
        self.email = email
        self.password = password
