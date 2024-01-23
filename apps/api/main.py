from fastapi import FastAPI
import injector

from shared.domain.query.query_bus import QueryBus

app = FastAPI()

@app.get("/")
def read_root():
    container = injector.Injector()
    query = container.get(QueryBus)

    print(query)
    return {"message": "Hello, Worldsss"}

class Engine:
    def rev(self):
        return "Vroom!"


@injector.inject
class Car:
    def __init__(self, engine: Engine):
        self.engine = engine

    def start(self):
        return self.engine.rev()
