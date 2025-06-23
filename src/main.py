from regression import load_model
from optimizer import pso


def main():
    # Carregar o modelo treinado
    model = load_model()

    # Definir os limites de cada variável
    bounds = [
        (0, 10),   # Aparência
        (0, 14),   # pH
        (0, 10)    # Odor
    ]

    # Executar PSO
    melhor_posicao, melhor_valor = pso(model, bounds)

    print("\nMelhor combinação encontrada:")
    print(f"Aparência: {melhor_posicao[0]:.2f}")
    print(f"pH: {melhor_posicao[1]:.2f}")
    print(f"Odor: {melhor_posicao[2]:.2f}")
    print(f"Qualidade máxima prevista: {melhor_valor:.2f}")


if __name__ == "__main__":
    main()
