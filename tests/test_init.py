from cmds.init import Init
from cmds.config import Config

class TestInit:

    """
    testing class
    """

    path = "/tmp/kitcontrol_test"
    filename = ".kitcontrol/config.yaml"

    def test_init(self):
        """testing init"""

        init = Init(self.path)
        result = init.init_app()
        config = Config()

        with open(self.path + '/' + self.filename, 'r', encoding="utf-8") as file:
            result = file.read()

        for folder in config.KIT_CONTROL_CONFIG["default_config"]:
            for directory in folder.values():
                assert directory in result
