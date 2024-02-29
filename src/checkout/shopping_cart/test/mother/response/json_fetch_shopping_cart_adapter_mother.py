from typing import Dict


class JsonFetchShoppingCartAdapterMother:
    @staticmethod
    def create(
        id: int = 1,
        status: str = "CREATED",
        lines: Dict = [
            {
                "id": 1,
                "quantity": 10
            },
            {
                "id": 2,
                "quantity": 20
            }
        ]
    ) -> dict:
        return {
            "id": id,
            "status": status,
            "lines": lines
        }