from typing import Union

def sum(a: Union[int, str], b: Union[int, str]) -> Union[int, str]:
    return a + b

sum("a", "b")

# def foo(a:int, b:str) -> dict[int,str]:
#     return {a:b}