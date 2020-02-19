from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT
from Clock import main as clock
import time

# import pytz

# tz = pytz.timezone('Europe/Berlin')
# berlin_now = datetime.now(tz)



def main():
        # Setup for Banggood version of 4 x 8x8 LED Matrix (https://bit.ly/2Gywazb)
        serial = spi(port=0, device=0, gpio=noop())
        # device = max7219(serial, cascaded=8, block_orientation=-90, blocks_arranged_in_reverse_order)
        device = max7219(serial, width=64, height=16, block_orientation=-90, rotate=0)

        # device.contrast(16)
        while True:
                c = clock()
                c.update_class(2)
                with canvas(device) as draw:
                        text(draw, (2, 1), c.hour_string, fill="white", font=proportional(CP437_FONT))
                        text(draw, (2, 9), c.minute_string, fill="white", font=proportional(CP437_FONT)) 

 			text(draw, (55, 1), "h", fill="white", font=proportional(TINY_FONT))	
			text(draw, (55, 9), "min", fill="white", font=proportional(TINY_FONT)) 		
			time.sleep(10)
if __name__ == "__main__":
        main()

