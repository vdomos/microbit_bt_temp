bluetooth.onBluetoothConnected(function on_bluetooth_connected() {
    basic.showString("C")
})
bluetooth.onBluetoothDisconnected(function on_bluetooth_disconnected() {
    basic.showString("D")
})
basic.showString("B")
bluetooth.startTemperatureService()
let compteur = 0
basic.pause(2000)
basic.forever(function on_forever() {
    
    serial.writeNumber(compteur)
    basic.pause(2000)
    compteur += 1
})
