# Stubs for fast_transformers_cxx (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def disable_gperf() -> None: ...
def enable_gperf(arg0: str) -> None: ...
def set_stderr_verbose_level(arg0: int) -> None: ...

class BERTEmbedding:
    def __init__(self, arg0: Tensor, arg1: Tensor, arg2: Tensor, arg3: Tensor, arg4: Tensor, arg5: float) -> None: ...
    def __call__(self, arg0: Tensor, arg1: Tensor, arg2: Tensor) -> Tensor: ...

class BertAttention:
    def __init__(self, arg0: Tensor, arg1: Tensor, arg2: Tensor, arg3: Tensor, arg4: Tensor, arg5: Tensor, arg6: Tensor, arg7: Tensor, arg8: Tensor, arg9: Tensor, arg10: int) -> None: ...
    def __call__(self, arg0: Tensor, arg1: Tensor, arg2: Tensor) -> Tensor: ...

class BertIntermediate:
    def __init__(self, arg0: Tensor, arg1: Tensor) -> None: ...
    def __call__(self, arg0: Tensor) -> Tensor: ...

class BertOutput:
    def __init__(self, arg0: Tensor, arg1: Tensor, arg2: Tensor, arg3: Tensor) -> None: ...
    def __call__(self, arg0: Tensor, arg1: Tensor) -> Tensor: ...

class BertSelfAttention:
    def __init__(self, arg0: Tensor, arg1: Tensor, arg2: Tensor, arg3: Tensor, arg4: Tensor, arg5: Tensor, arg6: int) -> None: ...
    def __call__(self, arg0: Tensor, arg1: Tensor, arg2: Tensor) -> Tensor: ...

class Tensor:
    def __init__(*args, **kwargs) -> None: ...
    def float_data(self) -> float: ...
    def from_dlpack(*args, **kwargs) -> Any: ...
    def n_dim(self) -> int: ...
    def shape(self, arg0: int) -> int: ...
    def to_dlpack(self) -> capsule: ...