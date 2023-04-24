import time

var addOne = int(input('What is the first number you would like to add?'));
var addTwo = int(input('What is the second number you would like to add?'));

function addition(): {
  result = addOne + addTwo;
  time.sleep(.5)
  print(result);
  time.sleep(1)
  print('Program shutting down in 15 seconds.');
  time.sleep(15)
}

addition()
