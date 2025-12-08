def discount_price():
  print('Products: Doughnut🍩, Pizza🍕, Cake🎂')
  product = input('Enter product name: ')
  price = float(input('Enter price: RM '))
  discount=5
  final_price = float(price - (price * (discount / 100)))

  print(f"{product} price after {discount}% discount is: RM {final_price}")
discount_price()