from subprocess import run


class System:

    def mkdir(self, path):
        print(path)
        return run(["mkdir", "-p", path], capture_output=True, text=True, check=True, timeout=30)


class FakeSystem:
    def mkdir(self, path):
        print(path)
        return False