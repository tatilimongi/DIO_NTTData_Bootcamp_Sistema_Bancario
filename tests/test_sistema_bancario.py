import pytest
from sistema_bancario import realizar_deposito, realizar_saque, exibir_extrato

# Fixture para configurar valores padrão
@pytest.fixture
def setup_conta():
    return {
        'saldo': 1000,
        'depositos': [],
        'saques': [],
        'saque_diario': 0,
        'LIMITE_SAQUE': 500,  # Limite de saque por transação
        'LIMITE_SAQUES_DIARIOS': 3  # Limite de saques diários
    }

# Teste para realizar_deposito
@pytest.mark.parametrize(
    "input_valor, saldo_esperado, depositos_esperados", [
        ("200", 1200, [200]),  # Depósito válido
        ("-50", 1000, []),     # Depósito inválido
        ("0", 1000, []),       # Depósito zero
    ]
)
def test_realizar_deposito(input_valor, saldo_esperado, depositos_esperados, monkeypatch, setup_conta):
    inputs = iter([input_valor])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    saldo = setup_conta['saldo']
    depositos = setup_conta['depositos']
    novo_saldo = realizar_deposito(saldo, depositos)
    
    assert novo_saldo == saldo_esperado
    assert depositos == depositos_esperados

import pytest
from sistema_bancario import realizar_deposito, realizar_saque, exibir_extrato

# Teste para realizar_saque com valores variados
@pytest.mark.parametrize(
    "input_valor, saldo_inicial, saque_diario_inicial, saldo_esperado, saque_diario_esperado, saques_esperados, mensagem_esperada", [
        ("300", 1000, 0, 700, 1, [300], ""),  # Saque válido
        ("300", 200, 0, 200, 0, [], "Saldo insuficiente"),  # Saque com saldo insuficiente
        ("600", 1000, 0, 1000, 0, [], "Limite de R$ 500.00 por saque."),  # Saque acima do limite por transação
        ("200", 1000, 3, 1000, 3, [], ""),    # Limite de saques diários atingido
    ]
)
def test_realizar_saque(input_valor, saldo_inicial, saque_diario_inicial, saldo_esperado, saque_diario_esperado, saques_esperados, mensagem_esperada, monkeypatch, capsys, setup_conta):
    # Configuração do mock do input
    inputs = iter([input_valor])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    LIMITE_SAQUE = setup_conta['LIMITE_SAQUE']
    LIMITE_SAQUES_DIARIOS = setup_conta['LIMITE_SAQUES_DIARIOS']
    saldo = saldo_inicial
    saque_diario = saque_diario_inicial
    saques = []

    # Função para realizar o saque, incluindo a verificação do limite
    def realizar_saque(LIMITE_SAQUE, saldo, saque_diario, saques):
        saque = float(input("Informe o valor do saque: "))

        # Verifica se o saque está dentro do limite por transação
        if saque > LIMITE_SAQUE:
            print(f"Limite de R$ {LIMITE_SAQUE}.00 por saque.")
            return saldo, saque_diario, saques

        # Verifica se o saque não ultrapassa o limite de saques diários
        if saque_diario >= LIMITE_SAQUES_DIARIOS:
            print("Limite de saques diários atingido.")
            return saldo, saque_diario, saques

        # Verifica se o saldo é suficiente
        if saque > saldo:
            print("Saldo insuficiente")
            return saldo, saque_diario, saques
        
        # Atualiza saldo e saques
        saldo -= saque
        saque_diario += 1
        saques.append(saque)
        return saldo, saque_diario, saques

    # Chamada à função
    novo_saldo, novo_saque_diario, saques_atualizados = realizar_saque(LIMITE_SAQUE, saldo, saque_diario, saques)

    # Validação dos resultados
    assert novo_saldo == saldo_esperado
    assert novo_saque_diario == saque_diario_esperado
    assert saques_atualizados == saques_esperados

    # Captura de saída para verificar mensagens
    captured = capsys.readouterr()
    assert mensagem_esperada in captured.out

# Teste para exibir_extrato
def test_exibir_extrato(capsys, setup_conta):
    saldo = 700
    saques = [300]
    depositos = [200, 300]
    
    exibir_extrato(saldo, saques, depositos)
    
    captured = capsys.readouterr()
    assert "1º depósito: R$ 200.00" in captured.out
    assert "2º depósito: R$ 300.00" in captured.out
    assert "1º saque: R$ 300.00" in captured.out
    assert "Saldo: R$ 700.00" in captured.out

