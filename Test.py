from itertools import product


def unique_pattern_generation(depth):
	print("I am doing - " + str(depth))

	temp_result = [''.join(x) for x in (product(*['ACGT'] * depth))]
	return temp_result

if __name__ == '__main__':
	print(unique_pattern_generation(6))
