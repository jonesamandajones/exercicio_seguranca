


def math_module():
    try:
        import mathmatics
        print(math.sqrt(25))
    except ModuleNotFoundError:
        import math
        print(ModuleNotFoundError, math.sqrt(25))
        
print(math_module())
