from pony.orm import db_session
from app import db
from models.Building import Building
from models.Construction import Construction
from models.Style import Style
from models.User import User, UserSchema


db.drop_all_tables(with_all_data=True)
db.create_tables()

with db_session():
    schema = UserSchema()
    char = User(
        username='char',
        email='ch@outlook.co.uk',
        password_hash=schema.generate_hash('pass')
    )

    schema = UserSchema()
    arj = User(
        username='arj',
        email='am@outlook.co.uk',
        password_hash=schema.generate_hash('pass')
    )

    brick = Construction(name='Brick')
    london_stock_brick = Construction(name='London Stock Brick')
    stone = Construction(name='Stone')
    timber_frame = Construction(name='Timber frame')
    rcf = Construction(name='Concrete frame')
    steel_frame = Construction(name='Steel frame')
    cast_iron_frame = Construction(name='Cast iron frame')
    aluminium_clad = Construction(name='Aluminium')
    modern_panel_cladding = Construction(name='Modern panel cladding')
    rendered_masonry = Construction(name='Rendered masonry')
    brick_block = Construction(name='Brick/block')
    pre_cast = Construction(name='Structural pre-cast concrete')
    granite_aggregate = Construction(name='pick-hammered, exposed granite aggregate')
    concrete = Construction(name='Concrete')
    mmc = Construction(name='Modern Methods of Construction')
    portland_stone = Construction(name='Portland stone')
    timber_cladding = Construction(name='Timber cladding')


    radical_bowellism = Style(name='Radical Bowellism')
    greek_revival = Style(name='Greek Revival')
    modern = Style(name='Modern')
    brutalist = Style(name='Brutalist')
    georgian = Style(name='Georgian')
    victorian = Style(name='Victorian')
    modernist = Style(name='Modernist')
    edwardian = Style(name='Edwardian')
    art_deco = Style(name='Art Deco')
    neo_classical = Style(name='Neo Classical')
    regency = Style(name='Regency')
    jaconbean = Style(name='jacobean')
    elizabethan = Style(name='Elizabethan')
    tudor = Style(name='Tudor')
    medieval = Style(name='Medieval')


    Building(
    name='The Lloyd\'s Building',
    architect='Sir Richard Rogers',
    style=radical_bowellism,
    # (refers to designs that see the services for the building located on the exterior to maximise the space inside)
    address='1 Lime Street, London',
    postcode='EC3M 7HA',
    constructions=[rcf, aluminium_clad],
    built=1978,
    image='https://upload.wikimedia.org/wikipedia/commons/3/34/Lloyd%27s_building_from_Leadenhall_Street.jpg',
    user=char
    )

    Building(
    name='The British Museum',
    architect='Sir Robert Smirke',
    style=greek_revival,
    # (refers to designs that see the services for the building located on the exterior to maximise the space inside)
    address='Great Russell Street, London',
    postcode='WC1B 3DG',
    constructions=[cast_iron_frame, london_stock_brick, portland_stone],
    built=1852,
    image='https://upload.wikimedia.org/wikipedia/commons/3/3a/British_Museum_from_NE_2.JPG',
    user=arj
    )

    Building(
    name='Lee Valley VeloPark',
    architect='Hopkins Architects',
    style=modern,
    address='Queen Elizabeth Olympic Park, Abercrombie Road, London',
    postcode='E20 3AB',
    constructions=[rcf, steel_frame, timber_cladding],
    built=2011,
    # about='On 12 July 2007, the Olympic Delivery Authority selected the design team: Hopkins Architects, Expedition Engineering, BDSP, and Grant Associates, following an architectural design competition managed by RIBA Competitions. The Velopark was scheduled to be completed by the contractor, ISG, in 2011. In 2004, during London\'s Olympic and Paralympic bid, the estimated cost was £37 million, including £20 million for the velodrome. </br> In 2009, at the time work began on the construction of the velodrome, the estimated cost of that facility alone was £105 million. Work on the velodrome was completed in February 2011, and was the first Olympic Park venue to be completed. The roof is designed to reflect the geometry of cycling as well as being lightweight and efficient reflecting a bike. There is also a 360-degree concourse level with windows allowing people views of the Olympic Park. The velodrome is energy efficient—rooflights reduce the need for artificial lights, and natural ventilation reduces the need for air condition. Rain water is also collected, which reduces the amount of water used from the municipal water system. Designer Ron Webb, who designed the velodrome tracks for the Sydney and Athens Games, was in charge of the design and installation of the track. The 250-metre track was made with 56 km (35 miles) of Siberian Pine and 350,000 nails.',
    image='https://images.unsplash.com/photo-1524772653050-7c42f97c43ca?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1033&q=80',
    user=char
    )

    Building(
    name='Shakespeare Tower',
    architect='Chamberlain, Powell and Bon',
    style=brutalist,
    address='The Barbican Estate, London',
    postcode='EC2Y 8NJ',
    constructions=[pre_cast, granite_aggregate],
    built=1976,
    # about='The Barbican Estate is a residential estate that was built during the 1960s and the 1980s within the City of London in Central London, in an area once devastated by World War II bombings and today densely populated by financial institutions. It contains, or is adjacent to, the Barbican Arts Centre, the Museum of London, the Guildhall School of Music and Drama, the Barbican public library, the City of London School for Girls and a YMCA (now closed), forming the Barbican Complex. The Barbican Complex is a prominent example of British brutalist architecture and is Grade II listed as a whole with the exception of the former Milton Court. Milton Court, which once contained a fire station, medical facilities, and some flats, was demolished to allow the construction of a new apartment tower named The Heron, which also contains additional facilities for the Guildhall School of Music and Drama. </br> The residential estate consists of three tower blocks, 13 terrace blocks, two mews and The Postern, Wallside and Milton Court. </br> The estate contains three of London\'s tallest residential towers, at 42 storeys and 123 metres (404 ft) high. The top two or three floors of each block comprise three penthouse flats.',
    image='https://images.unsplash.com/photo-1548324215-f179404ae9ac?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60',
    user=char
    )

    db.commit()
