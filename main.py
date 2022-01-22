backlight = True
list2: List[number] = []

def on_logo_pressed():
    basic.show_icon(IconNames.HEART)
    makerbit.connect_lcd(63)
    makerbit.clear_lcd1602()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_button_pressed_a():
    global backlight
    if backlight == True:
        makerbit.set_lcd_backlight(LcdBacklight.ON)
        backlight = False
    else:
        makerbit.set_lcd_backlight(LcdBacklight.OFF)
        backlight = True
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_sound_loud():
    global list2
    list2 = [1, 2, 3, 4, 5, 6]
    basic.clear_screen()
    basic.pause(500)
    basic.show_number(list2._pick_random())
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_forever():
    makerbit.clear_lcd1602()
    dht11_dht22.query_data(DHTtype.DHT11, DigitalPin.P0, True, False, True)
    if dht11_dht22.read_data_successful():
        makerbit.show_string_on_lcd1602("Humi:" + ("" + str(dht11_dht22.read_data(dataType.HUMIDITY))) + "%",
            makerbit.position1602(LcdPosition1602.POS18),
            18)
        makerbit.show_string_on_lcd1602("Temp:" + ("" + str(dht11_dht22.read_data(dataType.TEMPERATURE))) + " *C",
            makerbit.position1602(LcdPosition1602.POS2),
            18)
    else:
        makerbit.show_string_on_lcd1602("MOMENTS LATER...",
            makerbit.position1602(LcdPosition1602.POS1),
            18)
    basic.pause(5000)
basic.forever(on_forever)
