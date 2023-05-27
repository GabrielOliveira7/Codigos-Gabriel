import openai

# Define sua chave de API do OpenAI
openai.api_key = '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'

def calcular_imc(peso, altura):
    altura_metros = altura / 100  # Convertendo a altura para metros
    imc = peso / (altura_metros ** 2)
    return imc

def gerar_texto_dieta(ingredientes, refeicoes, dias, imc):
    prompt = f"Com base nos ingredientes: {ingredientes}, construa uma dieta com {refeicoes} refeições ao longo de {dias} dias para uma pessoa com IMC de {imc:.2f}."
    response = openai.Completion.create(
        engine='curie',
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

# Solicita os dados ao usuário
ingredientes = []
quantidades = []

while True:
    ingrediente = input("Informe o tipo de ingrediente: ")
    quantidade = input("Informe a quantidade desse ingrediente: ")

    ingredientes.append(ingrediente)
    quantidades.append(quantidade)

    opcao = input("Deseja inserir outro ingrediente? (s/n): ")
    if opcao.lower() != 's':
        break

refeicoes = int(input("Informe a quantidade de refeições desejada: "))
dias = int(input("Informe a quantidade de dias para as refeições: "))
peso = float(input("Informe seu peso (em kg): "))
altura = float(input("Informe sua altura (em cm): "))

# Calcula o IMC
imc = calcular_imc(peso, altura)

# Gera o texto da dieta
texto_dieta = gerar_texto_dieta(ingredientes, refeicoes, dias, imc)

# Exibe o resultado
print(texto_dieta)