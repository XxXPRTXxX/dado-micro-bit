input.onGesture(Gesture.ScreenDown, function () {
    Numero = 0
})
input.onGesture(Gesture.Shake, function () {
    Numero = randint(0, 6)
})
let Numero = 0
Numero = 0
basic.forever(function () {
    if (Numero > 0) {
        basic.showNumber(Numero)
    } else {
        basic.clearScreen()
    }
})
