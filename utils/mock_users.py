from faker import Faker
from models import User

def split_name(username: str, sep):
    surnames =  ["Sr.", "Sra.", "Dr.", "Dra.", "Srta."]
    name_splitted = username.split(sep)
    return [elem for elem in name_splitted if elem not in surnames]


def create_fake_users():
    faker_inst =  Faker(['pt-BR'])
    users = []

    for _ in range(1, 101):
        username = f"{faker_inst.first_name()} {faker_inst.last_name()}"

        name_splitted = split_name(username, " ")

        first_name = name_splitted[0]
        last_name = name_splitted[len(name_splitted) - 1]

        email =  f"{first_name.lower()}.{last_name.lower()}@{faker_inst.domain_name()}"

        birth_date = faker_inst.date_of_birth()

        fake_user = User(first_name, last_name, email, birth_date)

        users.append(fake_user)

    return users