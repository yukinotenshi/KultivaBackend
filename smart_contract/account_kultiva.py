# To do everything with stellar account associated with Kultiva


from smart_contract.setup import *
from stellar_base.utils import StellarMnemonic
from stellar_base.operation import ChangeTrust
from stellar_base.address import Address
import requests


# Change trust
def change_trust(acc, asset, limit):
    sequence = horizon.account(acc.address().decode('utf-8')).get('sequence')
    # Operation add trustline
    add_issue = ChangeTrust({
        'asset': asset,
        'limit': str(limit),
    })
    msg = TextMemo('Add issue')
    # Transaction builder
    tx = Transaction(
        source=acc.address().decode(),
        opts={
            'sequence': sequence,
            'memo': msg,
            'operations': [add_issue],
        },
    )
    envelope = Te(tx=tx, opts={"network_id": "TESTNET"})
    # Sign envelope
    envelope.sign(acc)
    # Get the xdr
    xdr = envelope.xdr()
    # Submit to horizon
    response = horizon.submit(xdr)
    # If Transaction Success, return True
    try:
        return not response['status']
    except KeyError:
        return True


# Generate key without funded
def generate_key():
    # Generate key
    print('Generate key..')
    sm = StellarMnemonic()
    m = sm.generate()
    print('Create key pair..')
    kp = Keypair.deterministic(m)
    # Return
    return m, kp


# Fund with bot
def add_fund_bot(public_key):
    # Request to friendbot
    requests.get('https://friendbot.stellar.org/?addr=' + public_key)


# Get balance from the account
def get_balance(pub_key):
    _address = Address(address=pub_key)
    _address.get()
    print(_address.balances)
    return _address.balances[0]['balance']
