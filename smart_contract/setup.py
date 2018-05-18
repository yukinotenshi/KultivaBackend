from stellar_base.keypair import Keypair
from stellar_base.horizon import horizon_testnet
from stellar_base.transaction import Transaction
from stellar_base.asset import Asset
from stellar_base.memo import TextMemo
from stellar_base.transaction_envelope import TransactionEnvelope as Te

# KLV
ISSUER = 'GDHR6UNRMLFSOFTIA5EKLIC32BLYSPFLMXJ4G43DYJZOZROR2B65OAPH'
KLTV = Asset('KLTV', ISSUER)

# Distributor -> MAIN ACC
DIST_PUB = 'GAN7PYN7D5V76PQNOIDWPRN7TV7TWM24EY7434LI7O35PUPJC5PQOKKT'
DIST_SEED = 'SDNHI43C4NUEZZFKIFTSXD6JEPTMZLMNRL5X3NMWQOQ43A2HEIM2D274'
kp_dist = Keypair.from_seed(DIST_SEED)

# URL Testnet
URL = 'https://horizon-testnet.stellar.org/'

# Distributor Address
seckey_dist = 'SCXGWORDHZA42NBPL7RQBWDYHV7JR672QRBGB3MX2WINJF2YJROTUNYK'

# Testing seed
seed = 'SBTYKU5OOZE46X63NBGXJ5XW32Q244DFMLCSZQP263GJF2GJSV5O53RO'

# Horizon Testnet
horizon = horizon_testnet()