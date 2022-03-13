input.onButtonPressed(Button.A, function () {
    radio.sendString("l")
    basic.showArrow(ArrowNames.West)
    basic.pause(2000)
    basic.clearScreen()
})
input.onButtonPressed(Button.AB, function () {
    radio.sendString("f")
    basic.showArrow(ArrowNames.North)
    basic.pause(2000)
    basic.clearScreen()
})
radio.onReceivedString(function (receivedString) {
    if (receivedString == "l") {
        Kitronik_Robotics_Board.motorOn(Kitronik_Robotics_Board.Motors.Motor2, Kitronik_Robotics_Board.MotorDirection.Forward, 50)
        basic.showArrow(ArrowNames.West)
    } else if (receivedString == "r") {
        Kitronik_Robotics_Board.motorOn(Kitronik_Robotics_Board.Motors.Motor1, Kitronik_Robotics_Board.MotorDirection.Forward, 50)
        basic.showArrow(ArrowNames.East)
    } else if (receivedString == "f") {
        Kitronik_Robotics_Board.motorOn(Kitronik_Robotics_Board.Motors.Motor1, Kitronik_Robotics_Board.MotorDirection.Forward, 50)
        Kitronik_Robotics_Board.motorOn(Kitronik_Robotics_Board.Motors.Motor2, Kitronik_Robotics_Board.MotorDirection.Forward, 50)
        basic.showArrow(ArrowNames.North)
    } else if (receivedString == "b") {
        Kitronik_Robotics_Board.motorOn(Kitronik_Robotics_Board.Motors.Motor1, Kitronik_Robotics_Board.MotorDirection.Reverse, 50)
        Kitronik_Robotics_Board.motorOn(Kitronik_Robotics_Board.Motors.Motor2, Kitronik_Robotics_Board.MotorDirection.Reverse, 50)
        basic.showArrow(ArrowNames.South)
    } else {
        basic.showString("ERROR")
    }
    basic.pause(2000)
    basic.clearScreen()
    Kitronik_Robotics_Board.allOff()
})
input.onButtonPressed(Button.B, function () {
    radio.sendString("r")
    basic.showArrow(ArrowNames.East)
    basic.pause(2000)
    basic.clearScreen()
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    radio.sendString("b")
    basic.showArrow(ArrowNames.South)
    basic.pause(2000)
    basic.clearScreen()
})
radio.setGroup(45)
