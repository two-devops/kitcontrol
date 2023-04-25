from ikcontrol.init import InitApp

class TestConfig:

    """
        testing class
    """

    path = "/tmp"

    def test_init(self):
        """testing init
        """
        # when(run).init("ikctl").thenReturn("kits, targets, pipelines")
        init = InitApp(self.path + "/kitctl")
        assert True is init.build_folders()

    def test_config_file(self):
        """testing config files
        """
        init = InitApp(self.path + "/kitctl")
        result = init.create_config_files()
        config = init.config

        for folder in config["default_config"]:
            for directory in folder.values():
                assert directory in result
