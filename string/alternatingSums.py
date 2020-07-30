import re

def enclosed(instr):
    capture = re.search("^.*(\(\w+\)).*$", instr)
    #print(capture)
    if capture:
        return capture.group(1)
    else:
        return None


def reverseInParentheses(inputString):
    a = inputString
    while enclosed(a):
        # fmt: off
        import ipdb,os; ipdb.set_trace(context=5)  # noqa
        # fmt: on
        print(enclosed(a))
        print(a)
        print(a[::-1][1:-1])
        a = a.replace(enclosed(a), a[::-1][1:-1])
    return a


i1 = "(baz)"
i2 = "foo(bar(baz))blim"
i3 = "foo(baz)blim"

print(list(map(reverseInParentheses, [i1, i2, i3])))
