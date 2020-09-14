#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
	def __init__(self, source, destination):
		self.source = source
		self.destination = destination


def reconstruct_trip(tickets, length):

	trip_dict = {}

	for ticket in tickets:

		trip_dict[ticket.source] = ticket.destination

	route = []

	route.append(trip_dict.pop('NONE'))

	length -= 1
	index = 0

	while length > 0:

		route.append(trip_dict.pop(route[index]))

		length -= 1
		index += 1

	return route
