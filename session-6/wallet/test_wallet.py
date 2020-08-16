import pytest
from random import randint
from wallet import Wallet, InsufficientAmount

def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0


# @pytest.mark.skip()
# @pytest.mark.smoke
def test_setting_initial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100


# @pytest.mark.skip(reason="To be suuported on v1.0")
# @pytest.mark.smoke
def test_wallet_add_cash():
    wallet = Wallet(10)
    wallet.add_cash(90)
    assert wallet.balance == 100


@pytest.mark.smoke
@pytest.mark.xfail()
def test_wallet_spend_cash():
    wallet = Wallet(20)
    wallet.spend_cash(10)
    assert wallet.balance == 10


@pytest.mark.xfail()
def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
    wallet = Wallet()
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(100)


def transaction_params(num):
    for _ in range(num):
        earned = randint(100,500)
        spend = randint(20,50)
        expected_balance = earned - spend
        yield earned, spend, expected_balance

@pytest.mark.parametrize("earned,spent,expected", transaction_params(10))

def test_transactions(earned, spent, expected):
    my_wallet = Wallet()
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected