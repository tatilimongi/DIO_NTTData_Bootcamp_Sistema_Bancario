import pytest
from sistema_bancario import realizar_deposito, realizar_saque, exibir_extrato

# Teste para realizar_deposito
def test_realizar_deposito_valido(monkeypatch):
    inputs = iter(["200"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    saldo = 1000
    depositos = []
    novo_saldo = realizar_deposito(saldo, depositos)
    
    assert novo_saldo == 1200
    assert depositos == [200]

def test_realizar_deposito_invalido(monkeypatch):
    inputs = iter(["-50"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    saldo = 1000
    depositos = []
    novo_saldo = realizar_deposito(saldo, depositos)
    
    assert novo_saldo == 1000
    assert depositos == []

# Teste para realizar_saque
def test_realizar_saque_valido(monkeypatch):
    inputs = iter(["300"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    LIMITE_SAQUE = 3
    saldo = 1000
    saque_diario = 0
    saques = []
    novo_saldo, novo_saque_diario = realizar_saque(LIMITE_SAQUE, saldo, saque_diario, saques)

    assert novo_saldo == 700
    assert novo_saque_diario == 1
    assert saques == [300]

def test_realizar_saque_saldo_insuficiente(monkeypatch):
    inputs = iter(["300"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    LIMITE_SAQUE = 3
    saldo = 200
    saque_diario = 0
    saques = []
    novo_saldo, novo_saque_diario = realizar_saque(LIMITE_SAQUE, saldo, saque_diario, saques)

    assert novo_saldo == 200
    assert novo_saque_diario == 0
    assert saques == []

# Teste para exibir_extrato
def test_exibir_extrato(capsys):
    saldo = 700
    saques = [300]
    depositos = [200, 300]
    exibir_extrato(saldo, saques, depositos)
    
    captured = capsys.readouterr()
    assert "1º depósito: R$ 200.00" in captured.out
    assert "2º depósito: R$ 300.00" in captured.out
    assert "1º saque: R$ 300.00" in captured.out
    assert "Saldo: R$ 700.00" in captured.out
