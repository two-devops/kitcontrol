# from src.kit import Kit
from src.target import Target
from io import StringIO

# kit = Kit("forwarder", {"collector": {"port": 55000}})
target = Target("docker")

# print(kit.contents())
# print(target.osinfo)

string = "POC string as file :D"
file = StringIO(string)

target.upload(file, "testfile.txt")

print(target.execute("ls -lah"))
print(target.execute("cat testfile.txt"))
