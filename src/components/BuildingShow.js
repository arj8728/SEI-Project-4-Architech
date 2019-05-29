import React from 'react'
//import { Link } from 'react-router-dom'   ...FOR EDIT BUTTON...
import axios from 'axios'
// import Auth from '../../lib/Auth'

class BuildingShow extends React.Component {


  constructor(props) {
    super(props) // because this component needs `this.props`

    this.state = {
      building: null
    }

    // this.handleDelete = this.handleDelete.bind(this)
  }

  componentDidMount() {
    axios.get(`/api/buildings/${this.props.match.params.id}`)
      .then(res => this.setState({ building: res.data }))
  }

  // handleDelete() {
  //   const token = Auth.getToken()
  //   axios.delete(`/api/characters/${this.props.match.params.id}`, {
  //     headers: { 'Authorization': `Bearer ${token}` }
  //   })
  //     .then(() => this.props.history.push('/characters'))
  // }
  //
  // canModify() {
  //   // if the user is logged in AND the user's id matches the characters' user's id return true
  //   return Auth.isAuthenticated() && Auth.getPayload().sub === this.state.character.createdBy._id
  // }


  render() {
    if(!this.state.building) return null
    const { name, image, architect, style, constructions, address } = this.state.building

    return (
      <section className="section">
        <div className="container">
          <div className="level">
            <div className="level-left">
              <h1 className="title is-1">{name}</h1>
            </div>

            <hr />

            <div className="columns is-multiline">
              <div className="column is-half-desktop is-full-tablet">
                <figure className="image">
                  <img src={image} alt={name} />
                </figure>
              </div>

              <div className="media-content">
                <div className="content">
                  <h2 className="title is-4">Architect: {architect}</h2>
                </div>
              </div>
              <div className="media-content">
                <div className="content">
                  <h2 className="title is-4">Architectural Style: {style.name}</h2>
                </div>
              </div>
              <div className="media-content">
                <div className="content">
                  <h2 className="title is-4">Construction: {constructions.name}</h2>
                </div>
              </div>
              <div className="media-content">
                <div className="content">
                  <h2 className="title is-4"> {address}</h2>
                </div>
              </div>
            </div>

            <hr />
          </div>
        </div>
      </section>
    )
  }
}

export default BuildingShow
