def on_gesture_screen_down():
    global Numero
    Numero = 0
input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

def on_gesture_shake():
    global Numero
    Numero = randint(0, 6)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

Numero = 0
basic.show_arrow(ArrowNames.NORTH)
Numero = 0

def on_forever():
    if Numero > 0:
        basic.show_number(Numero)
    else:
        basic.clear_screen()
basic.forever(on_forever)