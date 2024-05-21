# YD-RP2040 Board
# User Button (GPIO24)
# User LED    (GPIO25)

import time # type: ignore
from machine import Pin, Timer # type: ignore
from libs.module_init import Global_Default as MyDefault
 
usr_led = Pin(25, Pin.OUT)

Counter_1 = 0
Counter_2 = 0

# ==============================================================================

def timer_1_call(tim):
    global Counter_1
    # print("Timer 1 Call")

    if Counter_1 == 1:
        usr_led.value(True)
        Counter_1 = 0
    else:
        usr_led.value(False)
        Counter_1 = Counter_1 + 1
 
# ==============================================================================

def timer_2_call(tim):
    global Counter_2
    
    # print("Timer 2 ", Counter_2)

    if Counter_2 == 0:
        print("0 - 0 - 0")
    if Counter_2 == 1:
        print("0 - 0 - 1 ")
    if Counter_2 == 2:
        print("0 - 1 - 0")
    if Counter_2 == 3:
        print("1 - 0 - 0")
    if Counter_2 > 3:
        Counter_2 = 0
    else:
        Counter_2 = Counter_2 + 1
    

# ###############################################################################
# ### Function ->                                                             ###
# ###############################################################################

def main():

    mg_def = MyDefault

    timer_1 = Timer(-1)
    timer_1.init(period=mg_def.led_blink_period, mode=Timer.PERIODIC, callback=timer_1_call)
    
    timer_2 = Timer(-1)
    timer_2.init(period=mg_def.led_step_time, mode=Timer.PERIODIC, callback=timer_2_call)

    try:
        print("Start")
        while(True):
            time.sleep(1)
            #print("Run")

    except KeyboardInterrupt:
        print("-> Keyboard Interrupt")

    finally:
        print("-> Exiting the program")
        timer_1.deinit()
        timer_2.deinit()
        usr_led.value(0)
 

    print("=== End of Main ===")

   

# ###############################################################################
# ### Main                                                                    ###
# ###############################################################################

if __name__ == "__main__":
    
    main()      # Start Main $$$

# Normal sollte das Programm hier nie ankommen !
print("___ End of Programm ___ !!!")

# ##############################################################################
