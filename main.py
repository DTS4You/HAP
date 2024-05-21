######################################################
### Main-Program                                   ###
### Projekt: HAP-Messemodell                       ###
### Version: 1.00                                  ###
######################################################
import time # type: ignore
from machine import Pin, Timer # type: ignore
from libs.module_init import Global_Default as MyDefault
from libs.module_init import Globel_State as MyState
from libs.module_init import Global_Module as MyModule

usr_led = Pin(25, Pin.OUT)

Counter_1 = 0
Counter_2 = 0


# ==============================================================================

def timer_1_call(tim):
    global Counter_1
    # print("Timer 1 Call")

    if Counter_1 == 1:
        mg_state.led_state = True
        usr_led.value(True)
        MyI2C.gpio.set_output(4, True)
        MyI2C.gpio.set_output(5, True)
        Counter_1 = 0
    else:
        mg_state.led_state = False
        usr_led.value(False)
        MyI2C.gpio.set_output(4, False)
        MyI2C.gpio.set_output(5, False)
        Counter_1 = Counter_1 + 1
 
# ==============================================================================

def timer_2_call(tim):
    global Counter_2
    # print("Timer 2 ", Counter_2)
    led_decode(Counter_2)
    if Counter_2 == 3:
        Counter_2 = 0
    else:
        Counter_2 = Counter_2 + 1


def led_decode(value):
    # print(value)
    if value == 0:
        MyI2C.gpio.set_output(0, False)
        MyI2C.gpio.set_output(1, False)
        MyI2C.gpio.set_output(2, False)
    if value == 1:
        MyI2C.gpio.set_output(0, True)
        MyI2C.gpio.set_output(1, False)
        MyI2C.gpio.set_output(2, False)
    if value == 2:
        MyI2C.gpio.set_output(0, False)
        MyI2C.gpio.set_output(1, True)
        MyI2C.gpio.set_output(2, False)
    if value == 3:
        MyI2C.gpio.set_output(0, False)
        MyI2C.gpio.set_output(1, False)
        MyI2C.gpio.set_output(2, True)

# ###############################################################################
# ### Function ->                                                             ###
# ###############################################################################

def main():
    global mg_def
    global mg_state

    mg_def = MyDefault
    mg_state = MyState

    #print(mg_def.led_blink_period)
    #print(mg_def.led_step_time)

    MyI2C.i2c_setup()

    timer_1 = Timer(-1)
    timer_1.init(period=mg_def.led_blink_period, mode=Timer.PERIODIC, callback=timer_1_call)
    
    timer_2 = Timer(-1)
    timer_2.init(period=mg_def.led_step_time, mode=Timer.PERIODIC, callback=timer_2_call)

    try:
        print("Start")
        MyI2C.gpio.set_output(6, True)      # Motor 1 an
        MyI2C.gpio.set_output(7, True)      # Motor 2 an
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
        for i in range(0,8):                # Alle Ausgänge aus
            MyI2C.gpio.set_output(i, False)
 

    print("=== End of Main ===")

   

# ###############################################################################
# ### Main                                                                    ###
# ###############################################################################

if __name__ == "__main__":

    mg_inc = MyModule

    if mg_inc.inc_i2c == True:
        print("Load Module -> I2C")
        import libs.module_i2c as MyI2C
        
    main()      # Start Main $$$

# Normal sollte das Programm hier nie ankommen !
print("___ End of Programm ___ !!!")

# ##############################################################################
