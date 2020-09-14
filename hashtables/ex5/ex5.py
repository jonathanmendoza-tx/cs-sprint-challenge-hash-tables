
def finder(files, queries):

	file_dict = {}

	result = []

	length = len(files)

	for i in range(length):

		file_dict[files[i]] = i

	for query in queries:

		result += [key for key, val in file_dict.items() if query in key]

	return result


if __name__ == "__main__":
	files = [
		'/bin/foo',
		'/bin/bar',
		'/usr/bin/baz'
	]
	queries = [
		"foo",
		"qux",
		"baz"
	]
	print(finder(files, queries))
