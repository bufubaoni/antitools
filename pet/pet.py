# -*- coding: utf-8 -*-
from time import sleep
import timeout_decorator
from timeout_decorator import TimeoutError


class Pet(object):
    motion = 0
    thirsty = 0
    hunger = 0

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f"I'm {self.name}~!"

    def feed(self, food):
        self.motion += food.motion
        self.hunger += food.hunger
        return f'{food.name} taste good~!'

    def drink(self):
        self.motion += 3
        self.thirsty += 5
        return f'Thank you'

    def fun(self, fun):
        self.motion += fun.motion
        self.thirsty -= fun.warter
        self.hunger -= fun.hunger
        return f'Love you'


class Food(object):

    def __init__(self, name, motion, hunger):
        self.motion = motion
        self.hunger = hunger
        self.name = name


class Fun(object):
    def __init__(self, motion, hunger, thirsty):
        self.motion = motion
        self.thirsty = thirsty
        self.hunger = hunger


@timeout_decorator.timeout(10)
def timeout_input(input_str):
    return input(input_str)


class Engine(object):
    pet = None

    def init_env(self):
        name = input('please input you pet name:')
        self.pet = Pet(name)

    def run(self):
        while True:
            try:
                user_action = timeout_input('what do you want:')
                method, arg = user_action.split(',')
                pet_method = self.pet.__getattribute__(method)
                pet_method()
            except TimeoutError:
                print(self.pet.say_hello())


if __name__ == "__main__":
    engine = Engine()
    engine.init_env()
    engine.run()
