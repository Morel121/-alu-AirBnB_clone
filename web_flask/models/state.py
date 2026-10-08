import models
from models.base_model import BaseModel, Base
from models.city import City
import os


class State(BaseModel, Base):
    """Representation of State"""
    __tablename__ = 'states'
    # ... existing class attributes like name ...

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Getter attribute that returns the list of City instances
            with state_id equal to the current State.id
            """
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
