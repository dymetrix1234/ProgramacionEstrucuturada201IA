from faker import Faker

faker = Faker('es_MX')
ciudades_la = []
for _ in range(5):
    ciudades_la.append(faker.city())

print("\n--- DATASET DE CIUDADES GENERADO")
for i in range(len(ciudades_la)):
    print(f"Registro{i+1}: {ciudades_la[i]}")