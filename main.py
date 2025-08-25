import random

print("Bichinho virtual")
nome = input("Dê um nome para o seu bichinho: ")

pet = {
    "nome": nome,
    "fome": 50,         # 100 mortinho de fome
    "felicidade": 50,   # 100 happy happy happy
    "energia": 50       # 100 cheio de energia
}

def mostrar_status():
    print(f"Status de {pet['nome']}:")
    print(f"Fome: {pet['fome']}")
    print(f"Felicidade: {pet['felicidade']}")
    print(f"Energia: {pet['energia']}")


while True:
    mostrar_status()
    print("O que deseja fazer agora?")
    print("1 - Alimentar")
    print("2 - Brincar")
    print("3 - Colocar para dormir")
    print("0 - Sair")

    escolha = input("Escolha: ")


    if escolha == "1":
        pet["fome"] = max(0, pet["fome"] - 50)
        pet["felicidade"] = min(100, pet["felicidade"] + 5)
        print(f"Você alimentou {pet['nome']}! Nhami Nhami")

    elif escolha == "2":
        if pet["energia"] > 20:
            pet["felicidade"] = min(100, pet["felicidade"] + 50)
            pet["energia"] = max(0, pet["energia"] - 15)
            pet["fome"] = min(100, pet["fome"] + 10)
            print(f"Você brincou com {pet['nome']}!Uhuuul")
        else:
            print(f"{pet['nome']} está cansadito demais para brincar...")

    elif escolha == "3":
        pet["energia"] = min(100, pet["energia"] + 50)
        pet["fome"] = min(100, pet["fome"] + 10)
        print(f"\n{pet['nome']} tirou uma soneca gostosa! zzz")

    elif escolha == "0":
        print(f"Tchau tchau {pet['nome']}! Até a próxima!")
        break

    else:
        print("Opção inválida!")


