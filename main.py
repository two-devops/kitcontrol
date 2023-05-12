# from src.kit import Kit
# from src.target import Target
# from io import StringIO
from src.pipeline import Pipeline

# kit = Kit("forwarder", {"collector": {"port": 55000}})
# target = Target("docker")

# print(kit.contents())
# print(target.osinfo)

# string = "Esta cadena seria el contenido de un template"
# file = StringIO(string)
# target.upload(file, "demo.txt")

pipeline = Pipeline(kit="helloworld", target="docker", values={"worldof": "Bigman"})

print(pipeline.run())