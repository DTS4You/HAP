# #############################################################################
# ### MyGlobal
# #############################################################################


class Global_Module:
    
    inc_ws2812          = False
    inc_decoder         = False
    inc_serial          = False
    inc_i2c             = True


class Global_Default:

    led_blink_period    = 500          # Blink-Periode in (ms)
    led_step_time       = 200          # Animation in (ms)
    motor_delay_time    = 2000         # Motor Anlauf-Verzögerung (ms)


class Globel_State:

    led_state           = False
    anim_state          = 0
    
# #############################################################################

def main():

    print("Start Global Init")
    mg = Global_Default
    print(mg.led_blink_period)
    print(mg.led_step_time)
 


#------------------------------------------------------------------------------
#--- Main
#------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
