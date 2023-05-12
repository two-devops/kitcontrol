from init import InitApp

class TestInit:

    """
    testing class
    """

    path = "/tmp/kitcontrol_test"
    filename = ".kitcontrol/config.yaml"

    def test_init(self):
        """testing init"""

        init = InitApp(self.path)
        result = init.init_app()
        config = init.CONFIG

        with open(self.path + '/' + self.filename, 'r', encoding="utf-8") as file:
            result = file.read()

        for folder in config["default_config"]:
            for directory in folder.values():
                assert directory in result
