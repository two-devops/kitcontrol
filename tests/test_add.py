from add import AddResources

class TestAddResources:

    """
    testing class AddResource
    """
    entities = ["kit", "target", "pipeline"]

    def test_add_kit(self):
        """
        testing add_kit function
        """
        addresource = AddResources()

        for entity in self.entities:
            if entity == "kit":
                assert True is addresource.add_entity(entity, "test")

    def test_add_target(self):
        """
        testing add_target function
        """
        pass

    def test_add_pipeline(self):
        """
        testing add_pipeline function
        """
        pass
