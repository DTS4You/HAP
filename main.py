######################################################
### Main-Program                                   ###
### Projekt: HAP-Messemodell                       ###
### Version: 1.02                                  ###
### - Fernbedienung hinzu                          ###
######################################################
import time # type: ignore
from machine import Pin, Timer # type: ignore
from libs.module_init import Global_Default as MyDefault
from libs.module_init import Globel_State as MyState
from libs.module_init import Global_Module as MyModule

# Define Pins
usr_led = Pin(25, Pin.OUT)                          # OnBoard LED   -> Output
input_pin = Pin(10, mode=Pin.IN, pull=Pin.PULL_UP)  # RF-Relais     -> Input, aktiv low

Counter_1 = 0

blink_state = False

# ==============================================================================

def led_sequence():
    global Counter_1
    # print("Timer 2 ", Counter_2)
    if Counter_1 == 3:
        Counter_1 = 0
    else:
        Counter_1 = Counter_1 + 1

# ==============================================================================

def timer_motor_call(tim):
    MyI2C.gpio.set_output(6, True)      # Motor 1 an
    MyI2C.gpio.set_output(7, True)      # Motor 2 an

# ==============================================================================

def timer_blink_call(tim):
    global blink_state
    blink_state = not blink_state
    usr_led.value(blink_state)
    led_decode(Counter_1, blink_state)

# ==============================================================================

def led_decode(step, blink):
    # print(value)
    if blink:
        if step == 0:
            MyI2C.gpio.set_output(0, False)
            MyI2C.gpio.set_output(1, False)
            MyI2C.gpio.set_output(2, False)
        if step == 1:
            MyI2C.gpio.set_output(0, True)
            MyI2C.gpio.set_output(1, False)
            MyI2C.gpio.set_output(2, False)
        if step == 2:
            MyI2C.gpio.set_output(0, False)
            MyI2C.gpio.set_output(1, True)
            MyI2C.gpio.set_output(2, False)
        if step == 3:
            MyI2C.gpio.set_output(0, False)
            MyI2C.gpio.set_output(1, False)
            MyI2C.gpio.set_output(2, True)
    else:
        MyI2C.gpio.set_output(0, False)
        MyI2C.gpio.set_output(1, False)
        MyI2C.gpio.set_output(2, False)

# ==============================================================================

class input_state:
    def __init__(self):
        self.state_now  = False
        self.state_last = False
    
    def read(self, value):
        self.state_now = value
        if self.state_now != self.state_last:
            self.state_last = self.state_now
            if self.state_last:
                #print("On")
                return True
            else:
                #print("Off")
                pass
        else:
            pass
        return False
# ###############################################################################
# ### Main - Function ->                                                      ###
# ###############################################################################

def main():
    global mg_def
    global mg_state

    mg_def = MyDefault
    mg_state = MyState

    button_1 = input_state()

    MyI2C.i2c_setup()

    timer_1 = Timer(-1)         # Blink-Timer
    timer_1.init(period=mg_def.led_blink_period, mode=Timer.PERIODIC, callback=timer_blink_call)

    timer_2 = Timer(-1)         # Motor-Timer
    timer_2.init(period=mg_def.motor_delay_time, mode=Timer.ONE_SHOT, callback=timer_motor_call)

    try:
        print("Start")
        while(True):                # Schleife für die Ewigkeit !!!
            if button_1.read(not input_pin()):
                #print("On")
                led_sequence()
            time.sleep_ms(20)
            
            #print(input_pin.value())

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
