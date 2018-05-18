from smart_contract.contract_kultiva import *
from smart_contract.account_kultiva import *

print("Acc 1")
acc1 = create_account()
'''print("Acc 2")
acc2 = create_account()
print("Acc 3")
acc3 = create_account()'''

get_balance(acc1[2])

'''kp_acc1 = Keypair.deterministic(acc1[0])
kp_acc2 = Keypair.deterministic(acc2[0])
kp_acc3 = Keypair.deterministic(acc3[0])

create_payment(kp_dist, acc1[2], 30, 'Fund KLTV Again')
create_payment(kp_dist, acc2[2], 10, 'Fund KLTV Again')
create_payment(kp_dist, acc3[2], 10, 'Fund KLTV Again')

print("Phase 1 and 2")
list_escrow = create_and_fund(acc1[0], 2, [10, 10])
escrow_1 = list_escrow[0]
escrow_2 = list_escrow[1]
kp_escrow_1 = Keypair.deterministic(escrow_1[2])
kp_escrow_2 = Keypair.deterministic(escrow_2[2])
print("Phase 3")
add_signer_petani(list_escrow, [acc2[2], acc3[2]])
print("Phase 4")
add_signer_user(kp_acc2, escrow_1[0], acc1[2])
add_signer_user(kp_acc3, escrow_2[0], acc1[2])
print("Phase 5")
fund_petani(kp_acc1, escrow_1[0], acc2[2], 10)
fund_petani(kp_acc1, escrow_2[0], acc3[2], 10)
remove_escrow(kp_escrow_1, DIST_PUB)
remove_escrow(kp_escrow_2, DIST_PUB)

print("Back to kultiva")
create_payment(kp_acc1, DIST_PUB, 10, 'Refund to Kultiva')
create_payment(kp_acc2, DIST_PUB, 20, 'Refund to Kultiva')
create_payment(kp_acc3, DIST_PUB, 20, 'Refund to Kultiva')

print("Bonus")
merge_account(kp_acc1, DIST_PUB)
merge_account(kp_acc2, DIST_PUB)
merge_account(kp_acc3, DIST_PUB)'''
