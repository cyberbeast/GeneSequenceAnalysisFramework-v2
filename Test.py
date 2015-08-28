from itertools import product


def unique_pattern_generation(depth):
	print("I am doing - " + str(depth))

	if depth == 1:
		val = depth
	else:
		val = 2 * depth

	temp_result = [''.join(x) for x in (product(*['ACGT'] * val))]
	return temp_result


def main():
	print(str(unique_pattern_generation(5)))

if __name__ == '__main__':
	main()