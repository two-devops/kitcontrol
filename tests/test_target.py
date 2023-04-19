from src.target import Target
from mockito import when

def test_target():
    target = Target("master")
    # when(target).get_connection().thenReturn(True)
    when(target).execute("hostnamectl").thenReturn("Is a macbook xD")

    assert "macbook" in target.execute("hostnamectl")
