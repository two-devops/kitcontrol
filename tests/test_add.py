from add import AddResources

class TestAddResources:
    """testing class AddResource"""

    entities = ["kit", "target", "pipeline"]

    def test_entities(self):
        """testing entities function"""

        addresource = AddResources()

        for entity in self.entities:
            if entity == "kit":
                assert True is addresource.add_entity(entity, "test")
            if entity == "target":
                assert True is addresource.add_entity(entity, "test")
            if entity == "pipeline":
                assert True is addresource.add_entity(entity, "test")
