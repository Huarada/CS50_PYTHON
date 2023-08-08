from fuel import convert,gauge


def test_convert1():
    assert convert("3/4") == 75

def test_convert2():
    assert convert("1/2") == 50

def test_convert3():
    assert convert("4/7") == 57

def test_convert4():
    assert convert("3/10") == 30


def test_gauge1():
    assert gauge(99) == "F"


def test_gauge2():
    assert gauge(100) == "F"



def test_gauge3():
    assert gauge(1) == "E"
    assert gauge(0) == "E"


def test_gauge4():
    assert gauge(95) == "95%"
    assert gauge(50) == "50%"

#testing ErrorValue





#testing Divisionbyzero