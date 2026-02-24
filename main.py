def on_forever():
    if input.pin_is_pressed(TouchPin.P0):
        basic.show_icon(IconNames.YES)
    else:
        basic.show_icon(IconNames.NO)
basic.forever(on_forever)
