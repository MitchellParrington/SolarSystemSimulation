
def ParseEnvArgs(args:tuple, kwargs:dict[str:str]) -> dict[str:str]:
    print(args);
    print(kwargs);
    if len(args) < 2:
        raise RuntimeError("Not enough args passed");