def has_negatives(a):

	num_dict = {}

	result = []

	for num in a:

		if num in num_dict:

			num_dict[num] += 1

		else:
			num_dict[num] = 1

	for num in num_dict.keys():

		if num > 0:

			if -num in num_dict:

				result.append(num)

	return result


if __name__ == "__main__":
	print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
