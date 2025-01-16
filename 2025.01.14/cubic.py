from math import sqrt
from typing import SupportsIndex, SupportsFloat, SupportsInt
from typing_extensions import TypeAlias

_SupportsFloatOrIndex: TypeAlias = SupportsFloat | SupportsIndex
_SupportsIntOrIndex: TypeAlias = SupportsInt | SupportsIndex
_SupportsTupleOrInt: TypeAlias = tuple | SupportsInt
class NegativeDifferentialException(Exception):
    pass

def cubicEqn(a:_SupportsFloatOrIndex, b:_SupportsFloatOrIndex, c:_SupportsFloatOrIndex, d:_SupportsFloatOrIndex) -> _SupportsFloatOrIndex:
    pass