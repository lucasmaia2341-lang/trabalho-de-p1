# --------------------------
# Alunos: Lucas Maia e Iohannan Anthony 
# --------------------------
import json

# --------------------------
# FUNÇÕES
# --------------------------

def carregar_dados():
    try:
        with open("jogadores.json", "r") as arquivo:
            return json.load(arquivo)
    except:
        return []

def salvar_dados(jogadores):
    with open("jogadores.json", "w") as arquivo:
        json.dump(jogadores, arquivo)

def criar_ficha(jogadores):
    if len(jogadores) >= 3:
        print("\n❌ Limite de 3 fichas atingido!\n")
        return

    nome = input("Nome do personagem: ")
    arma = input("Arma: ")
    item = input("Item: ")

    ficha = {
        "nome": nome,
        "arma": arma,
        "item": item
    }

    jogadores.append(ficha)
    print("\n✅ Ficha criada com sucesso!\n")

def listar_fichas(jogadores):
    if not jogadores:
        print("\n⚠️ Nenhuma ficha criada.\n")
        return

    print("\n===== FICHAS CRIADAS =====")
    for i, ficha in enumerate(jogadores, start=1):
        print(f"\nFicha {i}")
        print("-------------------------")
        print("Nome:", ficha["nome"])
        print("Arma:", ficha["arma"])
        print("Item:", ficha["item"])
    print()

def apagar_ficha(jogadores):
    if not jogadores:
        print("\n⚠️ Nenhuma ficha para apagar.\n")
        return

    listar_fichas(jogadores)
    num = int(input("Digite o número da ficha que deseja apagar: "))

    if num < 1 or num > len(jogadores):
        print("\n❌ Número inválido.\n")
        return

    apagada = jogadores.pop(num - 1)
    print(f"\n🗑️ Ficha de {apagada['nome']} apagada!\n")

# --------------------------
# PROGRAMA PRINCIPAL
# --------------------------

jogadores = carregar_dados()

while True:
    print("""
=================================
      🎮 MENU PRINCIPAL 🎮
=================================
1 - Criar nova ficha
2 - Listar fichas
3 - Apagar ficha
4 - Salvar e sair
=================================
""")

    op = input("Escolha uma opção: ")

    if op == "1":
        criar_ficha(jogadores)
    elif op == "2":
        listar_fichas(jogadores)
    elif op == "3":
        apagar_ficha(jogadores)
    elif op == "4":
        salvar_dados(jogadores)
        print("\n💾 Dados salvos. Saindo do jogo...\n")
        break
    else:
        print("\n❌ Opção inválida! Tente novamente.\n")

