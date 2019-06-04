import React from 'react'
// import { Link } from 'react-router-dom'
import axios from 'axios'
import Auth from '../lib/Auth'
import Slider from './Slider'

class BuildingShow extends React.Component {


  constructor(props) {
    super(props) // because this component needs `this.props`

    this.state = {
      building: null,
      location: {}
    }

    this.handleDelete = this.handleDelete.bind(this)
  }

  componentDidMount() {
    axios.get(`/api/buildings/${this.props.match.params.id}`)
      .then(res => this.setState({ building: res.data }))

    //***From Arj's
    axios('/api/buildings')
      .then(res => this.setState({ buildings: res.data }))

    navigator.geolocation.watchPosition((position) => {
      const { latitude, longitude } = position.coords
      // setting location on the state. So, latititude and longitude are now on this.state.location.lat and this.state.location.lon
      this.setState({ location: { lat: latitude, lon: longitude } })
    })
  }


  handleDelete() {
    const token = Auth.getToken()
    axios.delete(`/api/buildings/${this.props.match.params.id}`, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
      .then(() => this.props.history.push('/buildings'))
  }

  canModify() {
    // if the  user is logged in AND the user's id matches the buildings' user's id return true
    return Auth.isAuthenticated() && Auth.getPayload().sub === this.state.building.user.id
  }


  render() {
    if(!this.state.building) return null

    const images = this.state.building.images
    const photos = images
    console.log(photos, 'photos')
    console.log(this.state, 'state')

    const building = this.state.building

    return (
      <section className="section">
        <div className="container">
          <div className="level">
            <div className="level-left">
              <h1 className="building-title title is-1">{building.name}</h1>
            </div>
          </div>
          <div className="media-content">
            <div className="content">
              <h2 className="title is-5"> {building.address}</h2>
            </div>

            <button className="google button is-warning has-text-grey dir-btn is-outlined is-info"><a href={`https://www.google.com/maps/dir/?api=1&origin=${this.state.location.lat},${this.state.location.lon}&destination=${building.latitude},${building.longitude}`} target="blank">Directions in Google Maps</a></button>

            <button className="city button is-success has-text-grey dir-btn is-outlined is-info"><a href={`https://citymapper.com/directions?startcoord=${this.state.location.lat},${this.state.location.lon}&endcoord=${building.latitude},${building.longitude}`} target="blank">Directions in CityMapper</a></button>

          </div>
          <hr />
          <div className="columns">

            <div className="left-column">
              <div className="columns is-multiline">
                <div className="column is-half-desktop is-full-tablet">
                  <Slider images={photos}/>
                </div>
              </div>

            </div>


            <div className="show media-content">
              <div className="content ">
                <h2 className="title is-4">Architect: {building.architect}</h2>
                <h2 className="title is-4">Architectural Style: {building.style.name}</h2>
              </div>

              <div className="content">
                <p className="title is-6"> {building.about}</p>
              </div>
            </div>

            {this.canModify() &&
              <div className="level-right">


                <button className="button is-danger is-outlined" onClick={this.handleDelete}>Delete</button>
              </div>
            }

          </div>
        </div>
      </section>
    )
  }
}
export default BuildingShow


// <Link to={`/buildings/${building.id}/Edit`} className="button is-warning is-outlined">Edit</Link>

// in line 85   <BuildingMap date={state} />  from before we removed the buildingMap component






//this.state.constructions.map

// <div className="media-content">
//   <div className="content">
//     <h2 className="title is-4">Construction: {state.constructions.name}</h2>
//   </div>
// </div>
