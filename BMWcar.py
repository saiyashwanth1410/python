from abc import ABC, abstractmethod
class modelcar(ABC):
    @abstractmethod
    def Break():
        pass
    @abstractmethod
    def Speed_up():
        pass
    def speed_down():
        pass
class X6 (modelcar):
    def __init__(self,speed=0,stop=True):
        self.speed=speed
        self.stop=stop
    def Speed_up(self):
        self.speed+=5
        self.stop=False
    def Break(self):
        self.speed=0
        self.stop=True
    def speed_down(self):
        if not self.stop:
            self.speed-=5
            if self.speed ==0:
                self.stop=True
        print(f'accelerated by 5 km/hr and current speed is {self.speed}')

