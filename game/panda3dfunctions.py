class panda3dFunc:
    @staticmethod
    def load_model(model: str, showbase):
        return showbase.loader.load_model(f"models/{model}")

load = panda3dFunc()
