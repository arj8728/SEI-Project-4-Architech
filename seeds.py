from pony.orm import db_session
from app import db
from models.Building import Building

db.drop_all_tables(with_all_data=True)
db.create_tables()

with db_session():
    Building(
    name='The Lloyd\'s Building',
    architect='Sir Richard Rogers',
    style='Radical Bowellism',
    # (refers to designs that see the services for the building located on the exterior to maximise the space inside)
    address='1 Lime Street, London',
    post_code='EC3M 7HA',
    construction='reinforced concrete frame, alumunium cladding',
    built=1978
    )

    Building(
    name='The British Museum',
    architect='Sir Robert Smirke',
    style='Greek Revival',
    # (refers to designs that see the services for the building located on the exterior to maximise the space inside)
    address='Great Russell Street, London',
    post_code='WC1B 3DG',
    construction='cast iron frame, london-stockbrick, part clad in Portland stone',
    built=1852
    )

    db.commit()
