input.onButtonPressed(Button.A, function () {
    row = randint(0, 4)
    position = 4
    direction = -1
    bounceCount = 0
    moveLED()
})
function moveLED () {
    basic.clearScreen()
    led.plot(position, row)
    basic.pause(200)
    position += direction
    if (position < 0) {
        radio.sendValue("position", 4)
    } else if (position > 4) {
        bounceCount += 1
        if (bounceCount >= 10) {
            basic.showIcon(IconNames.Happy)
            return
        }
        direction = -1
        position = 4
    }
    moveLED()
}
radio.onReceivedValue(function (name, value) {
    if (name == "position") {
        position = value
        direction = 1
        basic.clearScreen()
        led.plot(position, row)
    }
})
let bounceCount = 0
let row = 0
let direction = 0
let position = 0
position = 4
direction = -1
radio.setGroup(1)
