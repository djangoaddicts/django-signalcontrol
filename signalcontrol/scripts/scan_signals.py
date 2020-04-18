

def scan_signals():
    """
    Scan through all apps with a signals.py file and find signals with the signal_control decorator applied. For those
    found, attempt to add an entry for it in the SignalControl table.
    """
    # get all apps in the project

    # for each app, find the signals.py file(s)

    # find signals with the signal_control decorator

    # add entries to the SignalControl table

    pass







def makeRegistrar():
    registry = {}
    def registrar(func):
        registry[func.__name__] = func
        return func
    registrar.all = registry
    return registrar


reg = makeRegistrar()

@reg
def f1(a):
    return a+1


@reg
def f2(a,b):
    return a+b


reg = makeRegistrar()
reg.all












import inspect

def deco(func):
    return func

def deco2():
    def wrapper(func):
        pass
    return wrapper


class Test(object):
    @deco
    def method(self):
        pass

    @deco2()
    def method2(self):
        pass


def methodsWithDecorator(cls, decoratorName):
    sourcelines = inspect.getsourcelines(cls)[0]
    for i,line in enumerate(sourcelines):
        line = line.strip()
        if line.split('(')[0].strip() == '@'+decoratorName: # leaving a bit out
            nextLine = sourcelines[i+1]
            name = nextLine.split('def')[1].split('(')[0].strip()
            yield(name)





