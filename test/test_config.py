from ikcontrol.init import InitApp
from ikcontrol.system import FakeSystem
# from mockito import when

class TestConfig:

    """
        testing class
    """


    def test_init(self):
        """testing init
        """
        # when(run).init("ikctl").thenReturn("kits, targets, pipelines")
        init = InitApp("ikctl", FakeSystem())
        assert True == init.build()
