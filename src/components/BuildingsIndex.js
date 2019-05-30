import React from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'
import Auth from '../lib/Auth'

import BuildingCard from './BuildingCard'

class Index extends React.Component {

  constructor() {
    super()

    this.state = {
      buildings: []
    }
  }

  componentDidMount() {
    axios('/api/buildings')
      .then(res => this.setState({ buildings: res.data }))
  }

  render() {
    return (
      <section className="section">
        <div className="container">
          {Auth.isAuthenticated() && <Link to="/buildings/new" className="button">Add Building</Link>}
          <hr />
          <div className="columns is-multiline">
            {this.state.buildings.map(building =>
              <div key={building._id} className="column is-one-quarter-desktop is-one-third-tablet">
                <Link to={`/buildings/${building._id}`}>
                  <BuildingCard {...building} />
                </Link>
              </div>
            )}

          </div>
        </div>
      </section>
    )
  }
}

export default Index
