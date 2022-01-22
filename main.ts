input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.showIcon(IconNames.Heart)
    makerbit.connectLcd(63)
    makerbit.clearLcd1602()
})
input.onButtonPressed(Button.A, function () {
    if (backlight == true) {
        makerbit.setLcdBacklight(LcdBacklight.On)
        backlight = false
    } else {
        makerbit.setLcdBacklight(LcdBacklight.Off)
        backlight = true
    }
})
input.onSound(DetectedSound.Loud, function () {
    list2 = [
    1,
    2,
    3,
    4,
    5,
    6
    ]
    basic.clearScreen()
    basic.pause(500)
    basic.showNumber(list2._pickRandom())
})
let list2: number[] = []
let backlight = false
backlight = true
basic.forever(function () {
    makerbit.clearLcd1602()
    dht11_dht22.queryData(
    DHTtype.DHT11,
    DigitalPin.P0,
    true,
    false,
    true
    )
    if (dht11_dht22.readDataSuccessful()) {
        makerbit.showStringOnLcd1602("Humi:" + ("" + dht11_dht22.readData(dataType.humidity)) + "%", makerbit.position1602(LcdPosition1602.Pos18), 18)
        makerbit.showStringOnLcd1602("Temp:" + ("" + dht11_dht22.readData(dataType.temperature)) + " *C", makerbit.position1602(LcdPosition1602.Pos2), 18)
    } else {
        makerbit.showStringOnLcd1602("MOMENTS LATER...", makerbit.position1602(LcdPosition1602.Pos1), 18)
    }
    basic.pause(10000)
})
