from Pensieve.AbstractModel import AbstractModel


class AbstractModelProvider:

    def build_model(self, model: str) -> AbstractModel:
        pass
