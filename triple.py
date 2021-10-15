def tripler(funt):
    def init(*args):
        funt(*args)
        funt(*args)
        funt(*args)
    return init
@tripler
def printfunc():
    print("Function printed three time")
printfunc()