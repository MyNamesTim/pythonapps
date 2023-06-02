import time

var num1 = int(input('What is the number that you would like to subtract from?'));
var num2 = int(input('What is the amount that you would like to subtract from the first number?'));

def subtraction():
  print('Subtracting...');
  time.sleep(1);
  var result = num1 - num2;
  print(num1 + ' minus ' + num2 + ' equals ' + result);
  time.sleep(0.5);
  print('Program shutting down in 15 seconds.');
  time.sleep(15);

subtraction();
