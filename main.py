
#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
brain_inertial = Inertial()
front_rollers_motor_a = Motor(Ports.PORT1, False)
front_rollers_motor_b = Motor(Ports.PORT6, True)
front_rollers = MotorGroup(front_rollers_motor_a, front_rollers_motor_b)
back_roller = Motor(Ports.PORT4, True)
left_drive_smart = Motor(Ports.PORT3, 1.0, True)
right_drive_smart = Motor(Ports.PORT2, 1.0, False)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 200, 173, 76, MM, 1)
catapult = Motor(Ports.PORT7, False)
pneumatics = Pneumatic(Ports.PORT8)
touchled_10 = Touchled(Ports.PORT10)



# generating and setting random seed
def initializeRandomSeed():
    wait(100, MSEC)
    xaxis = brain_inertial.acceleration(XAXIS) * 1000
    yaxis = brain_inertial.acceleration(YAXIS) * 1000
    zaxis = brain_inertial.acceleration(ZAXIS) * 1000
    systemTime = brain.timer.system() * 100
    urandom.seed(int(xaxis + yaxis + zaxis + systemTime)) 
    
# Initialize random seed 
initializeRandomSeed()

#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
# 
#   Project:      VEXcode Project
#   Author:       VEX
#   Created:
#   Description:  VEXcode IQ Python Project
# 
# ------------------------------------------

# Library imports
from vex import *

# Begin project code
drivetrain.set_stopping(BRAKE)
TURN_WAIT_SECONDS = 0.5

# DO NOT TOUCH THIS CODE!!!!!!!!!!!!!!!!!!!!!!!
class Robot:
    def __init__(self, drive_left_velocity=85, drive_right_velocity=100, turn_velocity=40, catapult_velocity=100, front_rollers_velocity=100, back_roller_velocity=100):
        self.pneumatics_extended = True
        self.drive_left_velocity = drive_left_velocity
        self.drive_right_velocity = drive_right_velocity
        self.turn_velocity = turn_velocity
        self.catapult_velocity = catapult_velocity
        self.front_rollers_velocity = front_rollers_velocity
        self.back_roller_velocity = back_roller_velocity
        touchled_10.set_color(Color.GREEN)
        left_drive_smart.set_velocity(self.drive_left_velocity, PERCENT)
        right_drive_smart.set_velocity(self.drive_right_velocity, PERCENT)
        drivetrain.set_turn_velocity(self.turn_velocity, PERCENT)
        catapult.set_velocity(self.catapult_velocity, PERCENT)
        front_rollers.set_velocity(self.front_rollers_velocity, PERCENT)
        back_roller.set_velocity(self.back_roller_velocity, PERCENT)
    
    def drive_stop(self):
        drivetrain.stop()

    def drive_fwd(self, seconds, stop_=True):
        drivetrain.drive(FORWARD)
        if stop_:
            wait(seconds, SECONDS)
            self.drive_stop()

    def drive_rev(self, seconds, stop_=True):
        drivetrain.drive(REVERSE)
        wait(seconds, SECONDS)
        if stop_:
            self.drive_stop()
    
    def turn_right(self, degrees):
        drivetrain.turn_for(RIGHT, degrees, DEGREES)
        wait(TURN_WAIT_SECONDS, SECONDS)
    
    def turn_left(self, degrees):
        drivetrain.turn_for(LEFT, degrees, DEGREES)
        wait(TURN_WAIT_SECONDS, SECONDS)

    def rollers_fwd(self, seconds=0):
        front_rollers.spin(FORWARD)
        back_roller.spin(FORWARD)
        if seconds != 0:
            wait(seconds, SECONDS)
            front_rollers.stop()
            back_roller.stop()
    
    def rollers_rev(self, seconds=0):
        front_rollers.spin(REVERSE)
        back_roller.spin(REVERSE)
        if seconds != 0:
            wait(seconds, SECONDS)
            front_rollers.stop()
            back_roller.stop()
    
    
    def rollers_stop(self):
        front_rollers.stop()
        back_roller.stop()
    
    def catapult_fwd(self, seconds=0):
        catapult.spin(FORWARD)
        if seconds != 0:  
            wait(seconds, SECONDS)
            catapult.stop()
        wait(0.5, SECONDS)
    
    def catapult_rev(self, seconds=0):
        catapult.spin(REVERSE)
        if seconds != 0:
            wait(seconds, SECONDS)
            catapult.stop()
        wait(0.5, SECONDS)
    
    def catapult_stop(self):
        catapult.stop()
    
    def extend_pneumatics(self):
        pneumatics.extend(CYLINDER1)
        pneumatics.extend(CYLINDER2)
    
    def retract_pneumatics(self):
        pneumatics.retract(CYLINDER1)
        pneumatics.retract(CYLINDER2)
    
    def stop_all(self):
        self.drive_stop()
        self.rollers_stop()
        touchled_10.set_color(Color.RED)

def main():
    robot = Robot()
    robot.extend_pneumatics()
    robot.rollers_fwd()
    robot.drive_fwd(1)
    wait(1, SECONDS)
    robot.turn_right(87)
    robot.drive_rev(1.56, False)
    robot.retract_pneumatics()
    wait(0.5, SECONDS)
    robot.extend_pneumatics()
    robot.catapult_fwd(1.8)
    robot.rollers_fwd()
    robot.drive_stop()
    robot.drive_fwd(1.5)
    robot.turn_right(30)
    robot.drive_fwd(1.25)
    wait(0.35, SECONDS)
    robot.turn_left(30)
    robot.drive_rev(2.5, False)
    robot.retract_pneumatics()
    wait(0.5, SECONDS)
    robot.extend_pneumatics()
    robot.catapult_fwd(3)
    robot.rollers_fwd()
    robot.drive_stop()
    while True:
        robot.drive_fwd(1.7)
        wait(1, SECONDS)
        robot.drive_rev(2.5)
        robot.retract_pneumatics()
        wait(1.5, SECONDS)
        robot.catapult_rev(0.7)
        wait(1, SECONDS)
        robot.extend_pneumatics()
        robot.catapult_fwd(0.7)
        if touchled_10.pressing():
            return

touchled_10.set_color(Color.RED)
touchled_10.pressed(main)