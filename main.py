def mostrar_menu():
    print("O que deseja fazer agora?")
    print("1 - Alimentar")
    print("2 - Brincar")
    print("3 - Colocar para dormir")
    print("0 - Sair")


def alimentar(pet):
    pet["fome"] = max(0, pet["fome"] - 50)
    pet["felicidade"] = min(100, pet["felicidade"] + 5)
    print(f"Você alimentou {pet['nome']}! Nhami Nhami")


def brincar(pet):
    if pet["energia"] > 20:
        pet["felicidade"] = min(100, pet["felicidade"] + 50)
        pet["energia"] = max(0, pet["energia"] - 15)
        pet["fome"] = min(100, pet["fome"] + 10)
        print(f"Você brincou com {pet['nome']}!Uhuuul")
    else:
        print(f"{pet['nome']} está muy cansadito para brincar...")


def dormir(pet):
    pet["energia"] = min(100, pet["energia"] + 50)
    pet["fome"] = min(100, pet["fome"] + 10)
    print(f"\n{pet['nome']} tirou uma soneca gostosa! zzz")


def main():
    print("Bichinho virtual")
    nome = input("Dê um nome para o seu bichinho: ")
    pet = {
        "nome": nome,
        "fome": 50,
        "felicidade": 50,
        "energia": 50,
    }

    while True:
        print(f"Status de {pet['nome']}:")
        print(f"Fome: {pet['fome']}")
        print(f"Felicidade: {pet['felicidade']}")
        print(f"Energia: {pet['energia']}")
        mostrar_menu()
        escolha = input("Escolha: ")

        if escolha == "1":
            alimentar(pet)
        elif escolha == "2":
            brincar(pet)
        elif escolha == "3":
            dormir(pet)
        elif escolha == "0":
            print(f"Tchau tchau {pet['nome']}! Até mais!")
            return pet
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
