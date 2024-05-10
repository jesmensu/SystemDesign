import os
# Without dependence injection
class ApiClient:
    def __init__(self) -> None:
        self.api_key = os.getenv("API_KEY")  # <-- dependency
        self.timeout = int(os.getenv("TIMEOUT"))  # <-- dependency

class Service:
    def __init__(self) -> None:
        self.api_client = ApiClient()  # <-- dependency

def main() -> None:
    service = Service()  # <-- dependency

if __name__ == "__main__":
    main()



# With dependency inversion

class ApiClient:
    def __init__(self, api_key,timeout) -> None:
        self.api_key = api_key      # <-- dependency is injected
        self.timeout = timeout      # <-- dependency is injected

class Service:

    def __init__(self, api_client:ApiClient) -> None:
        self.api_client = api_client      # <-- dependency is injected


def main(service) -> None:
    service = service                   # <-- dependency is injected


if __name__ == "__main__":
    main(service = Service(api_client=ApiClient(api_key = os.getenv("API_KEY"), timeout= int(os.getenv("TIMEOUT")))))