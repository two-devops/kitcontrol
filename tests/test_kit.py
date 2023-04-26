import src.kit as k
import pytest

@pytest.fixture
def mock_kits_dir(monkeypatch):
    monkeypatch.setattr(k, "BASEPATH", "tests/kits")

def test_kit_default(mock_kits_dir):

    kit = k.Kit("test")

    assert "Mike" in kit.contents()

def test_kit_pass_values(mock_kits_dir):

    kit = k.Kit("test", {"greeting": "Hello baby :)"})

    assert "baby" in kit.contents()