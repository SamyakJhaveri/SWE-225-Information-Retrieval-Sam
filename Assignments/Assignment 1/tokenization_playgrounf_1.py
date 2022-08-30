# 1
# https://stackoverflow.com/questions/4697006/python-split-string-by-list-of-separators
def split(txt, seps):
    default_sep = seps[0]

    # we skip seps[0] because that's the default separator
    for sep in seps[1:]:
        txt = txt.replace(sep, default_sep)
    return [i.strip() for i in txt.split(default_sep)]
    How to use it:

>>> split('ABC ; DEF123,GHI_JKL ; MN OP', (',', ';'))
['ABC', 'DEF123', 'GHI_JKL', 'MN OP']
Performance test:

import timeit
import re


TEST = 'ABC ; DEF123,GHI_JKL ; MN OP'
SEPS = (',', ';')


rsplit = re.compile("|".join(SEPS)).split
print(timeit.timeit(lambda: [s.strip() for s in rsplit(TEST)]))
# 1.6242462980007986

print(timeit.timeit(lambda: split(TEST, SEPS)))
# 1.3588597209964064
And with a much longer input string:

TEST = 100 * 'ABC ; DEF123,GHI_JKL ; MN OP , '

print(timeit.timeit(lambda: [s.strip() for s in rsplit(TEST)]))
# 130.67168392999884

print(timeit.timeit(lambda: split(TEST, SEPS)))
# 50.31940778599528




#2
# https://note.nkmk.me/en/python-split-rsplit-splitlines-re/

s_marks = 'one-two+three#four'

print(re.split('[-+#]', s_marks))
# ['one', 'two', 'three', 'four']