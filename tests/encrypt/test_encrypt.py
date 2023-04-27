import pytest
from encrypt import encrypt_message


def test_encrypt_message():
    # Teste 1: índice positivo válido, chave ímpar
    assert encrypt_message("trybe", 2) == "ryb_te"

    # Teste 2: índice positivo válido, chave par
    assert encrypt_message("trybe", 3) == "ytb_re"

    # Teste 3: índice igual a 0, retorna mensagem invertida
    assert encrypt_message("trybe", 0) == "ebryt"

    # Teste 4: índice igual ao tamanho da mensagem, retorna mensagem invertida
    assert encrypt_message("trybe", 5) == "ebryt"

    # Teste 5: índice maior que o tamanho da mensagem, gera exceção
    with pytest.raises(Exception):
        encrypt_message("trybe", 6)

    # Teste 6: índice negativo, gera exceção
    with pytest.raises(Exception):
        encrypt_message("trybe", -1)

    # Teste 7: mensagem vazia, gera exceção
    with pytest.raises(Exception):
        encrypt_message("", 2)

    # Teste 8: chave inválida, gera exceção
    with pytest.raises(Exception):
        encrypt_message("trybe", "key")

    # Teste 9: tipo de mensagem inválido, gera exceção
    with pytest.raises(Exception):
        encrypt_message(123, 2)

    # Teste 10: tipo de chave inválido, gera exceção
    with pytest.raises(Exception):
        encrypt_message("trybe", 2.5)
