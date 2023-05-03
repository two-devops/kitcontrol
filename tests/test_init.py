from init import InitApp

class TestInit:

    """
    testing class
    """

    path = "/tmp"

    def test_init(self):
        """
        testing init
        """
        init = InitApp(self.path + "/kitctl")
        assert True is init.build_folders()

    def test_config_file(self):
        """testing config files
        """
        init = InitApp(self.path + "/kitctl")
        result = init.create_config_files("test.yaml")
        config = init.CONFIG

        for folder in config["default_config"]:
            for directory in folder.values():
                assert directory in result
