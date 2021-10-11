EMPLOYEES = [
    {
        "name": "Eric \"Macho Man\" Taylor",
        "email": "macho@man.com",
    },
    {
        "name": "Alexander Schroyer",
        "email": "alex@geemail.com",
    },
    {
        "name": "Kylie Postlethwaite",
        "email": "kylie@geemail.com",
    },
    {
        "name": "Brandon De Leon",
        "email": "brandon@geemail.com",
    },
    {
        "name": "Pauly D",
        "email": "pauly@geemail.com",
    }
]

def get_all_employees():
    return EMPLOYEES


# Function with a single parameter
def get_single_employee(id):
    # Variable to hold the found animal, if it exists
    requested_employee = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee