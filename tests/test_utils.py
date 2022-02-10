from imeastools.utils import *

def test_get_intersection():
	assert get_difference(get_difference([1,2,3],[2]),[1,3]) == []