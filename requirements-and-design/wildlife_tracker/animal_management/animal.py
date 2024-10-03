from typing import Any, Optional

class Animal:

    def __init__(self, animal_id: int, age: Optional[int], species: str, health_status: Optional[str]) -> None:

        self.animal_id = animal_id
        self.age = age or None
        self.species = species
        self.health_status = health_status or None
    
    def get_animal_details(self, animal_id: int) -> dict[str, Any]:
        pass

    def update_animal_details(self, animal_id: int, **kwargs: Any) -> None:
        pass
