# 1. ENTRADA DE DADOS E VARIÁVEIS
print("--- Bem-vindo ao seu primeiro programa! ---")
nome = input("Qual é o seu nome? ")
ano_nascimento = input("Em que ano você nasceu? ")

# 2. CONVERSÃO E CÁLCULO
# O input recebe texto, então usamos 'int()' para converter para número inteiro
idade = 2025 - int(ano_nascimento)

# 3. LÓGICA DE DECISÃO (IF/ELSE)
if idade >= 18:
    status = "maior de idade"
else:
    status = "menor de idade"

# 4. EXIBIÇÃO DE RESULTADO (SAÍDA)
print(f"\nOlá {nome}! Você tem {idade} anos e já é {status}.")

# 5. REPETIÇÃO (LOOP)
print("\nContando até 3 para finalizar:")
for numero in range(1, 4):
    print(f"Número... {numero}")

print("\nFim do programa!")
