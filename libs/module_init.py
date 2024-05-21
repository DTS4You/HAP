# #############################################################################
# ### MyGlobal
# #############################################################################


class Global_Module:
    
    inc_ws2812          = False
    inc_decoder         = False
    inc_serial          = False


class Global_Default:

    led_blink_period    = 300           # Blink-Periode in (ms)
    led_step_time       = 1000          # Animation in (ms)


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