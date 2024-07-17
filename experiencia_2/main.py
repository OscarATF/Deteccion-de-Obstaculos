#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()
mi=Motor(Port.C)
md=Motor(Port.B)
robot=DriveBase(mi,md,55.5,104)
ultraS=UltrasonicSensor(Port.S4)

while True:
    ev3.light.on(Color.RED)
    mi.run(400)
    md.run(400)
    sensorU = ultraS.distance()

    if sensorU < 200:
        ev3.light.on(Color.ORANGE)
        robot.stop()
        ev3.speaker.beep(200)
        mi.run(-400)
        md.run(-400)
        wait(1200)
        mi.run(0)
        md.run(300)
        wait(1270)