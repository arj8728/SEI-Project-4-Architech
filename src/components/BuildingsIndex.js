import React from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'

import BuildingCard from './BuildingCard'
import IndexMap from './IndexMap'

class Index extends React.Component {

  constructor() {
    super()

    this.state = {
      buildings: [],
      view: 'map'
    }
    this.setView = this.setView.bind(this)
  }

  setView(view) {
    this.setState({ view })
  }

  componentDidMount() {
    axios('/api/buildings')
      .then(res => this.setState({ buildings: res.data }))
  }

  render() {
    return (
      <section className="section">
        <div className="container">

          <div className="level-left">
            <button className="button is-danger fas fa-map-marker-alt" onClick={() => this.setView('map')}>Map view</button>
            <button className="button is-danger fas fa-list" onClick={() => this.setView('list')}>List View</button>
          </div>
          {this.state.view === 'map' &&
            <IndexMap className="show" buildings={this.state.buildings}/>
          }
          {this.state.view === 'list' &&

          <div className="columns is-multiline">
            {this.state.buildings.map(building =>
              <div key={building._id} className="column is-one-quarter-desktop is-one-third-tablet">
                <Link to={`/buildings/${building._id}`}>
                  <BuildingCard {...building} />
                </Link>
              </div>
            )}
          </div>
          }
        </div>
      </section>
    )
  }
}

export default Index


//   {Auth.isAuthenticated() && <Link to="/buildings/new" className="button">Add Building</Link>} //this was in render just after div className="container"
