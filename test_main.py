from main import add

def test_add():
    assert add(2,3) == 5
    assert add(1,3) == 4
    assert add(-5,10) == 5