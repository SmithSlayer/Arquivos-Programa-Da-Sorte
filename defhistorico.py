def armazenar_numeros():
    historico = []  # Lista para armazenar os números digitados
    while True:
        try:
            numero = int(input("Digite um número (ou '0' para sair): "))
            if numero == 0:
                print("Encerrando...")
                break
            historico.append(numero)
            print(f"Histórico atualizado: {historico}")  # Exibe o histórico atualizado a cada entrada
        except ValueError:
            print("Por favor, digite um número válido.")
    
    print("\nHistórico final de números digitados:", historico)
    return historico

# Executa a função
historico_jogador = armazenar_numeros()
