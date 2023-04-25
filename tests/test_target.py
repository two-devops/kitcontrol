from src.target import Target
from mockito import when

def test_target():
    # when(Target).get_connection().thenReturn(True)
    target = Target("master")
    when(target).execute("hostnamectl").thenReturn("Is a macbook xD")

    assert "macbook" in target.execute("hostnamectl")

def test_connection_ok():
    pass

def test_connection_fails():
    pass

def test_autodetection_info():
    pass

def test_execution():
    pass
