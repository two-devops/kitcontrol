import src.kit as k

def test_kit_default(monkeypatch):
    monkeypatch.setattr(k, "BASEPATH", "tests/kits")

    kit = k.Kit("test")

    assert "Mike" in kit.contents()

def test_kit_pass_values(monkeypatch):
    monkeypatch.setattr(k, "BASEPATH", "tests/kits")

    kit = k.Kit("test", {"greeting": "Hello baby :)"})

    assert "baby" in kit.contents()