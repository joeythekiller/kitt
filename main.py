def on_button_pressed_a():
    global row, position, direction, bounceCount
    row = randint(0, 4)
    position = 4
    direction = -1
    bounceCount = 0
    moveLED()
input.on_button_pressed(Button.A, on_button_pressed_a)

def moveLED():
    global position, bounceCount, direction
    basic.clear_screen()
    led.plot(position, row)
    basic.pause(200)
    position += direction
    if position < 0:
        radio.send_value("position", 4)
    elif position > 4:
        bounceCount += 1
        if bounceCount >= 10:
            basic.show_icon(IconNames.HAPPY)
            return
        direction = -1
        position = 4
    moveLED()

def on_received_value(name, value):
    global position, direction
    if name == "position":
        position = value
        direction = 1
        basic.clear_screen()
        led.plot(position, row)
radio.on_received_value(on_received_value)

bounceCount = 0
row = 0
direction = 0
position = 0
position = 4
direction = -1
radio.set_group(1)