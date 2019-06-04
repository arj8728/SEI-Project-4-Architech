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
    early_georgian = Style(name='Early Georgian')
    gothic = Style(name='Gothic')
    neo_futurism = Style(name='Neo Futurism')


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
    images=['https://tokyofox.files.wordpress.com/2015/01/dscn0270.jpg', 'http://spinlister-blog.s3.amazonaws.com/2016/04/Modern-Architecture-London-2.jpg', 'http://www.bbc.co.uk/staticarchive/e8eea2b72d54aa09dfb5cfb4bf882e7c78059ed7.jpg', 'https://i.pinimg.com/564x/30/fa/87/30fa87305c142afbe0b9e5fe372cc672.jpg'],
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
    images=['https://i.pinimg.com/564x/d8/2c/31/d82c318409474007daf4b76b012628ba.jpg', 'https://upload.wikimedia.org/wikipedia/commons/3/3a/British_Museum_from_NE_2.JPG', 'https://c1.staticflickr.com/1/96/214966284_120633c9ef_z.jpg?zz=1', 'https://i.pinimg.com/564x/fd/ce/bb/fdcebb9f00b6cbc32bcbe64d552f06f8.jpg'],
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
    images=['https://images.unsplash.com/photo-1524772653050-7c42f97c43ca?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1033&q=80', 'https://cdn.londonandpartners.com/asset/lee-valley-velopark-velopark-777863150d38447a491533c459931086.jpg', 'https://q7a5d3d2.stackpathcdn.com/wp-content/uploads/2014/05/lee-valley-velopark-2.jpg', 'https://i.pinimg.com/564x/3a/1a/ed/3a1aedc48258f7b9f1c84351b3977fef.jpg', 'https://i.pinimg.com/564x/df/28/84/df2884fec89315b6d6274be933fb215d.jpg'],
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
    images=['http://pic.triposo.com/ios/cas/medium/75e1/75e13334b27d3e39a4d5c48113d956fc1978b50e51437f401939113fd2397f1a', 'http://www.barbicanliving.co.uk/wp-content/uploads/2015/09/P1000520.jpg', 'https://i.pinimg.com/564x/95/e8/5a/95e85ae23cdbb98b896eb6f4105ad3ea.jpg', 'https://i.pinimg.com/564x/bb/6d/e7/bb6de76fe448de5e884b77aa5ecd7470.jpg'],
    user=char
    )

    Building(
    name='Florin Court',
    images=['https://lid.zoocdn.com/645/430/8e656a8f1e9d07e4a0dfc93b36ef047577772e19.jpg', 'https://i.pinimg.com/564x/87/0a/b5/870ab56511f17b7608786c3ca6906fbf.jpg', 'https://i.pinimg.com/564x/d1/fe/87/d1fe872bc542fe0b13df11204cab7458.jpg', 'https://i.pinimg.com/564x/d8/96/04/d89604b5b37504cc8161ad0373af0c42.jpg'],
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
    images=['https://upload.wikimedia.org/wikipedia/commons/9/91/The_Hoover_Building%2C_Perivale%2C_London_-_geograph.org.uk_-_1208842.jpg', 'https://i.pinimg.com/originals/d7/0e/fe/d70efe4756a292980e61b6364d1bd622.jpg', 'https://www.hughesandsalvidge.co.uk/wp-content/uploads/2014/02/hoover-.png', 'https://i.pinimg.com/564x/48/4c/4b/484c4bcceaf2f268da52e5d5fd7d767d.jpg'],
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
    images=['https://i.pinimg.com/564x/4f/86/69/4f86692102a32849dcf502d6fe7d47aa.jpg', 'https://nineelmslondon.com/wp-content/uploads/2017/09/MI6-1024x600.jpg', 'https://i.pinimg.com/564x/68/ea/f2/68eaf26f198174a0da8053c185db1e31.jpg', 'https://i.pinimg.com/564x/f1/38/fc/f138fc42648404f689d23338776e0203.jpg', 'https://i.pinimg.com/564x/39/43/ba/3943ba3a355c1eb728d8b97cda1da8f8.jpg', 'https://i.pinimg.com/564x/28/83/f0/2883f08cb5241a9d9eed7540c5dd32b9.jpg'],
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
    images=['http://vipauk.org/enter/muse/lond/img/j01a.jpg', 'https://media.timeout.com/images/103503699/750/562/image.jpg', 'https://www.english-heritage.org.uk/siteassets/home/visit/places-to-visit/jewel-tower/history/view-from-the-west.jpg', 'https://www.britainexpress.com/images/attractions/editor3/Jewel-Tower-2806.jpg', 'https://www.britainexpress.com/images/attractions/editor3/Jewel-Tower-2812.jpg'],
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
    images=['https://i.pinimg.com/564x/10/66/8a/10668ad456473a08c7db7c034feb2027.jpg', 'https://i.pinimg.com/564x/ed/88/95/ed8895814b0c94bcc3e63b2fbdb968e1.jpg', 'https://i.pinimg.com/564x/bb/0a/83/bb0a83474bc3acb7b7ae4de227492132.jpg', 'https://i.pinimg.com/564x/e7/ff/68/e7ff6816eb6198cd1d01d1deff0fc3e0.jpg', 'https://media.timeout.com/images/103503677/1024/768/image.jpg'],
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
    images=['https://static1.squarespace.com/static/56b865ce7c65e435b9beb85d/56d57bec8259b57a20251c89/56d57c0422482e42c20fedd8/1457346772789/SLATECH_0013_Layer+6.jpg', 'https://i.pinimg.com/564x/08/38/0d/08380d958b7911f1ac60e867f4b1f935.jpg', 'https://i.pinimg.com/564x/e7/c6/b0/e7c6b0445548dc0a521b74913513e324.jpg', 'https://i.pinimg.com/564x/3c/4e/1d/3c4e1d6cc7fa570fd15783bc0d136098.jpg', 'https://i.pinimg.com/564x/9e/15/ea/9e15eaa9770666dc9993a081b36b9080.jpg', 'https://media.timeout.com/images/103503727/1024/768/image.jpg'],
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
    images=['https://imganuncios.mitula.net/3_bedroom_maisonette_for_sale_in_new_river_head_173_rosebery_avenue_ec1r_london_9020083539963362096.jpg', 'https://i.pinimg.com/564x/b7/35/51/b735519e06819ea84e3086272fb0ff59.jpg', 'https://imganuncios.mitula.net/2_bedroom_flat_for_sale_in_rosebery_avenue_clerkenwell_ec1r_london_5800084552061298041.jpg', 'https://ga-students.slack.com/archives/DEWD9HVQT/p1559598258018100', 'https://assets.themodernhouse.com/wp-content/uploads/tmh/7940/26-11.jpg'],
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
    images=['https://i.pinimg.com/564x/a0/3e/e6/a03ee625b4bf1038f14933c274b1984a.jpg', 'https://i.pinimg.com/564x/38/6d/ed/386dedf9c888a54215c3bc6195ed6e3f.jpg', 'https://s0.geograph.org.uk/geophotos/01/69/63/1696368_0f5a8715.jpg', 'https://i.pinimg.com/564x/b8/85/75/b88575c371b8893fc94d794c20dea9f2.jpg', 'https://i.pinimg.com/originals/a0/3e/e6/a03ee625b4bf1038f14933c274b1984a.jpg'],
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
    Building(
    name='The Geffyre Museum',
    images=['https://media.timeout.com/images/101632879/630/472/image.jpg', 'https://letsgowiththechildren.co.uk/wp-content/uploads/2016/12/The-Geffrye-Museum-of-the-Home-915px.jpg', 'https://www.geffrye-museum.org.uk/thumbnailgenerator.ashx?id=3970&width=932&height=2000&method=Limit&background=0&corners=0&cornerradius=0&type=Png&quality=80&h=E66A481EB4BB8B9563AF5FD42F3F9FA0&units=Pixel', 'https://www.geffrye-museum.org.uk/thumbnailgenerator.ashx?id=36805&width=932&height=2000&method=Limit&background=0&corners=0&cornerradius=0&type=Png&quality=80&h=75A3D579111C16E1A54F6FCC78FFE7&units=Pixel', 'https://images.squaremeal.co.uk/cloud/restaurants/10868/geffrye-museum-cafe-jan-2016-2.jpg?w=900&h=600&fit=crop'],
    architect='Unknown',
    style=early_georgian,
    address='136 Kingsland Rd, London',
    latitude=51.53155,
    longitude=-0.07627,
    postcode='E2 8EA',
    construction=brick,
    built=1714,
    about='The Geffrye Museum opened in 1914. The London County Council had been persuaded by leading members of the Arts and Crafts movement to convert the 18th century buildings into a museum related to the local furniture industry. Its purpose was to provide a reference collection of furniture of a \'fine standard of technical and artistic excellence\' to educate and inspire the local workforce. Its initial collections of furniture and panelled rooms have been added to over the years and now are complemented by decorative art, paintings, personalia and archives relating to English domestic interiors. Since becoming an independent charitable trust in 1991, we have embarked on an ambitious programme of developments, including refurbishing all of the period rooms and building a major new extension, which opened in November 1998',
    user=char
    )

    Building(
    name='The London Buddhist Centre',
    images=['https://i.pinimg.com/564x/bc/4c/2c/bc4c2cc2255ce5648736684449ace36d.jpg', 'https://s0.geograph.org.uk/geophotos/05/00/01/5000148_5749412d.jpg', 'https://thebuddhistcentre.com/sites/default/files/styles/large/public/groups/images/LBC_0.jpg?itok=UdhIglND', 'https://i.pinimg.com/564x/fa/99/e5/fa99e5996a714287d2757cf07ef85c11.jpg', 'https://pch-a.com/wp-content/uploads/2-London-Buddhist-Centre71.jpg'],
    architect='unknown',
    style=victorian,
    address='51 Roman Rd, Bethnal Green, London',
    latitude=51.52789,
    longitude=-0.05207,
    postcode='E2 0HU',
    construction=brick,
    built=1888,
    about='The Grade II listed former fire station has been subject to complete refurbishment in recent years. This is the culmination of over a £1 million extension and refurbishment of their site. The challenge of this listed building was met in 8 phases of work in an occupied building. The work consisted of the conversion of the upper floors to house the 10 fold community of residents, a new reception area and a third shrine room with associated support spaces.',
    user=char
    )

    Building(
    name='St Pancras',
    images=['https://www.cbreresidential.com/uk/sites/uk-residential/files/styles/image_style_mobile/public/Students%20-%20King%27s%20Cross%20HERO.jpg', 'https://www.jcms-journal.com/articles/10.5334/jcms.1021205/figures/Fig01_web.jpg', 'https://i0.wp.com/b-c-ing-u.com/wp/wp-content/uploads/2014/01/stpancras08.jpg?fit=640%2C480&w=640', 'https://memoirsofametrogirl.files.wordpress.com/2018/06/st-pancras-emin.jpg?w=640', 'http://gallery.nen.gov.uk/assets/1304/0000/0045/img_1351_mid.jpg'],
    architect='George Gilbert Scott,',
    style=gothic,
    address='Euston Rd, Kings Cross, London',
    latitude=51.52789,
    longitude=-0.05207,
    postcode='N1C 4QP',
    construction=brick,
    built=1868,
    about='St Pancras Station was opened in 1868 and is one of the wonders of Victorian engineering. Along with the former Midland Grand Hotel, it is a masterpiece of Victorian Gothic Architecture and one of the most elegant stations in the World. It has recently been refurbished to accommodate international train services; its history is a remarkable tale of decay, restoration and spectacular rebirth. In these history pages you can find out why the Victorians chose this design for the station and how they built it. You can also learn about how the station was restored and transformed to become the new arrival point for Eurostar services, and how the surrounding area has become one of London’s newest destinations. The train station design is a unique response to its geographic context but also reflects thinking of the day in respect of station design and operation; the platform deck was raised up on a grid of 688 cast-iron columns in order to allow steam engines to pass over the Regent’s canal just to the north. The space underneath, now called the Arcade, was designed and used to store beer produced by Burton Brewers, notably Bass and Thomas Salt.',
    user=char
        )

    Building(
    name='London City Hall',
    images=['https://i.pinimg.com/564x/f2/60/79/f26079dc7c212b5a8fbac82c4cefc545.jpg', 'https://i.pinimg.com/564x/df/41/0a/df410a1e73c3f4ffb4bc850fbe323afd.jpg', 'https://i.pinimg.com/564x/57/6e/38/576e38a3ebe9585305e4cb18ffffd590.jpg'],
    architect='George Gilbert Scott,',
    style=neo_futurism,
    address='Euston Rd, Kings Cross, London',
    latitude=51.50485,
    longitude=-0.07869,
    postcode='SE1 2AA',
    construction=steel_frame,
    built=2002,
    about='The building has an unusual, bulbous shape, purportedly intended to reduce its surface area and thus improve energy efficiency, although the excess energy consumption caused by the exclusive use of glass (in a double facade) overwhelms the benefit of shape. Despite claiming the building "demonstrates the potential for a sustainable, virtually non-polluting public building",[ energy use measurements have shown this building to be fairly inefficient in terms of energy use (375 kWh/m2/yr), with a 2012 Display Energy Performance Certificate rating of "E". Its designers reportedly saw it as a giant sphere hanging over the Thames, but opted for a more conventionally rooted building instead. It has no front or back in conventional terms but derives its shape from a modified sphere. A 500-metre (1,640 ft) helical walkway ascends the full ten stories. At the top is an exhibition and meeting space called "London\'s Living Room", with an open viewing deck which is occasionally open to the public. The walkway provides views of the interior of the building, and is intended to symbolise transparency; a similar device was used by Foster in his design for the rebuilt Reichstag (parliament), when Germany\'s capital was moved back to Berlin. The council chamber is located at the bottom of the helical stairway. The seats and desks for Assembly Members are arranged in a circular form (like the Round Table) with no clearly defined "head", podium, or chair where a speaker, council chairperson, or mayor might be seated. Raised tiers of seats for visitors or observers are located to one side.',
    user=arj
    )

    db.commit()
