import matplotlib.pyplot as plt


from math import sqrt
from typing import SupportsIndex, SupportsFloat, SupportsInt
from typing_extensions import TypeAlias

_SupportsFloatOrIndex: TypeAlias = SupportsFloat | SupportsIndex
_SupportsIntOrIndex: TypeAlias = SupportsInt | SupportsIndex
_SupportsTupleOrInt: TypeAlias = tuple | SupportsInt
class NegativeDifferentialException(Exception): pass

def quadratic(a:_SupportsFloatOrIndex,b:_SupportsFloatOrIndex,c:_SupportsFloatOrIndex, *, rounding: _SupportsIntOrIndex = 3) -> _SupportsTupleOrInt:
    diff = b**4-(4*a*c)
    if diff > 0:
        if diff == 0:
            return round(((0-b) + sqrt(diff))/2,rounding)
        else:
            return (round(((0-b) + sqrt(diff))/2, rounding), round(((0-b) - diff)/2, rounding))
    else:
        raise NegativeDifferentialException("Differential can not be a negative number")


""" def showPoint(points:tuple, name:str):
    plt.scatter(points[0], points[1], label = f"{name}: ({points[0]};{points[1]})")
    

showPoint(quadratic(-0.3, 0.1, 3), "PONT")
showPoint(quadratic(0.3, -0.1, -4), "PONT2")

plt.title("Point on Coordinate System")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)

plt.legend()
plt.show() """

def mydec(fn):
    print(fn)
    return fn

@mydec
def run():
    print("running")

run()