import React from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'
import Auth from '../lib/Auth'
//import BuildingMap from './BuildingMap'

class BuildingShow extends React.Component {


  constructor(props) {
    super(props) // because this component needs `this.props`

    this.state = {
      building: null
    }

    this.handleDelete = this.handleDelete.bind(this)
  }

  componentDidMount() {
    axios.get(`/api/buildings/${this.props.match.params.id}`)
      .then(res => this.setState({ building: res.data }))

    if (navigator.geolocation) {
      navigator.geolocation.watchPosition((position) => {
        const { latitude, longitude } = position.coords
        this.setState({ location: { lat: latitude, lon: longitude } })
      })
    }
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
    return Auth.isAuthenticated() && Auth.getPayload().sub === this.state.building.user._id
  }


  render() {
    console.log(this.state.lat)
    const state = this.state.building
    if(!this.state.building) return null

    return (
      <section className="section">
        <div className="container">
          <div className="level">
            <div className="level-left">
              <h1 className="title is-1">{state.name}</h1>
            </div>

            {this.canModify() &&
              <div className="level-right">
                <Link to={`/buildings/${state._id}/BuildingEdit`} className="button is-warning is-outlined">delete</Link>
                <button className="button is-danger is-outlined" onClick={this.handleDelete}>Delete</button>
              </div>
            }
          </div>
          <div className="media-content">
            <div className="content">
              <h2 className="title is-5"> {state.address}</h2>
            </div>
          </div>
          <hr />

          <div className="columns is-multiline">
            <div className="column is-half-desktop is-full-tablet">
              <figure className="image">
                <img src={state.image} alt={state.name} />
              </figure>

            </div>

            <div className="media-content">
              <div className="content">
                <h2 className="title is-4">Architect: {state.architect}</h2>
              </div>
            </div>
            <div className="media-content">
              <div className="content">
                <h2 className="title is-4">Architectural Style: {state.style.name}</h2>
              </div>
            </div>

            <div className="media-content">
              <div className="content">
                <p className="title is-6"> {state.about}</p>
              </div>
            </div>


            <br />

            <button className="button is-warning has-text-grey dir-btn is-outlined is-info"><a href={`https://www.google.com/maps/dir/?api=1&origin=${this.state.lat},${this.state.lon}&destination=${state.latitude},${state.longitude}`} target="blank">Directions in Google Maps</a></button>
            <br />

            <button className="button is-success has-text-grey dir-btn is-outlined is-info"><a href={`https://citymapper.com/directions?startcoord=${this.state.lat},${this.state.lon}&endcoord=${state.latitude},${state.longitude}`} target="blank">Directions in CityMapper</a></button>

          </div>
        </div>
      </section>
    )
  }
}
export default BuildingShow



// in line 85   <BuildingMap date={state} />  from before we removed the buildingMap component






//this.state.constructions.map

// <div className="media-content">
//   <div className="content">
//     <h2 className="title is-4">Construction: {state.constructions.name}</h2>
//   </div>
// </div>
