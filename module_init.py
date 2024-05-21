# #############################################################################
# ### MyGlobal
# #############################################################################


class Global_Module:
    
    inc_ws2812          = True
    inc_decoder         = True
    inc_serial          = True


class Global_WS2812:

    numpix_1            = 12            # Anzahl LEDs im 1. Stripe
    numpix_2            = 12            # Anzahl LEDs im 2. Stripe
    numpix_3            = 12            # Anzahl LEDs im 3. Stripe
    numpix_4            = 12            # Anzahl LEDs im 4. Stripe

    seg_01_strip        = 0             #  1. Ledsegment -> Stripe      # 1. LED hinterer Teil
    seg_01_start        = 0             #  1. Ledsegment -> Start
    seg_01_count        = 1             #  1. Ledsegment -> Anzahl

    seg_02_strip        = 0             #  2. Ledsegment -> Stripe      # 2. LED hinterer Teil
    seg_02_start        = 1             #  2. Ledsegment -> Start
    seg_02_count        = 1             #  2. Ledsegment -> Anzahl

    seg_03_strip        = 0             #  3. Ledsegment -> Stripe      # 3. LED hinterer Teil
    seg_03_start        = 2             #  3. Ledsegment -> Start
    seg_03_count        = 1             #  3. Ledsegment -> Anzahl
    
    seg_04_strip        = 0             #  4. Ledsegment -> Stripe      # 4. LED hinterer Teil
    seg_04_start        = 3             #  4. Ledsegment -> Start
    seg_04_count        = 1             #  4. Ledsegment -> Anzahl

    seg_05_strip        = 0             #  5. Ledsegment -> Stripe      # 5. LED hinterer Teil
    seg_05_start        = 4             #  5. Ledsegment -> Start
    seg_05_count        = 1             #  5. Ledsegment -> Anzahl
    
    seg_06_strip        = 0             #  6. Ledsegment -> Stripe      # 6. LED hinterer Teil
    seg_06_start        = 5             #  6. Ledsegment -> Start
    seg_06_count        = 1             #  6. Ledsegment -> Anzahl
    
    seg_07_strip        = 0             #  7. Ledsegment -> Stripe      # 7. LED hinterer Teil
    seg_07_start        = 6             #  7. Ledsegment -> Start
    seg_07_count        = 1             #  7. Ledsegment -> Anzahl

    seg_08_strip        = 0             #  8. Ledsegment -> Stripe      # 8. LED hinterer Teil
    seg_08_start        = 7             #  8. Ledsegment -> Start
    seg_08_count        = 1             #  8. Ledsegment -> Anzahl
    
    seg_09_strip        = 0             #  9. Ledsegment -> Stripe      # 9. LED hinterer Teil
    seg_09_start        = 8             #  9. Ledsegment -> Start
    seg_09_count        = 1             #  9. Ledsegment -> Anzahl
    
    seg_10_strip        = 1             # 10. Ledsegment -> Stripe      # 1. LED linker Teil
    seg_10_start        = 0             # 10. Ledsegment -> Start
    seg_10_count        = 1             # 10. Ledsegment -> Anzahl
    
    seg_11_strip        = 1             # 11. Ledsegment -> Stripe      # 2. LED linker Teil
    seg_11_start        = 1             # 11. Ledsegment -> Start
    seg_11_count        = 1             # 11. Ledsegment -> Anzahl

    seg_12_strip        = 1             # 12. Ledsegment -> Stripe      # 3. LED linker Teil
    seg_12_start        = 2             # 12. Ledsegment -> Start
    seg_12_count        = 1             # 12. Ledsegment -> Anzahl

    seg_13_strip        = 1             # 13. Ledsegment -> Stripe      # 4. LED linker Teil
    seg_13_start        = 3             # 13. Ledsegment -> Start
    seg_13_count        = 1             # 13. Ledsegment -> Anzahl

    seg_14_strip        = 1             # 14. Ledsegment -> Stripe      # 5. LED linker Teil
    seg_14_start        = 4             # 14. Ledsegment -> Start
    seg_14_count        = 1             # 14. Ledsegment -> Anzahl
    
    seg_15_strip        = 1             # 15. Ledsegment -> Stripe      # 6. LED linker Teil
    seg_15_start        = 5             # 15. Ledsegment -> Start
    seg_15_count        = 1             # 15. Ledsegment -> Anzahl

    seg_16_strip        = 2             # 16. Ledsegment -> Stripe      # 1. LED rechter Teil
    seg_16_start        = 0             # 16. Ledsegment -> Start
    seg_16_count        = 1             # 16. Ledsegment -> Anzahl
    
    seg_17_strip        = 2             # 17. Ledsegment -> Stripe      # 2. LED rechter Teil
    seg_17_start        = 1             # 17. Ledsegment -> Start
    seg_17_count        = 1             # 17. Ledsegment -> Anzahl
    
    seg_18_strip        = 2             # 18. Ledsegment -> Stripe      # 3. LED rechter Teil
    seg_18_start        = 2             # 18. Ledsegment -> Start
    seg_18_count        = 1             # 18. Ledsegment -> Anzahl

    seg_19_strip        = 2             # 19. Ledsegment -> Stripe      # 4. LED rechter Teil
    seg_19_start        = 3             # 19. Ledsegment -> Start
    seg_19_count        = 1             # 19. Ledsegment -> Anzahl
    
    seg_20_strip        = 2             # 20. Ledsegment -> Stripe      # 5. LED rechter Teil
    seg_20_start        = 4             # 20. Ledsegment -> Start
    seg_20_count        = 1             # 20. Ledsegment -> Anzahl
    
    seg_21_strip        = 2             # 21. Ledsegment -> Stripe      # 6. LED rechter Teil
    seg_21_start        = 5             # 21. Ledsegment -> Start
    seg_21_count        = 1             # 21. Ledsegment -> Anzahl
    
    seg_22_strip        = 2             # 22. Ledsegment -> Stripe
    seg_22_start        = 6             # 22. Ledsegment -> Start
    seg_22_count        = 1             # 22. Ledsegment -> Anzahl

    seg_23_strip        = 2             # 23. Ledsegment -> Stripe
    seg_23_start        = 7             # 23. Ledsegment -> Start
    seg_23_count        = 1             # 23. Ledsegment -> Anzahl
    
    seg_24_strip        = 2             # 24. Ledsegment -> Stripe
    seg_24_start        = 8             # 24. Ledsegment -> Start
    seg_24_count        = 1             # 24. Ledsegment -> Anzahl

    seg_25_strip        = 2             # 25. Ledsegment -> Stripe
    seg_25_start        = 9             # 25. Ledsegment -> Start
    seg_25_count        = 1             # 25. Ledsegment -> Anzahl

    seg_26_strip        = 2             # 26. Ledsegment -> Stripe
    seg_26_start        = 10            # 26. Ledsegment -> Start
    seg_26_count        = 1             # 26. Ledsegment -> Anzahl
    
    seg_27_strip        = 2             # 27. Ledsegment -> Stripe
    seg_27_start        = 11            # 27. Ledsegment -> Start
    seg_27_count        = 1             # 27. Ledsegment -> Anzahl

    seg_28_strip        = 2             # 28. Ledsegment -> Stripe
    seg_28_start        = 12            # 28. Ledsegment -> Start
    seg_28_count        = 1             # 28. Ledsegment -> Anzahl
    
    seg_29_strip        = 2             # 29. Ledsegment -> Stripe
    seg_29_start        = 13            # 29. Ledsegment -> Start
    seg_29_count        = 1             # 29. Ledsegment -> Anzahl
    
    seg_30_strip        = 2             # 30. Ledsegment -> Stripe
    seg_30_start        = 14            # 30. Ledsegment -> Start
    seg_30_count        = 1             # 30. Ledsegment -> Anzahl

    seg_31_strip        = 2             # 31. Ledsegment -> Stripe
    seg_31_start        = 15            # 31. Ledsegment -> Start
    seg_31_count        = 1             # 31. Ledsegment -> Anzahl
    
    seg_32_strip        = 2             # 32. Ledsegment -> Stripe
    seg_32_start        = 7             # 32. Ledsegment -> Start
    seg_32_count        = 1             # 32. Ledsegment -> Anzahl
    
    seg_33_strip        = 2             # 33. Ledsegment -> Stripe
    seg_33_start        = 8             # 33. Ledsegment -> Start
    seg_33_count        = 1             # 33. Ledsegment -> Anzahl
    
    seg_34_strip        = 2             # 34. Ledsegment -> Stripe
    seg_34_start        = 9             # 34. Ledsegment -> Start
    seg_34_count        = 1             # 34. Ledsegment -> Anzahl

    seg_35_strip        = 2             # 35. Ledsegment -> Stripe
    seg_35_start        = 10            # 35. Ledsegment -> Start
    seg_35_count        = 1             # 35. Ledsegment -> Anzahl
    
    seg_36_strip        = 2             # 36. Ledsegment -> Stripe
    seg_36_start        = 11            # 36. Ledsegment -> Start
    seg_36_count        = 1             # 36. Ledsegment -> Anzahl

# -----------------------------------------------------------------------------

    seg_37_strip        = 3             # 37. Ledsegment -> Stripe
    seg_37_start        = 0             # 37. Ledsegment -> Start
    seg_37_count        = 16            # 37. Ledsegment -> Anzahl

# -----------------------------------------------------------------------------

    color_def           = (  0,  0,  5)
    color_off           = (  0,  0,  0)
    color_on            = (100,100,100)
    color_dot           = ( 50, 50, 50)
    color_blink_on      = (100,100,100)
    color_blink_off     = ( 30, 30, 30)


class Global_Default:

    blink_freq          = 3.0           # Blink Frequenz
    

def main():

    print("Start Global Init")
    mg = Global_WS2812
    print(mg.numpix_1)
    print(mg.numpix_2)
    print(mg.seg_01_strip, mg.seg_01_start, mg.seg_01_count)
    print(mg.seg_02_strip, mg.seg_02_start, mg.seg_02_count)


#------------------------------------------------------------------------------
#--- Main
#------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
