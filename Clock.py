# Import Module


import math  # Required For Coordinates Calculation
import time  # Required For Time Handling
from datetime import datetime
#import pytz
import random


#


class main():
        def __init__(self):
                pass

        minute_string = str(' ')
        hour_string = str(' ')
        # 0 heisst strichrechnung
        # 1 heisst punktrechnung
        # 2 heisst kombination
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
                #  strichrechnung
                if self.calc_mode == 0:
                        self.minute_string = self.line_calculation(which_minute)
                # punktrechnung
                elif self.calc_mode == 1:
                        self.minute_string = self.point_calculation(which_minute)
                elif self.calc_mode == 2:
                        rng_calc_mode = random.randrange(0, 2)
                        if rng_calc_mode == 1:
                                self.minute_string = self.line_calculation(which_minute)
                        else:
                                self.minute_string = self.point_calculation(which_minute)
                return

        def set_hour_string(self, which_hour):
                # strichrechnung
                if self.calc_mode == 0:
                        self.hour_string = self.line_calculation(which_hour + 1)
                # punktrechnung
                elif self.calc_mode == 1:
                        self.hour_string = self.point_calculation(which_hour + 1)
                elif self.calc_mode == 2:
                        rng_calc_mode = random.randrange(0, 2)
                        if rng_calc_mode == 1:
                                self.hour_string = self.line_calculation(which_hour + 1)
                        else:
                                self.hour_string = self.point_calculation(which_hour + 1) #+1 weil wir zu doof waren, die zeitzone zu implementiren
                return

        def point_calculation(self, which_minute_or_hour):
                if which_minute_or_hour != 0:
                        # 0 heisst mal
                        # 1 heisst geteilt
                        which_point_calc_mode = random.randrange(0, 2)
                        if which_point_calc_mode == 0:
                                rng_number = random.randrange(0, which_minute_or_hour)
                                print(which_minute_or_hour)
                                if rng_number != 0:
                                        while which_minute_or_hour % rng_number != 0:
                                                rng_number = random.randrange(1, which_minute_or_hour)
                                if rng_number != 0:
                                        return str(rng_number) + ' * ' + str(which_minute_or_hour / rng_number)
                        elif which_point_calc_mode == 1:
                                rng_number = random.randrange(1, 11)
                                return str(which_minute_or_hour * rng_number) + ' : ' + str(rng_number)
                elif which_minute_or_hour == 0:
                        return str('0 * 0')

        def line_calculation(self, which_minute_or_hour):
                rng_number = random.randrange(1, 99)
                while rng_number == which_minute_or_hour:
                        rng_number = random.randrange(1, 99)
                if rng_number > which_minute_or_hour:
                        return str(rng_number) + ' - ' + str(rng_number - which_minute_or_hour)
                else:
                        return str(rng_number) + ' + ' + str(which_minute_or_hour - rng_number)

        # Function Need Regular Update
        def update_class(self, calc_mode):
                now = time.localtime()
                t = time.strptime(str(now.tm_hour), "%H")
                hour = int(time.strftime("%I", t)) * 5
                now = (hour, now.tm_min, now.tm_sec)

                # strichrechnug - siehe oben bei der defintion der variable
                self.set_calc_mode(calc_mode)
                now2 = datetime.now()
                print("%s/%s/%s %s:%s:%s" % (now2.month, now2.day, now2.year, now2.hour, now2.minute, now2.second))
                self.set_hour_string(now2.hour)
                self.set_minute_string(now2.minute)
                print(self.hour_string + ' h')
                print(self.minute_string + 'min ')
                time.sleep(30)

                # Changing Stick Coordinates
                return


# Main Function Trigger
if __name__ == '__main__':
        root = main()

        # Creating Main Loop
        while True:
                root.update_class()
