# #############################################################################
# ### MyGlobal
# #############################################################################


class Global_Module:
    
    inc_ws2812          = False
    inc_decoder         = False
    inc_serial          = False


class Global_Default:

    led_blink_period    = 300           # Blink-Periode in (ms)
    led_step_time       = 500           # Animation in (ms)

def main():

    print("Start Global Init")
    mg = Global_Default
    print(mg.led_blink_period)
    print(mg.led_blink_period)
 


#------------------------------------------------------------------------------
#--- Main
#------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
