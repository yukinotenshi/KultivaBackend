from stellar_base.operation import *
from smart_contract.account_kultiva import *


# Create transaction with list of operations availables
def create_tx(pub_source, kp_signer, sequence, msg, list_op):
    tx = Transaction(
        source = pub_source,
        opts = {
            'fee': 100 * len(list_op),
            'sequence': sequence,
            'memo': msg,
            'operations': list_op
        },
    )
    # Create envelope
    envelope = Te(tx = tx, opts = {"network_id": "TESTNET"})
    # Sign
    envelope.sign(kp_signer)
    # Get xdr
    xdr = envelope.xdr()
    # Response
    return horizon.submit(xdr)


# Create account funded by signer
# In creating escrow, Signer is kultiva's account held by kultiva
def create_escrow(signer, total_escrow):
    # Get signer
    pub_source = signer.address().decode('utf-8')
    # List account
    list_escrow = []
    list_op = []
    # Generate key and operation create account
    for i in range(total_escrow):
        m_dest, kp_dest = generate_key()
        # Operation create account
        create_acc = CreateAccount({
            'source': pub_source,
            'destination': kp_dest.address().decode(),
            'starting_balance': '4',
        })
        list_escrow.append((kp_dest.address().decode(), kp_dest.seed().decode(), m_dest))
        list_op.append(create_acc)
    msg = TextMemo('Creating escrow accounts')
    # Get sequence
    sequence = horizon.account(pub_source).get('sequence')
    # Build transaction
    resp = create_tx(pub_source, signer, sequence, msg, list_op)
    print(list_escrow)
    print(resp)
    # Check if success
    try :
        temp = resp['status']
        raise Exception('Error creating account')
    except KeyError:
        return list_escrow


# Add trust to escrow
def add_trust_escrow(list_acc):
    for acc in list_acc:
        kp_acc = Keypair.deterministic(acc[2])
        change_trust(kp_acc, KLTV, 100000000)


# User has enough money
def escrow_fund(user, list_escrow, list_amount):
    pub_user = user.address().decode('utf-8')
    # Get sequence
    sequence = horizon.account(pub_user).get('sequence')
    list_fund = []
    # Add fund to each escrow
    for i in range(len(list_escrow)):
        payment = Payment({
            'source': pub_user,
            'destination': list_escrow[i],
            'asset': KLTV,
            'amount': str(list_amount[i])
        })
        list_fund.append(payment)
    # Memo
    msg = TextMemo('Add fund to escrow')
    # Create Transaction
    resp = create_tx(pub_user, user, sequence, msg, list_fund)
    print(resp)
    # Check if success
    try :
        temp = resp['status']
        raise Exception(temp)
    except KeyError:
        return True


# Change sign, Must True
def change_acc_signer(acc, new_signer_pub, weight):
    # Get public key
    public_acc = acc.address().decode()
    # Get sequence
    sequence = horizon.account(public_acc).get('sequence')
    set_option = SetOptions(
        opts = {
            'master_weight': 1,
            'signer_address': new_signer_pub,
            'signer_weight': weight,
            'low_threshold': 1,
            'med_threshold': 1,
            'high_threshold': 1
        }
    )
    msg = TextMemo('Add Farmer Signer')
    resp = create_tx(public_acc, acc, sequence, msg, [set_option])
    print(resp)


# Change signer account by another signer
def change_other_signer(pub_acc, new_signer_pub, weight, signer):
    # Get sequence
    sequence = horizon.account(pub_acc).get('sequence')
    set_option = SetOptions(
        opts={
            'master_weight': 1,
            'signer_address': new_signer_pub,
            'signer_weight': weight,
            'low_threshold': 1,
            'med_threshold': 1,
            'high_threshold': 1
        }
    )
    msg = TextMemo('Add Farmer Signer')
    resp = create_tx(pub_acc, signer, sequence, msg, [set_option])
    print(resp)


# Payment, Must True
def create_payment(source, pub_destination, amount, memo_string):
    pub_source = source.address().decode('utf-8')
    # Get sequence
    sequence = horizon.account(pub_source).get('sequence')
    payment = Payment({
        'source': pub_source,
        'destination': pub_destination,
        'asset': KLTV,
        'amount': str(amount)
    })
    # Memo
    msg = TextMemo(memo_string)
    # Create transaction
    resp = create_tx(pub_source, source, sequence, msg, [payment])
    print(resp)


# Payment signed by other user
def create_payment_other(pub_source, pub_destination, amount, memo_string, signer):
    # Get sequence
    sequence = horizon.account(pub_source).get('sequence')
    payment = Payment({
        'source': pub_source,
        'destination': pub_destination,
        'asset': KLTV,
        'amount': str(amount)
    })
    # Memo
    msg = TextMemo(memo_string)
    # Create transaction
    resp = create_tx(pub_source, signer, sequence, msg, [payment])
    print(resp)


# Return XLM to Kultiva Account
def merge_account(source, pub_destination):
    pub_source = source.address().decode('utf-8')
    change_trust(source, KLTV, 0)
    # Get sequence
    sequence = horizon.account(pub_source).get('sequence')
    merge = AccountMerge({
        'source': pub_source,
        'destination': pub_destination
    })
    # Memo
    msg = TextMemo('Send XLM back to Kultiva')
    # Create Transaction
    resp = create_tx(pub_source, source, sequence, msg, [merge])
    print(resp)

# Create account with funded money + trust
def create_account():
    # Create key and add fund
    m, kp = generate_key()
    public = kp.address().decode()
    secret = kp.seed().decode()
    add_fund_bot(public)
    # Change the trust
    change_trust(kp, KLTV, 100000000)
    create_payment(kp_dist, public, 10000000, "hahshhs")
    # Return it
    return m, secret, public
