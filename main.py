sensordetected = 0
obsercle = 0

def on_forever():
    global sensordetected, obsercle
    reromicro.read_line_sensors()
    if reromicro.line_sensor_detects_line(LineSensors.LEFT) and (reromicro.line_sensor_detects_line(LineSensors.CENTER) and reromicro.line_sensor_detects_line(LineSensors.RIGHT)):
        sensordetected += 1
        if sensordetected == 1:
            reromicro.brake()
            basic.pause(300)
            reromicro.move_forward(47)
            basic.pause(20)
            reromicro.run_motor(Motors.RIGHT, -47)
            reromicro.run_motor(Motors.LEFT, 47)
            basic.pause(200)
            reromicro.brake()
            basic.pause(200)
        elif sensordetected == 2:
            reromicro.brake()
            basic.pause(300)
            reromicro.move_forward(47)
            basic.pause(300)
        elif sensordetected == 3:
            reromicro.brake()
            basic.pause(300)
            reromicro.move_forward(47)
            basic.pause(200)
        elif sensordetected == 4:
            reromicro.brake()
            basic.pause(200)
            reromicro.run_motor(Motors.RIGHT, -47)
            reromicro.run_motor(Motors.LEFT, 47)
            basic.pause(200)
            reromicro.brake()
            basic.pause(200)
        elif sensordetected == 5:
            reromicro.brake()
    elif reromicro.line_sensor_detects_line(LineSensors.CENTER) and reromicro.line_sensor_detects_line(LineSensors.LEFT):
        reromicro.run_motor(Motors.LEFT, 32)
        reromicro.run_motor(Motors.RIGHT, 47)
    elif reromicro.line_sensor_detects_line(LineSensors.CENTER) and reromicro.line_sensor_detects_line(LineSensors.RIGHT):
        reromicro.run_motor(Motors.LEFT, 47)
        reromicro.run_motor(Motors.RIGHT, 32)
    elif reromicro.line_sensor_detects_line(LineSensors.CENTER):
        reromicro.move_forward(47)
    elif reromicro.line_sensor_detects_line(LineSensors.LEFT):
        reromicro.run_motor(Motors.LEFT, 0)
        reromicro.run_motor(Motors.RIGHT, 47)
    elif reromicro.line_sensor_detects_line(LineSensors.RIGHT):
        reromicro.run_motor(Motors.RIGHT, 0)
        reromicro.run_motor(Motors.LEFT, 47)
    if reromicro.read_ultrasonic() <= 3.5:
        obsercle += 1
        reromicro.brake()
        music.play_tone(988, music.beat(BeatFraction.WHOLE))
        basic.pause(200)
        basic.show_number(obsercle)
        basic.clear_screen()
    else:
        reromicro.read_line_sensors()
        if reromicro.line_sensor_detects_line(LineSensors.LEFT) and (reromicro.line_sensor_detects_line(LineSensors.CENTER) and reromicro.line_sensor_detects_line(LineSensors.RIGHT)):
            reromicro.move_forward(47)
        elif reromicro.line_sensor_detects_line(LineSensors.CENTER) and reromicro.line_sensor_detects_line(LineSensors.LEFT):
            reromicro.run_motor(Motors.LEFT, 32)
            reromicro.run_motor(Motors.RIGHT, 47)
        elif reromicro.line_sensor_detects_line(LineSensors.CENTER) and reromicro.line_sensor_detects_line(LineSensors.RIGHT):
            reromicro.run_motor(Motors.LEFT, 47)
            reromicro.run_motor(Motors.RIGHT, 32)
        elif reromicro.line_sensor_detects_line(LineSensors.CENTER):
            reromicro.move_forward(47)
        elif reromicro.line_sensor_detects_line(LineSensors.LEFT):
            reromicro.run_motor(Motors.LEFT, 0)
            reromicro.run_motor(Motors.RIGHT, 47)
        elif reromicro.line_sensor_detects_line(LineSensors.RIGHT):
            reromicro.run_motor(Motors.RIGHT, 0)
            reromicro.run_motor(Motors.LEFT, 47)
        else:
            reromicro.brake
basic.forever(on_forever)
