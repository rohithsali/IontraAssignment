import minInArray

def test_min_num():
    assert minInArray.min_num([200, 4, 5]) == 4
    assert minInArray.min_num([0, 0, 0, 0]) == 0
    assert minInArray.min_num([-2, 6, -5, -100]) == -100
    assert minInArray.min_num([100, 100, 100, 100, 100, 100]) == 100
    assert minInArray.min_num([-100]) == -100
    assert minInArray.min_num([100, 5, 4, 200, 4]) == 4

def test_second_min_num():
    assert minInArray.second_min_num([0, 0, 0, 0, 0]) == 0
    assert minInArray.second_min_num([8, 9, 4, 3, 2]) == 3
    assert minInArray.second_min_num([-4, 5, 10, 100, -100]) == -4
    assert minInArray.second_min_num([2, 4]) == 4
    assert minInArray.second_min_num([-5, -10]) == -5
    assert minInArray.second_min_num([-100]) == None
    assert minInArray.second_min_num([4, 6, 5, 4, 6, 5]) == 5

def test_nth_min_num():
    assert minInArray.nth_min_num([0, 0, 0, 0], 2) == 0
    assert minInArray.nth_min_num([8, 9, 4, 3, 2], 4) == 8
    assert minInArray.nth_min_num([-4, 5, 10, 100, -100], 1) == -100
    assert minInArray.nth_min_num([2, 4], 1) == 2
    assert minInArray.nth_min_num([-5, -10], 2) == -5
    assert minInArray.nth_min_num([4, 6, 5, 4, 6, 5], 3) == 6
    assert minInArray.nth_min_num([-4, 5, 10, 100, -100], 0) == "n should be greater than 0"
    assert minInArray.nth_min_num([-4, 5, 10, 100, -100], 8) == "n is smaller than length of array or n =0"
    assert minInArray.nth_min_num([-4, 5, 10, 100, -100], -3) == "n should be greater than 0"