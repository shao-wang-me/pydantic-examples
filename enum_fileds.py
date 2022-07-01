from enum import Enum

from pydantic import BaseModel


class Make(Enum):
    AUDI = 'Audi'
    TOYOTA = 'Toyota'


class Tag(Enum):
    SEDAN = 'Sedan'
    HATCH = 'Hatch'
    HYBRID = 'Hybrid'
    PREMIUM = 'Premium'


class Car(BaseModel):
    name: str
    make: Make
    tags: set[Tag] = []


corolla = Car(name='Corolla', make=Make.TOYOTA, tags={Tag.HATCH, Tag.HYBRID})
a4 = Car(name='A4', make=Make.AUDI, tags={Tag.SEDAN, Tag.PREMIUM})

print(corolla.json())
print(a4.json())

# {"name": "Corolla", "make": "Toyota", "tags": ["Hatch", "Hybrid"]}
# {"name": "A4", "make": "Audi", "tags": ["Sedan", "Premium"]}
