# Pesquisa de satisfação - TudoWeb

qtde_excelente = 0
qtde_ruim = 0

for i in range(1, 51):
    print(f"\nEntrevistado {i}:")
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    # Loop para garantir resposta válida
    while True:
        print("Opinião sobre o atendimento:")
        print("1 - EXCELENTE")
        print("2 - BOM")
        print("3 - RUIM")
        opiniao = input("Digite sua opinião (1/2/3): ")

        if opiniao in ["1", "2", "3"]:
            opiniao = int(opiniao)
            break
        else:
            print("Resposta inválida! Por favor, digite apenas 1, 2 ou 3.")

    # Estrutura de decisão para contar respostas
    if opiniao == 1:
        qtde_excelente += 1
    elif opiniao == 3:
        qtde_ruim += 1

# Resultado final
print("\n--- RESULTADO DA PESQUISA ---")
print(f"Quantidade de respostas EXCELENTE: {qtde_excelente}")
print(f"Quantidade de respostas RUIM: {qtde_ruim}")
