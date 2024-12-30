import argparse
import random

def generate_test(n, m, t):
    """
    Gera um teste com:
    - n fábricas
    - m países
    - t crianças
    """
    factories = []
    countries = []
    children = []

    # Gerar fábricas
    for i in range(1, n + 1):
        country_id = random.randint(1, m)
        stock = random.randint(1, 100)  # Stock máximo aleatório
        factories.append((i, country_id, stock))

    # Gerar países
    for j in range(1, m + 1):
        export_max = random.randint(1, 200)  # Exportações máximas
        min_gifts = random.randint(1, 50)   # Presentes mínimos
        countries.append((j, export_max, min_gifts))

    # Gerar crianças
    for k in range(1, t + 1):
        country_id = random.randint(1, m)
        num_toys = random.randint(1, min(5, n))  # Cada criança pede brinquedos de 1 a 5 fábricas
        toy_factories = random.sample(range(1, n + 1), num_toys)
        children.append((k, country_id, toy_factories))

    # Construir o input
    output = [f"{n} {m} {t}"]

    # Adicionar fábricas
    for factory in factories:
        output.append(" ".join(map(str, factory)))

    # Adicionar países
    for country in countries:
        output.append(" ".join(map(str, country)))

    # Adicionar crianças
    for child in children:
        child_id, country_id, toy_factories = child
        output.append(f"{child_id} {country_id} " + " ".join(map(str, toy_factories)))

    return "\n".join(output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gerador de casos de teste para o projeto.")
    parser.add_argument("n", type=int, help="Número de fábricas")
    parser.add_argument("m", type=int, help="Número de países")
    parser.add_argument("t", type=int, help="Número de crianças")
    args = parser.parse_args()

    # Gerar e imprimir o caso de teste
    print(generate_test(args.n, args.m, args.t))
