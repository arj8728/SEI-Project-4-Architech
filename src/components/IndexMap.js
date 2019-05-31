import React from 'react'
import { Link } from 'react-router-dom'
import ReactMapboxGl, { Marker, Popup } from 'react-mapbox-gl'

const Map = ReactMapboxGl({
  accessToken: process.env.MAPBOX_TOKEN
})

class IndexMap extends React.Component {

  constructor(props){
    super(props)

    this.state = {
      pin: {},
      pinClick: false
    }

  }

  handleMarkerClick(building) {
    if(building === this.state.selected) this.setState({ selectedBuilding: null })
    else this.setState({ selectedBuilding: building })
  }


  render() {
    console.log(this.props, 'THIS.PROPS')
    if (!this.props.buildings) {
      return <h1>Loading...</h1>
    } else {
      return (
        <div className="location">
          <Map
            style='mapbox://styles/mapbox/streets-v9'
            center={[-0.25, 51.1010]}
            zoom={[8]}
            containerStyle={{
              height: '80vh',
              width: '80vw'
            }}
          >

            {this.props.buildings.map(building =>
              <Marker className="marker"
                key={building._id}
                coordinates={[building.longitude, building.latitude]}
                anchor="bottom"
                onClick={() => this.handleMarkerClick(building)}
              >
                <img src={'../images/pin.png'}/>
              </Marker>
            )}

            {this.state.selectedBuilding &&
              <Link to ={`/buildings/${this.state.selectedBuilding._id}`} key={this.state.selectedBuilding._id}>
                <Popup className="popup"
                  coordinates={[this.state.selectedBuilding.longitude, this.state.selectedBuilding.latitude]}
                  offset={{
                    'bottom-left': [12, -38],  'bottom': [0, -38], 'bottom-right': [-12, -38]
                  }}>

                  <div>
                    <h3>{this.state.selectedBuilding.title}</h3>
                    <img className="popupimage"src={this.state.selectedBuilding.image} alt={this.state.selectedBuilding.name}/>
                    <h3> Price: {this.state.selectedBuilding.price} | Sleeps: {this.state.selectedBuilding.sleeps}</h3>
                  </div>
                </Popup>
              </Link>
            }

          </Map>
        </div>
      )
    }
  }
}

export default IndexMap
