basic_salary = float(input('Please input the basic salary: '))
bonus_rate = float(input('Please input the bonus rate: '))
commission_rate = float(input('Please input the commission rate: '))
numberofgoods = int(input('Enter the number of goods sold: '))
price = float(input('Enter the price of goods: '))
bonus = (bonus_rate * numberofgoods)
commission = (commission_rate * price * numberofgoods)
print('Bonus = {:.2f}'.format(bonus))
print('Commission = {:.2f}'.format(commission))
print('Gross salary = {:.2f}'.format(basic_salary + bonus + commission))