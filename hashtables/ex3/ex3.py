def intersection(arrays):

	length = len(arrays)

	num_dict = {}

	result = []

	for num_list in arrays:

		for num in num_list:

			if num in num_dict:

				num_dict[num] += 1

			else:

				num_dict[num] = 1

	for nums in num_dict.items():

		if nums[1] == length:

			result.append(nums[0])

	return result


if __name__ == "__main__":
	arrays = []

	arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
	arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
	arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

	print(intersection(arrays))
