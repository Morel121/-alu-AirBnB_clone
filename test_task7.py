#!/usr/bin/python3
from models import storage
from models.state import State
from models.city import City

state_1 = State(name="California")
state_1.save()
city_1 = City(state_id=state_1.id, name="Napa")
city_1.save()

for state in storage.all(State).values():
    for city in state.cities:
        print("Found city {} in state {}".format(city.name, state.name))
