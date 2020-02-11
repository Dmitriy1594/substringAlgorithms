from functools import wraps
from time import time


timedict = {}

def speed_test(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		start_time = time()
		result = fn(*args, **kwargs)
		end_time = time()
		global timedict
		timedict[fn.__name__] = end_time - start_time
		return result
	return wrapper

def get_time_dict():
	return timedict


