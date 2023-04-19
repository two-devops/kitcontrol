from src.kit import Kit

def test_kit():
    kit = Kit("forwarder", {"collector": {"port": 2222}})

    assert "port 2222" in kit.contents()
