class Switch:
    ''' The INVOKER class'''

    def __init__(self, flipUpCmd, flipDownCmd):
        self.__flipUpCommand = flipUpCmd
        self.__flipDownCommand = flipDownCmd

    def flipUp(self):
        self.__flipUpCommand.execute()

    def flipDown(self):
        self.__flipDownCommand.execute()


class Light:
    '''The RECEIVER Class'''

    def turnOn(self):
        print("The light is on")

    def turnOff(self):
        print("The light is off")


class Command:
    """The Command Abstrace class"""

    def __init__(self):
        pass

    def execute(self):
        pass


class FlipUpCommand(Command):
    '''The Command class for turning on the light'''

    def __init__(self, light):
        self.__light = light

    def execute(self):
        self.__light.turnOn()


class FileDownCommand(Command):
    '''The Command class for turning off the light'''

    def __init__(self, light):
        Command.__init__(self)
        self.__light = light

    def execute(self):
        self.__light.turnOff()


class LightSwitch:
    '''The Client Class'''

    def __init__(self):
        self.__lamp = Light()
        self.__switchUp = FlipUpCommand(self.__lamp)
        self.__switchDown = FileDownCommand(self.__lamp)
        self.__switch = Switch(self.__switchUp, self.__switchDown)

    def switch(self, cmd):
        cmd = cmd.strip().upper()
        try:
            if cmd == "ON":
                self.__switch.flipUp()
            elif cmd == "OFF":
                self.__switch.flipDown()
            else:
                print('Argument "ON" or "OFF" is required')
        except Exception as msg:
            print("Exception occured:%s" % msg)


# Execute if the file is run as a script and not imported as a module
if __name__ == "__main__":
    lightSwitch = LightSwitch()
    print("Switch ON test")
    lightSwitch.switch("ON")
    print("Switch OFF test")
    lightSwitch.switch("OFF")
    print("Invalid Command test")
    lightSwitch.switch("****")
