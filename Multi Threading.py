from threading import *
from time import sleep
class A(Thread):
    def run(self):
        for i in range(6):
            print("A")
            sleep(2)
class B(Thread):
    def run(self):
        for i in range(6):
            print("B")
            sleep(2)
a=A()
b=B()
a.start()
sleep(0.5)
b.start()
a.join()
b.join()
print("end:")
