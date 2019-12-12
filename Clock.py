# Import Module


import math # Required For Coordinates Calculation
import time # Required For Time Handling
from datetime import datetime
import random

#


class main():
 def __init__(self):
  pass
 minute_string =str(' ')
 hour_string = str(' ')

 # Creating Trigger For Other Functions
 def creating_all_function_trigger(self):
  return

 # Creating Background
 def creating_background_(self):
  return

 # creating Canvas
 def create_canvas_for_shapes(self):
  return

 # Creating Moving Sticks
 def creating_sticks(self):
  return

#rechnung spinnt noch, aber es geht voran. python nervt!
 def set_minute_string(self, which_number):
  rng_number = random.randrange(1, 100)
  while rng_number == which_number:
   rng_number = random.randrange(1, 100)
  if(rng_number > which_number):
   self.minute_string = str(rng_number) + ' + ' + str(which_number-rng_number)
  else:
   self.minute_string = str(rng_number) + ' + ' + str(which_number+rng_number)
  return



 # Function Need Regular Update
 def update_class(self):
  now=time.localtime()
  t = time.strptime(str(now.tm_hour), "%H")
  hour = int(time.strftime( "%I", t ))*5
  now=(hour,now.tm_min,now.tm_sec)


  now2 = datetime.now()
  print ("%s/%s/%s %s:%s:%s" % (now2.month, now2.day, now2.year, now2.hour, now2.minute, now2.second))
  self.set_minute_string(now2.minute)
  print(self.minute_string)
  time.sleep(1)


  # Changing Stick Coordinates
  return

# Main Function Trigger
if __name__ == '__main__':
 root=main()

 # Creating Main Loop
 while True:
  root.update_class()