# Import Module


import math  # Required For Coordinates Calculation
import time  # Required For Time Handling
from datetime import datetime
import random


#


class main():
        def __init__(self):
                pass

        minute_string = str(' ')
        hour_string = str(' ')
        # 0 heißt strichrechnung
        # 1 heißt punktrechnung
        # 2 heißt kombination
        calc_mode = 1

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

        def set_calc_mode(self, new_calc_mode):
                if new_calc_mode > -1 and new_calc_mode < 3:
                        self.calc_mode = new_calc_mode


        def set_minute_string(self, which_minute):
                rng_number = 0
                if self.calc_mode == 0:
                        rng_number = random.randrange(1, 99)
                        while rng_number == which_minute:
                                rng_number = random.randrange(1, 99)
                        if rng_number > which_minute:
                                self.minute_string = str(rng_number) + ' - ' + str(rng_number - which_minute)
                        else:
                                self.minute_string = str(rng_number) + ' + ' + str(which_minute - rng_number)
                elif self.calc_mode == 1:
                        if which_minute != 0:
                                rng_number = random.randrange(1, which_minute)
                                if rng_number != 0:
                                        while which_minute % rng_number != 0:
                                                rng_number = random.randrange(1, which_minute)
                                if rng_number != 0:
                                         self.minute_string = str(rng_number) + ' * ' + str(which_minute / rng_number)
                return

        # Function Need Regular Update
        def update_class(self):
                now = time.localtime()
                t = time.strptime(str(now.tm_hour), "%H")
                hour = int(time.strftime("%I", t)) * 5
                now = (hour, now.tm_min, now.tm_sec)

                # strichrechnug - siehe oben bei der defintion der variable
                self.set_calc_mode(0)
                now2 = datetime.now()
                print("%s/%s/%s %s:%s:%s" % (now2.month, now2.day, now2.year, now2.hour, now2.minute, now2.second))
                self.set_minute_string(now2.minute)
                print(self.minute_string)
                time.sleep(1)

                # Changing Stick Coordinates
                return


# Main Function Trigger
if __name__ == '__main__':
        root = main()

        # Creating Main Loop
        while True:
                root.update_class()
