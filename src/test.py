from polynomial import Polynomial
from finitefield import GF, isprime
from lagrange import Lagrange
import random
from msg_handling import MSG_Handler

BASE64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 ."
GFn = GF(97)
lagrange = Lagrange(GFn)
handler = MSG_Handler(GFn)

def vecint2type(vecs : list[list], type_ : type):
    return [[type_(point[0]), type_(point[1])] for point in vecs]

points = [[random.randint(0,GFn.p), random.randint(0,GFn.p)] for i in range(6)]

points = vecint2type(points, GFn)

poly = lagrange.interpolate(points)
print(poly)
print("\n-----\n")

# for i in range(len(points)):
#     if points[i][1]!=poly(points[i][0]):
#         raise NotImplementedError("we basically failed")
# print(r""" ____   _    ____ ____  _____ ____  _ 
# |  _ \ / \  / ___/ ___|| ____|  _ \| |
# | |_) / _ \ \___ \___ \|  _| | | | | |
# |  __/ ___ \ ___) |__) | |___| |_| |_|
# |_| /_/   \_\____/____/|_____|____/(_)""")

print("\n\n\n")

print(handler.get_str_of_points(handler.get_points_of_str("W4e&lLc?o+m1e2!1+r  13"))[::2])