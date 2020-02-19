hours = float(input('How many hours did you do this week? '))
rate = 8.21
over = 1.5 * rate
income = hours*rate
diference = hours-40
nhs = income*0.01
tax = income*0.12
alltaxes = nhs+tax
if hours < 41:
    print("You earned £", income-alltaxes)
else:
    print("You earned £", income+diference-alltaxes)
print("You should work harder and longer to be rich ;PP")
input("Aby zakończyć program naciśnij ENTER")
