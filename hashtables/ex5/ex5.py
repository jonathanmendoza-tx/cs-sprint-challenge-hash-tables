
def finder(files, queries):

	file_dict = {}

	result = []

	length = len(files)

	for i in range(length):

		parsed_file_path = files[i].split('/')

		file_name = parsed_file_path[len(parsed_file_path)-1]

		if file_name in file_dict:

			file_dict[file_name].add(i)

		else:

			file_dict[file_name] = set()
			file_dict[file_name].add(i)

	for query in queries:

		try:
			num_files = len(file_dict[query])

			while num_files > 0:

				result += [files[file_dict[query].pop()]]

				num_files -= 1

		except:
			pass

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
