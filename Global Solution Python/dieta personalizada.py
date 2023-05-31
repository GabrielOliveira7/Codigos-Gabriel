import openai

# Define sua chave de API do OpenAI
openai.api_key = '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'

def gerar_texto_dieta(ingredientes, refeicoes, dias):
    # Ordena a lista de ingredientes pela data de validade (em ordem crescente)
    ingredientes.sort(key=lambda x: x[2])

    prompt = f"Com base nos ingredientes disponíveis, construa uma dieta com {refeicoes} refeições ao longo de {dias} dias.\n"

    # Adiciona o modo de preparo para cada refeição
    for i in range(1, refeicoes + 1):
        prompt += f"\nRefeição {i}:"
        for ingrediente, quantidade, _ in ingredientes:
            prompt += f"\n- {quantidade} de {ingrediente}"

        prompt += "\nModo de preparo: "

    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

def planejamento_dieta():
    # Solicita os dados ao usuário
    ingredientes = []
    
    while True:
        ingrediente = input("Informe o tipo de ingrediente: ")
        quantidade = input("Informe a quantidade desse ingrediente: ")
        data_validade = input("Informe a data de validade (no formato dd/mm/aaaa): ")

        ingredientes.append((ingrediente, quantidade, data_validade))

        opcao = input("Deseja inserir outro ingrediente? (s/n): ")
        if opcao.lower() != 's':
            break

    refeicoes = int(input("Informe a quantidade de refeições desejada: "))
    dias = int(input("Informe a quantidade de dias para as refeições: "))

    # Gera o texto da dieta
    texto_dieta = gerar_texto_dieta(ingredientes, refeicoes, dias)

    # Exibe o resultado
    print(texto_dieta)

# Menu de escolhas
print("Bem-vindo(a)!")
print("Escolha uma opção:")
print("1. Realizar um plano de dieta")
print("2. Encerrar o programa")

opcao = input("Digite o número da opção desejada: ")

while opcao != '2':
    if opcao == '1':
        planejamento_dieta()
    else:
        print("Opção inválida. Tente novamente.")

    opcao = input("Digite o número da opção desejada: ")

print("Programa encerrado.")