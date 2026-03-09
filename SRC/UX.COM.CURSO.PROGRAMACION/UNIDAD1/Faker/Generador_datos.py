#importar la librerria de faker
from faker import Faker

faker = Faker('es_MX')

print(f'nombre: {faker.name()}')
print(f'direccion: {faker.address()}')
print(f'email: {faker.email()}')
print(f'numero de telefono: {faker.phone_number()}')
