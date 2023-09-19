class User:
    def __init__(self, first_name, last_name, email, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.birth_date = birth_date
        self.active = True

    def __str__(self) -> str:
        return f"First Name: {self.first_name}, Last Name: {self.last_name}, Email: {self.email}"