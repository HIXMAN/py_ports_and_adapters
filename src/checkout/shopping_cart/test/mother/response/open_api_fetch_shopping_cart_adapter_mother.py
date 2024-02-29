from typing import List


class OpenApiFetchShoppingCartAdapterMother:
    @staticmethod
    def create(
        id: int = 1,
        status: str = "CREATED",
        lines: List = [
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
            "data": {
                "id": id,
                "status": status,
                "lines": [item["id"] for item in lines]
            },
            "relationships": {
                "lines": lines
            }
        }