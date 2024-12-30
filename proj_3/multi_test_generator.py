"""
Este script gera múltiplos casos de teste para o projeto 3.
Os testes são guardados em ficheiros de texto no diretório "tests".
Os argumentos da linha de comando são:
- num_tests: Número de testes a serem gerados.                          (default: 10)
- n: Número inicial de fábricas.                                        (default: 10)
- m: Número inicial de países.                                          (default: 5)
- t: Número inicial de crianças.                                        (default: 20)
- c_n: Crescimento de fábricas por teste.                               (default: 5)
- c_m: Crescimento de países por teste.                                 (default: 2)
- c_t: Crescimento de crianças por teste.                               (default: 10)
- output_dir: Diretório para salvar os testes gerados.                  (default: "tests")
- scale_factor: Fator de escala para ajustar estoques e exportações.    (default: 1.2)
"""
import argparse
import os
import random

def generate_test(n, m, t, scale_factor=20):
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
        # Escalar f_max proporcional ao número de crianças
        max_stock = round(((t * 2) / n) * random.uniform(0.5, scale_factor))
        factories.append((i, country_id, max_stock))

    # Gerar países
    for j in range(1, m + 1):
        # Escalar p_max e p_min proporcional ao número de fábricas e crianças
        export_max = round((n * random.uniform(1, scale_factor)))
        min_gifts = round((t / m) * random.uniform(0.8, 1))
        countries.append((j, export_max, min_gifts))

    # Gerar crianças
    for k in range(1, t + 1):
        country_id = random.randint(1, m)
        num_toys = random.randint(1, min(5, n))  # Cada criança pede brinquedos de 1 a 5 fábricas
        toy_factories = random.sample(range(1, n + 1), num_toys)    # Escolher fábricas aleatórias
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

def generate_multiple_tests(num_tests, n, m, t, c_n, c_m, c_t, output_dir, scale_factor=1.2):
    os.makedirs(output_dir, exist_ok=True)  # Criar diretório se não existir

    for i in range(1, num_tests + 1):
        # Gerar o caso de teste atual
        test_case = generate_test(n, m, t, scale_factor)

        # Salvar o teste num ficheiro
        test_file = os.path.join(output_dir, f"test_{i}.txt")
        with open(test_file, "w") as f:
            f.write(test_case)

        print(f"Teste {i} gerado: {test_file}")

        # Atualizar os valores de n, m e t com os coeficientes
        n += c_n
        m += c_m
        t += c_t

if __name__ == "__main__":
    # Configurar argumentos da linha de comando
    parser = argparse.ArgumentParser(description="Gerar múltiplos casos de teste para o projeto.")
    parser.add_argument("num_tests", type=int, help="Número de testes a serem gerados.")
    parser.add_argument("--n", type=int, default=10, help="Número inicial de fábricas.")
    parser.add_argument("--m", type=int, default=5, help="Número inicial de países.")
    parser.add_argument("--t", type=int, default=20, help="Número inicial de crianças.")
    parser.add_argument("--c_n", type=int, default=5, help="Crescimento de fábricas por teste.")
    parser.add_argument("--c_m", type=int, default=2, help="Crescimento de países por teste.")
    parser.add_argument("--c_t", type=int, default=10, help="Crescimento de crianças por teste.")
    parser.add_argument("--output_dir", type=str, default="tests", help="Diretório para salvar os testes gerados.")
    parser.add_argument("--scale_factor", type=float, default=1.2, help="Fator de escala para ajustar estoques e exportações.")
    args = parser.parse_args()

    # Gerar os casos de teste
    generate_multiple_tests(
        args.num_tests, args.n, args.m, args.t, args.c_n, args.c_m, args.c_t, args.output_dir, args.scale_factor
    )
