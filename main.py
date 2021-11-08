def on_button_pressed_a():
    basic.show_number(5)
    basic.pause(500)
    basic.show_number(4)
    basic.pause(500)
    basic.show_number(3)
    basic.pause(500)
    basic.show_number(2)
    basic.pause(500)
    basic.show_number(1)
    basic.pause(500)
    basic.show_number(0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.show_string("warning!!")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    global dice
    dice = randint(1, 6)
    if dice == 1:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
    if dice == 2:
        basic.show_leds("""
            . . . . .
                        . . . # .
                        . . . . .
                        . # . . .
                        . . . . .
        """)
    if dice == 3:
        basic.show_leds("""
            . . . . .
                        . . . # .
                        . . # . .
                        . # . . .
                        . . . . .
        """)
    if dice == 4:
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . . . . .
                        . # . # .
                        . . . . .
        """)
    if dice == 5:
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . . # . .
                        . # . # .
                        . . . . .
        """)
    if dice == 6:
        basic.show_leds("""
            . . . . .
                        . # # # .
                        . . . . .
                        . # # # .
                        . . . . .
        """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_icon(IconNames.HAPPY)
    basic.pause(500)
    basic.show_icon(IconNames.SAD)
input.on_button_pressed(Button.B, on_button_pressed_b)

dice = 0
basic.show_number(3518)

def on_forever():
    if input.temperature() >= 30:
        basic.show_string("HOT")
    if input.light_level() >= 150:
        pins.digital_write_pin(DigitalPin.P1, 1)
    else:
        pins.digital_write_pin(DigitalPin.P1, 0)
basic.forever(on_forever)
