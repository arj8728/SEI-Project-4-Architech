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
    metal_frame = Construction(name='Metal frame')
    aluminium_clad = Construction(name='Aluminium')
    modern_panel_cladding = Construction(name='Modern panel cladding')
    rendered_masonry = Construction(name='Rendered masonry')
    brick_block = Construction(name='Brick/block')
    pre_cast = Construction(name='Pre-cast structural concrete')
    concrete = Construction(name='Concrete')
    mmc = Construction(name='Modern Methods of Construction')
    portland_stone = Construction(name='Portland stone')
    timber_cladding = Construction(name='Timber cladding')
    brick_portland_stone_faced = Construction(name='Brick faced with Portland Stone')
    reinforced_concrete = Construction(name='Reinforced concrete')


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
    art_nouveau = Style(name='Art Nouveau')
    classical = Style(name='Classical')


    Building(
    name='The Lloyd\'s Building',
    architect='Sir Richard Rogers',
    style=radical_bowellism,
    # (refers to designs that see the services for the building located on the exterior to maximise the space inside)
    address='1 Lime Street, London',
    latitude=51.51301,
    longitude=-0.08228,
    postcode='EC3M 7HA',
    construction=rcf,
    built=1978,
    about='Lloyds of London is the world’s greatest insurance market. It had moved its dealing room twice in 50 years and wanted a building that would provide for its needs well into the 21st century. It was also imperative that Lloyd’s could continue their operations unhindered during the rebuilding operation, which almost inevitably involved the demolition of the existing 1928 building. The competition for a new building was won on the basis not of an architectural proposal but of a strategy for the future of this key City institution. Richard Rogers Partnership (RRP) proposed a building where the dealing room could expand or contract, according to the needs of the market, by means of a series of galleries around a central space. To maximise space, services are banished to the perimeter. As the architectural form of the building evolved, particular attention was paid to its impact on the surrounding area, especially on the listed 19th century Leadenhall Market. As a result, Lloyd’s became a complex grouping of towers, almost Gothic in feeling – an effect enhanced by the height of the external plant-room towers. Lloyd’s is one of the great architectural achievements of the 1980s, one of the buildings which confirmed the practice’s position in the front rank of international architects. It has emerged as one of the greatest modern British buildings, one which balances technical efficiency with architectural expressiveness to produce an effect which might be called highly romantic and judged a very positive addition to the London skyline. The building was Grade I listed in 2011, the youngest structure to obtain this status. English Heritage described it as “universally recognized as one of the key buildings of the modern epoch.',
    image=['https://upload.wikimedia.org/wikipedia/commons/3/34/Lloyd%27s_building_from_Leadenhall_Street.jpg', 'http://www.bbc.co.uk/staticarchive/e8eea2b72d54aa09dfb5cfb4bf882e7c78059ed7.jpg'],
    user=char
    )

    Building(
    name='The British Museum',
    architect='Sir Robert Smirke',
    style=greek_revival,
    # (refers to designs that see the services for the building located on the exterior to maximise the space inside)
    address='Great Russell Street, London',
    latitude=51.51936,
    longitude=-0.12687,
    postcode='WC1B 3DG',
    construction=portland_stone,
    built=1852,
    about='The core of today’s building was designed by the architect Sir Robert Smirke (1780–1867) in 1823. It was a quadrangle with four wings: the north, east, south and west wings. The building was completed in 1852. It included galleries for classical sculpture and Assyrian antiquities as well as residences for staff. Smirke designed the building in the Greek Revival style, which emulated classical Greek architecture. Greek features on the building include the columns and pediment at the South entrance. This style had become increasingly popular since the 1750s when Greece and its ancient sites were ‘rediscovered’ by western Europeans. The building was constructed using up-to-the-minute 1820s technology. Built on a concrete floor, the frame of the building was made from cast iron and filled in with London stock brick. The public facing sections of the building were covered in a layer of Portland stone. In 1853, the quadrangle building won the Royal Institute of British Architects’ Gold Medal.',
    image=['https://upload.wikimedia.org/wikipedia/commons/3/3a/British_Museum_from_NE_2.JPG'],
    user=arj
    )

    Building(
    name='Lee Valley VeloPark',
    architect='Hopkins Architects',
    style=modern,
    address='Queen Elizabeth Olympic Park, Abercrombie Road, London',
    latitude=51.55038,
    longitude=-0.01526,
    postcode='E20 3AB',
    construction=rcf,
    built=2011,
    about='On 12 July 2007, the Olympic Delivery Authority selected the design team: Hopkins Architects, Expedition Engineering, BDSP, and Grant Associates, following an architectural design competition managed by RIBA Competitions. The Velopark was scheduled to be completed by the contractor, ISG, in 2011. In 2004, during London\'s Olympic and Paralympic bid, the estimated cost was £37 million, including £20 million for the velodrome. </br> In 2009, at the time work began on the construction of the velodrome, the estimated cost of that facility alone was £105 million. Work on the velodrome was completed in February 2011, and was the first Olympic Park venue to be completed. The roof is designed to reflect the geometry of cycling as well as being lightweight and efficient reflecting a bike. There is also a 360-degree concourse level with windows allowing people views of the Olympic Park. The velodrome is energy efficient—rooflights reduce the need for artificial lights, and natural ventilation reduces the need for air condition. Rain water is also collected, which reduces the amount of water used from the municipal water system. Designer Ron Webb, who designed the velodrome tracks for the Sydney and Athens Games, was in charge of the design and installation of the track. The 250-metre track was made with 56 km (35 miles) of Siberian Pine and 350,000 nails.',
    image=['https://images.unsplash.com/photo-1524772653050-7c42f97c43ca?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1033&q=80'],
    user=char
    )

    Building(
    name='Shakespeare Tower',
    architect='Chamberlain, Powell and Bon',
    style=brutalist,
    address='The Barbican Estate, London',
    latitude=51.52028,
    longitude=-0.09492,
    postcode='EC2Y 8NJ',
    construction=pre_cast,
    built=1976,
    about='The Barbican Estate is a residential estate that was built during the 1960s and the 1980s within the City of London in Central London, in an area once devastated by World War II bombings and today densely populated by financial institutions. It contains, or is adjacent to, the Barbican Arts Centre, the Museum of London, the Guildhall School of Music and Drama, the Barbican public library, the City of London School for Girls and a YMCA (now closed), forming the Barbican Complex. The Barbican Complex is a prominent example of British brutalist architecture and is Grade II listed as a whole with the exception of the former Milton Court. Milton Court, which once contained a fire station, medical facilities, and some flats, was demolished to allow the construction of a new apartment tower named The Heron, which also contains additional facilities for the Guildhall School of Music and Drama. </br> The residential estate consists of three tower blocks, 13 terrace blocks, two mews and The Postern, Wallside and Milton Court. </br> The estate contains three of London\'s tallest residential towers, at 42 storeys and 123 metres (404 ft) high. The top two or three floors of each block comprise three penthouse flats.',
    image=['https://images.unsplash.com/photo-1548324215-f179404ae9ac?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60'],
    user=char
    )

    Building(
    name='Florin Court',
    image=['https://lid.zoocdn.com/645/430/8e656a8f1e9d07e4a0dfc93b36ef047577772e19.jpg'],
    architect='Guy Morgan and Partners',
    style=art_deco,
    address='6-9 Charterhouse Square',
    latitude=51.52097,
    longitude=-0.09854,
    postcode='EC1M 6ET',
    construction=steel_frame,
    built=1936,
    about='Ten storeys high, the apartment block is a steel-framed building with concrete floors. It has a recessed centre with wings on either side, and curved round the corners. The brickwork of the walls are in yellow brick and laid out via a method named Flemish bond, where one brick of shorter length is placed in between longer length pieces. There are also decorative pieces in brown brick such as the stylised cartouche (a frame around a design) and ribbons. On the façade of the building, you can see eleven windows on every floor which are lined both at the top and below with metal. Although the individual flats are relatively small in size, the apartment block has a rooftop terrace, a gym, a sauna and swimming pool that is free for all the residents to use.',
    user=char
    )

    Building(
    name='The Hoover Building',
    image=['https://media.architecturaldigest.com/photos/584f2b59001c874267ed3a73/master/w_1200%2Cc_limit/art-deco-london-07.jpg'],
    architect='Wallis, Gilbert and Partners',
    style=art_deco,
    address='Western Avenue, Perivale',
    latitude=51.53379,
    longitude=-0.31888,
    postcode='UB6 8DW',
    construction=reinforced_concrete,
    built=1933,
    about='Designed by architecture firm, Wallis, Gilbert and Partners who also designed a number of other Art Deco buildings in the 1920s and 30s, the Hoover Building was built as the British manufacturing plant for American Hoover Company\'s vacuum cleaners. Originally it was just the main office building that was opened in 1932, but later on the factory canteen and another five-story building was built on the site.The ferro-concrete construction method was used to build the factory which has two storeys with slighty taller towers on either side. The building is rendered in a white Portland cement, also known as Snowcrete, with Egyptian-inspired details in red, green, and blue tiles on the façade. The front is divided up into 15 recessed window bays with copper-green glazing bars and straight fluted columns in between; and at the very far sides of the factory there are two pillars with a spiral underneath which could be influenced by the curved tail of the Eye of the Horus. The main entrance is decorated with a geometric windows in the shape of a sunburst and sits above a concrete entablature of the copper-green door.',
    user=char
    )

    Building(
    name='SIS Building',
    image=['https://nineelmslondon.com/wp-content/uploads/2017/09/MI6-1024x600.jpg'],
    architect='Terry Farrell and Partners',
    style=modernist,
    address='85 Albert Embankment, London',
    latitude=51.48796,
    longitude=-0.12372,
    postcode='SE1 7TP',
    construction=rcf,
    built=1994,
    about='It\'s along one of the most filmed waterfronts in the world – the MI6 building on the Albert Embankment has a strident Thameside presence and is perhaps most recognisable from its several cameos in recent James Bond films. Officially, 85 Albert Embankment at Vauxhall Cross is named the SIS Building for Secret Intelligence Service and has been at this location since 1994. Before then, the SIS headquarters were at Century House by Waterloo station but weren\'t secure or well hidden.'
    'The current spot housed the historic Vauxhall Pleasure Gardens (1600s) then a glass factory, a vinegar works, a gin distillery, and finally, the SIS headquarters. Architect Terry Farrell was inspired by 1930s industrial modernist architecture (like that of Bankside and Battersea Power Station) as well as Aztec and Mayan temples. That\'s why the MI6 building looks like a jazz age ziggurat!',
    user=char
    )

    Building(
    name='Jewel Tower',
    image=['https://media.timeout.com/images/103503699/750/562/image.jpg'],
    architect='Henry Yevele',
    style=medieval,
    address='Abingdon St, Westminster, London',
    latitude=51.50000,
    longitude=-0.12700,
    postcode='SW1P 3JX',
    construction=stone,
    built=1366,
    about='The Jewel Tower is a three-story building of Kentish Ragstone with a brick parapet, structurally largely unchanged since the 14th century. The walls that once faced away from the palace are finely coursed, but the interior two walls are more crudely finished. The external windows are almost all 18th-century in origin and made from Portland limestone. The jagged remnants of the former palace walls jut out from the sides of the tower.[70] The moat, now dry, stretches away east from the tower, passing by the former landing stage for boats from the Thames, 6 metres (20 ft) long and made from ashlar stone. The clearances of the post-war era mean that there are now few neighbouring buildings to the tower, and it is much more visible than in previous centuries. The ground floor of the tower is entered from the north, and is made up of two chambers, a larger room 7.5 by 4 metres (25 by 13 ft), a smaller turret room in the south-east corner, 4 by 3 metres (13.1 by 9.8 ft). The windows in the main room are a mixture of early 18th-century designs, combined with a surviving large medieval window embrasure on the eastern side. The main chamber has elaborate stone vaulting, considered by historian Jeremy Ashbee to be "one of the most impressive medieval interiors in London... an architectural masterpiece". The vaulting features 16 carved Reigate stone bosses, including grotesque heads, birds, flowers and the devil, some designed to form amusing visual illusions. The ground floor is used by English Heritage as a gift shop and cafe. The first floor is reached by a 20th-century spiral staircase, and follows the same two-room design as the first floor. It has a roof of groin-vaulted Portland stone, probably from the 18th century, and the windows are mostly 18th century in origin, with one 20th century reconstruction. The iron door to the larger chamber carries the date of its installation, 1621, and its lock carries the letters "IR", standing for King James I. The neighbouring room is barrel-vaulted in brick, with a recess in the wall that was originally a latrine, and the original 1719 iron-shutters on its north window. The first floor contains an exhibit on the history of the UK Parliament.The spiral staircase to the second floor is original. The floor continues the two-room design, and the roof, largely a post-war replacement with only a few surviving medieval timbers, is intended to resemble the original medieval design. The fireplace and windows are original, as probably is the 14th-century wooden door to the floor. Both the wall between the two rooms, and its stone doorway, were built in the 18th century. The room contains a display on the history of the tower, and some of the original wooden foundations of the building.',
    user=char
    )

    Building(
    name='The Blackfriar Pub',
    image=['https://media.timeout.com/images/103503677/1024/768/image.jpg'],
    architect='H. Fuller-Clark',
    style=art_nouveau,
    address='174 Queen Victoria Street',
    latitude=51.51212,
    longitude=-0.10375,
    postcode='EC4V 4EG',
    construction=brick,
    built=1875,
    about='The Black Friar is a Grade II* listed public house on Queen Victoria Street in Blackfriars, London. It was built in about 1875 on the site of a former medieval Dominican friary, and then remodelled in about 1905 by the architect Herbert Fuller-Clark. Much of the internal decoration was done by the sculptors Frederick T. Callcott & Henry Poole. The building was nearly demolished during a phase of redevelopment in the 1960s, until it was saved by a campaign spearheaded by poet Sir John Betjeman. It is on the Campaign for Real Ale\'s National Inventory of Historic Pub Interiors.',
    user=char
    )

    Building(
    name='The Queen\'s House',
    image=['https://media.timeout.com/images/103503727/1024/768/image.jpg'],
    architect='Inigo Jones',
    style=classical,
    address='Park Row, Greenwich',
    latitude=51.48094,
    longitude=-0.00524,
    postcode='SE10 9NF',
    construction=brick_portland_stone_faced,
    built=1635,
    about='The Queen\'s House was one of the earliest if not the first building in Britain to be built in a purely classical style; it was also Inigo Jones\' first commission after returning from his travels around Italy. The building was initially for Queen Anne of Denmark, James I\'s wife, and was to act as both a summer house and a link house to the original Palace of Placentia (Greenwich Palace). However, only three years after construction began, Queen Anne died and work was halted for 10 years until 1929 when Charles I gave the house to his queen, Henrietta Maria, and the building was finally finished in 1635. Built of brick and faced with Portland stone, the Queen\'s House consists of two storeys with the north and south façades being 35m in length and the east and west façades being half a metre longer. The north façade, which is the most recognisable and faces the river, has three sections: a middle section which slightly protrudes out with three window bays and a terrace with curving steps, and two sections on either side each with two window bays. The south façade also has three sections, however, an Ionic loggia of five bays spans the middle section of the second storey. The east and west façades are connected to the additional wings of the house via long colonnades.',
    user=char
    )

    Building(
    name='New River Head',
    image=['https://assets.themodernhouse.com/wp-content/uploads/tmh/7940/26-11.jpg'],
    architect='unknown,',
    style=neo_classical,
    address='173 Roseberry Avenue, London',
    latitude=51.52740,
    longitude=-0.10691,
    postcode='EC1R 4TY',
    construction=brick,
    built=1635,
    about='New River Head was constructed in 1920 to a design by Herbert Austen Hall, as the headquarters of the Metropolitan Water Board. It was listed Grade II by English Heritage in 1950. Converted into flats in the 1990s this most impressive building retains a gigantic ballroom entrance foyer. It has a gym, a porter, cellars, a substantial communal garden.',
    user=char
    )

    Building(
    name='The Captain Kidd',
    image=['https://i.pinimg.com/originals/a0/3e/e6/a03ee625b4bf1038f14933c274b1984a.jpg'],
    architect='Herbert Austen Hall,',
    style=victorian,
    address='108 Wapping High Street,  London',
    latitude=51.50302,
    longitude=-0.06012,
    postcode='E1W 2NE',
    construction=brick,
    built=1850,
    about='Former Victorian warsehouse converted to a Samuel Smith\'s pub in 1990. The yard to its east (now a beer garden) was the site for the public execution of pirates, usually by hanging. On 23 May 1701, the Scottish sailor William Kidd was hanged for piracy on that very spot. An engraving of the grizzly event still exists and it is easy to establish that this was the spot because, in the distance, is Rotherhithe’s church. The site was known as Execution Dock. The name ‘Captain Kidd’ was an obvious choice for the hostelry.',
    user=char
        )
    db.commit()
