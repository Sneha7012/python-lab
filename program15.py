my_dict = {'banana': 3, 'apple': 1, 'cherry': 2, 'date': 4}
asorted_dict = dict(sorted(my_dict.items()))
print("Ascending order:", asorted_dict)

dsorted_dict = dict(sorted(my_dict.items(), reverse=True))
print("Descending order:", dsorted_dict)
