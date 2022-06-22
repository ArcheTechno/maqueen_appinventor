def on_bluetooth_connected():
    basic.show_string("Mettre la lettre de l'équipe")
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_icon(IconNames.ASLEEP)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def on_received_string(key, receivedString):
    if receivedString == "avant":
        maqueen.motor_run(maqueen.aMotors.M1, maqueen.Dir.CW, 100)
        maqueen.motor_run(maqueen.aMotors.M2, maqueen.Dir.CW, 100)
    if receivedString == "stop":
        maqueen.motor_run(maqueen.aMotors.M1, maqueen.Dir.CW, 0)
        maqueen.motor_run(maqueen.aMotors.M2, maqueen.Dir.CW, 0)
    if receivedString == "reculer":
        maqueen.motor_run(maqueen.aMotors.M1, maqueen.Dir.CCW, 100)
        maqueen.motor_run(maqueen.aMotors.M2, maqueen.Dir.CCW, 100)
    if receivedString == "droite":
        maqueen.motor_run(maqueen.aMotors.M1, maqueen.Dir.CW, 100)
        maqueen.motor_run(maqueen.aMotors.M2, maqueen.Dir.CW, 0)
    if receivedString == "gauche":
        maqueen.motor_run(maqueen.aMotors.M1, maqueen.Dir.CW, 0)
        maqueen.motor_run(maqueen.aMotors.M2, maqueen.Dir.CW, 100)
    if receivedString == "BUT":
        basic.show_string("KING!")
blockytalky.on_received_string(on_received_string)
