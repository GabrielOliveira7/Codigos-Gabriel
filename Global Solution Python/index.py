import openai

# Define sua chave de API do OpenAI
openai.api_key = 'SUA_CHAVE_DE_API_DO_OPENAI'

def gerar_texto_dieta(ingredientes, refeicoes, dias):
    prompt = f"Com base nos ingredientes: {ingredientes}, construa uma dieta com {refeicoes} refeições ao longo de {dias} dias."
    response = openai.Completion.create(
        engine='davinci-codex',  # Você pode usar 'davinci' em vez de 'davinci-codex' se preferir
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

# Solicita os dados ao usuário
ingredientes = input("Informe os ingredientes que você possui: ")
refeicoes = int(input("Informe a quantidade de refeições desejada: "))
dias = int(input("Informe a quantidade de dias para as refeições: "))

# Gera o texto da dieta
texto_dieta = gerar_texto_dieta(ingredientes, refeicoes, dias)

# Exibe o resultado
print(texto_dieta)