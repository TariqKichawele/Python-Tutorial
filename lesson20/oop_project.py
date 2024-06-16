from bank_accounts import *

top_g = BankAccount(1000, 'top g')
top_t = BankAccount(3000, 'top t')

print("")

top_g.getBalance()
top_t.getBalance()

print("")

top_g.deposit(2000)
top_t.deposit(1000)

print('')
top_g.withdraw(10000)
top_g.withdraw(100)

print('')
top_g.transfer(100, top_t)

print('')
top_z = InterestRewardsAcct(3000, 'top z')
top_z.getBalance()
top_z.deposit(100)
top_z.transfer(100, top_g)

print('')

top_b = SavingsAcct(2000, 'top b')
top_b.getBalance()
top_b.deposit(100)
top_b.transfer(100, top_z)


 

