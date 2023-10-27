from Pensieve.CompletionRequest import CompletionRequest
from Pensieve.CompletionResponse import CompletionResponse


class AbstractModel:

    def complete(self, request: CompletionRequest) -> CompletionResponse:
        pass

    def complete_all(self, requests: list[CompletionRequest]) -> list[CompletionResponse]:
        pass
