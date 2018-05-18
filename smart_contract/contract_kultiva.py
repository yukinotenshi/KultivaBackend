from smart_contract.transaction_kultiva import *


# Create escrow and add fund
# 1st and 2nd Phase
def create_and_fund(mnemonic, total_addr, list_cost):
    # Create escrow funded by main account
    # Then add trustline from escrow
    try:
        list_escrow = create_escrow(kp_dist, total_addr)
    except Exception as e:
        raise Exception('Failed to create escrow!')

    # Add trust must be true!
    add_trust_escrow(list_escrow)
    # Get list public escrow
    list_pub_escrow = [escrow[0] for escrow in list_escrow]
    # Keypair generated
    kp_user = Keypair.deterministic(mnemonic)
    # User fund KLTV to escrow
    if escrow_fund(kp_user, list_pub_escrow, list_cost):
        return list_escrow
    else:
        for escrow in list_escrow:
            kp_escrow = Keypair.from_seed(escrow[1])
            merge_account(kp_escrow, DIST_PUB)
        raise Exception('Failed to create escrow!')


# 3rd phase
def add_signer_petani(list_escrow, list_petani):
    list_kp_escrow = [Keypair.deterministic(escrow[2]) for escrow in list_escrow]
    for i in range(len(list_petani)):
        kp_escrow = list_kp_escrow[i]
        petani = list_petani[i]
        change_acc_signer(kp_escrow, petani, 1)


# 4th phase
def add_signer_user(kp_petani, escrow, user):
    # Add user as signer
    change_other_signer(escrow, user, 1, kp_petani)
    # Get self public key
    pub_petani = kp_petani.address().decode()
    # Remove self as signer
    change_other_signer(escrow, pub_petani, 0, kp_petani)


# 5th phase
def fund_petani(kp_user, escrow, petani, amount):
    # Fund to farmer
    create_payment_other(escrow, petani, amount, 'Fund to Farmer', kp_user)
    # Get self public key
    pub_user = kp_user.address().decode()
    # Remove self as signer
    change_other_signer(escrow, pub_user, 0, kp_user)


# Another case
# Refund asset KLTV to honest user
def refund(kp_escrow, destination, amount):
    create_payment(kp_escrow, destination, amount, 'Refund')


# Remove escrow
# Escrow doesnt have any asset, only XLM
def remove_escrow(kp_escrow, destination):
    merge_account(kp_escrow, destination)