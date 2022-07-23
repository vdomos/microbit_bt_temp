def on_bluetooth_connected():
    basic.show_string("C")
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_string("D")
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

basic.show_string("B")
bluetooth.start_temperature_service()
compteur = 0
basic.pause(2000)

def on_forever():
    global compteur
    serial.write_number(compteur)
    basic.pause(2000)
    compteur += 1
basic.forever(on_forever)
