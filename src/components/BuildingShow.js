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
    console.log(this.props, 'buildingshow.PROPS')
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
                <Link to={`/buildings/${state._id}/BuildingEdit`} className="button is-primary">Edit</Link>
                <button className="button is-danger" onClick={this.handleDelete}>Delete</button>
              </div>
            }
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
                <h2 className="title is-4"> {state.address}</h2>
              </div>
            </div>





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
