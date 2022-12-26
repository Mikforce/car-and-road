from direct.showbase.ShowBase import ShowBase

showbase = ShowBase()

class panda3dFunc():
    @staticmethod
    def load_model(model: str):
        return showbase.loader.load_model(f"models/{model}")

load = panda3dFunc()

print(type(load.load_model("car.gltf")))