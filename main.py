import itertools

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]

for element in itertools.chain.from_iterable(nested_list):
    print(element)