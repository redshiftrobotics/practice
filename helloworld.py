import wpilib
from wpilib.drive import DifferentialDrive
from networktables import NetworkTables
from ctre import WPI_TalonSRX, ControlMode, NeutralMode, FeedbackDevice

talon = WPI_TalonSRX(0)

print(talon)