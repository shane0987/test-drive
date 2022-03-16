def on_button_pressed_a():
    radio.send_string("l")
    basic.show_arrow(ArrowNames.WEST)
    basic.pause(2000)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    radio.send_string("f")
    basic.show_arrow(ArrowNames.NORTH)
    basic.pause(2000)
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    if receivedString == "l":
        Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR2,
            Kitronik_Robotics_Board.MotorDirection.FORWARD,
            50)
        basic.show_arrow(ArrowNames.WEST)
    elif receivedString == "r":
        Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR1,
            Kitronik_Robotics_Board.MotorDirection.FORWARD,
            50)
        basic.show_arrow(ArrowNames.EAST)
    elif receivedString == "f":
        Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR1,
            Kitronik_Robotics_Board.MotorDirection.FORWARD,
            50)
        Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR2,
            Kitronik_Robotics_Board.MotorDirection.FORWARD,
            50)
        basic.show_arrow(ArrowNames.NORTH)
    elif receivedString == "b":
        Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR1,
            Kitronik_Robotics_Board.MotorDirection.REVERSE,
            50)
        Kitronik_Robotics_Board.motor_on(Kitronik_Robotics_Board.Motors.MOTOR2,
            Kitronik_Robotics_Board.MotorDirection.REVERSE,
            50)
        basic.show_arrow(ArrowNames.SOUTH)
    else:
        basic.show_string("ERROR")
    basic.pause(2000)
    basic.clear_screen()
    Kitronik_Robotics_Board.all_off()
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    radio.send_string("r")
    basic.show_arrow(ArrowNames.EAST)
    basic.pause(2000)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    radio.send_string("b")
    basic.show_arrow(ArrowNames.SOUTH)
    basic.pause(2000)
    basic.clear_screen()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

radio.set_group(45)