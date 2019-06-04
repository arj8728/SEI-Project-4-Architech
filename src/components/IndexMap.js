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
    console.log(this.props, 'IndexMAP.PROPS')
    if (!this.props.buildings) {
      return <img className="loading" src="https://media1.giphy.com/media/2Fazjtp85yxQTgh0c/giphy.gif" />
    } else {
      return (
        <div className="location">
          <Map
            style='mapbox://styles/mapbox/streets-v9'
            center={[-0.07251, 51.51538]}
            zoom={[10.7]}
            containerStyle={{
              height: '80vh',
              width: '80vw'
            }}
          >

            {this.props.buildings.map(building =>
              <Marker className="marker"
                key={building.id}
                coordinates={[building.longitude, building.latitude]}
                anchor="bottom"
                onClick={() => this.handleMarkerClick(building)}
              >
                <img src={'../images/pin.png'}/>
              </Marker>
            )}

            {this.state.selectedBuilding &&
              <Link to ={`/buildings/${this.state.selectedBuilding.id}`} key={this.state.selectedBuilding.id}>
                <Popup className="popup"
                  coordinates={[this.state.selectedBuilding.longitude, this.state.selectedBuilding.latitude]}
                  offset={{
                    'bottom-left': [12, -38],  'bottom': [0, -38], 'bottom-right': [-12, -38]
                  }}>

                  <div>
                    <h3 className="poptitle">{this.state.selectedBuilding.name}</h3>
                    <img className="popupimage"src={this.state.selectedBuilding.images} alt={this.state.selectedBuilding.name}/>
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

// From Arj's App.js
// componentDidMount() {
//   navigator.geolocation.watchPosition((position) => {
//     const { latitude, longitude } = position.coords
//     this.setState({ location: { lat: latitude, lon: longitude } })
//   })
//
// }

// ARJ and Laura's Map.js
//
// import React from 'react'
// import mapboxgl from 'mapbox-gl'
//
// mapboxgl.accessToken = 'pk.eyJ1IjoibGhtdXJwaHkiLCJhIjoiY2p1dTNzcnNhMGRrMjN5cGl2cmFpNmR0bCJ9.dghNRjtlhnn5h6UTeqnrKA'
//
// class Map extends React.Component {
//
//   componentDidMount() {
//     const { lng, lat, zoom } = this.props
//
//     this.map = new mapboxgl.Map({
//       container: this.mapContainer,
//       style: 'mapbox://styles/mapbox/streets-v9',
//       center: [lng, lat],
//       zoom
//     })
//     this.map.scrollZoom.disable()
//   }
//
//
//   componentDidUpdate() {
//     if(this.markers) return false
//
//     this.markers = this.props.bikes.map(bike => {
//       const el = document.createElement('div')
//       el.className = 'marker'
//
//       new mapboxgl.Marker(el)
//         .setLngLat([bike.lon, bike.lat])
//         .addTo(this.map)
//     })
//   }
//
//   render() {
//
//     return (
//       <div ref={el => this.mapContainer = el} className="map" />
//     )
//   }
// }
//
// export default Map
