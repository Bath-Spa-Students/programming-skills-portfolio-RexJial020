
price = 6
cash = 50
usb1 = cash // price
usb2 = price * usb1 

paid = usb2
change = cash - paid  

print (f'Cash: £{cash}')
print (f'\nAmount Paid: £{paid}')
print (f'Change: £{change}')
print (f'USB Sticks bought: {usb1}')
