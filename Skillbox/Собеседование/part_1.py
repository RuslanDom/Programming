dict_ = {
	1: 3,
	2: 2,
	3: 1
}
print(max(dict_))  #
print(max(dict_, key=lambda key: dict_[key]))