# from src.kit import Kit
from src.target import Target

# kit = Kit("forwarder", {"collector": {"port": 55000}})
target = Target("docker")

# print(kit.contents())
print(target.osinfo)
