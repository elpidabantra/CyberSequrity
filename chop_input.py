from itertools import chain, islice

def chunks(iterable, n):
   iterable = iter(iterable)
   while True:
       yield chain([next(iterable)], islice(iterable, n-1))

l = 40000
file_large = 'input.txt'
with open(file_large) as bigfile:
    for i, lines in enumerate(chunks(bigfile, l)):
        file_split = '{}.{}'.format(i, file_large)
        with open(file_split, 'w') as f:
            f.writelines(lines)