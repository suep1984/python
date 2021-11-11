import time


class TrafficLight:
    def __init__(self, color=""):
        self.__color = color

    def running(self, red, yellow, green):
        while True:
            self.__color = red
            if self.__color.lower() == "red":
                print(f'{self.__color}')
            else:
                exit()
            time.sleep(7)
            self.__color = yellow
            if self.__color.lower() == "yellow":
                print(f'{self.__color}')
            else:
                exit()
            time.sleep(2)
            self.__color = green
            if self.__color.lower() == "green":
                print(f'{self.__color}')
            else:
                exit()
            time.sleep(5)


a = TrafficLight()
a.running('RED', 'YELLOW', '3')
