def get_indices_of_item_weights(weights, length, limit):

	weights_dict = {}

	answer = ()

	for i in range(length):

		if weights[i] in weights_dict:

			weights_dict[weights[i]].add(i)

		else:

			weights_dict[weights[i]] = set()
			weights_dict[weights[i]].add(i)

	for num in weights_dict.items():

		index = num[1].pop()

		remainder = limit - num[0]

		if remainder in weights_dict:

			print(weights_dict[remainder])

			answer = (index, weights_dict[remainder].pop())

			return sorted(answer, reverse = True)

		else:

			num[1].add(index)

	return None

	

	
