import os
import sys
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
# find root dir
root_path = os.path.split((os.path.dirname(__file__)))[0]
# set root
sys.path.append(root_path)
from Source.Config.get_input import GetInput
from Source.Services.my_math_methods import MyMethods


class Main(GetInput):
    def execute_workflow(self):
        print(self.a)
        print(self.b)
        print("Addition")
        print(MyMethods.add(self.a, self.b))
        print("Substraktion")
        print(MyMethods.sub(self.a, self.b))
        print("multiply")
        print(MyMethods.multiply(self.const1, self.a))
        print("Norm")
        print(MyMethods.norm(self.a))
        print("Skalarprodukt")
        print(MyMethods.dotp(self.a, self.b))
        print("Kreuzprodukt")
        print(MyMethods.crossp(self.a, self.b))

        #fig = plt.figure()
        #ax = plt.axes(projection="3d")
        #ax.bar3d(self.a[0], self.a[1], self.a[2], 1, 1, 1, color='aqua')
        #plt.show()
        
my_code = Main(__file__)
my_code.execute_workflow()
