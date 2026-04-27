from unittest.mock import patch

from main import alimentar, brincar, dormir, main, mostrar_menu


def test_mostrar_menu(capsys):
    mostrar_menu()
    saida = capsys.readouterr().out

    assert "1 - Alimentar" in saida
    assert "2 - Brincar" in saida
    assert "3 - Colocar para dormir" in saida
    assert "0 - Sair" in saida


def test_alimentar():
    pet = {"nome": "Rex", "fome": 50, "felicidade": 50, "energia": 50}
    alimentar(pet)

    assert pet["fome"] == 0
    assert pet["felicidade"] == 55
    assert pet["energia"] == 50


def test_brincar():
    pet = {"nome": "Rex", "fome": 50, "felicidade": 50, "energia": 50}
    brincar(pet)

    assert pet["felicidade"] == 100
    assert pet["energia"] == 35
    assert pet["fome"] == 60


def test_dormir():
    pet = {"nome": "Rex", "fome": 50, "felicidade": 50, "energia": 50}
    dormir(pet)

    assert pet["energia"] == 100
    assert pet["fome"] == 60


def test_main(capsys):
    with patch("builtins.input", side_effect=["Rex", "0"]):
        pet = main()
    saida = capsys.readouterr().out

    assert pet == {"nome": "Rex", "fome": 50, "felicidade": 50, "energia": 50}
    assert "Tchau tchau Rex" in saida
