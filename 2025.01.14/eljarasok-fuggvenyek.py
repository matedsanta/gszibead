from math import sqrt
from typing import SupportsIndex, SupportsFloat, SupportsInt
from typing_extensions import TypeAlias

_SupportsFloatOrIndex: TypeAlias = SupportsFloat | SupportsIndex
_SupportsIntOrIndex: TypeAlias = SupportsInt | SupportsIndex
_SupportsTupleOrInt: TypeAlias = tuple | SupportsInt
class NegativeDifferentialException(Exception):
    pass

def quadratic(a:_SupportsFloatOrIndex,b:_SupportsFloatOrIndex,c:_SupportsFloatOrIndex, *, rounding: _SupportsIntOrIndex = 3) -> _SupportsTupleOrInt:
    diff = b**4-(4*a*c)
    if diff > 0:
        if diff == 0:
            return round(((0-b) + sqrt(diff))/2,rounding)
        else:
            return (round(((0-b) + sqrt(diff))/2, rounding), round(((0-b) - diff)/2, rounding))
    else:
        raise NegativeDifferentialException("Differential can not be a negative number")
    
print(quadratic(-3,6,-0, rounding=1))


def negyzetek(max: _SupportsIntOrIndex) -> list[int]:
    return [f**2 for f in range(max+1)] 

for i in range(10):
    print(negyzetek(i))

    