import React from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'
import Auth from '../lib/Auth'

import BuildingCard from './BuildingCard'
//import IndexMap from './IndexMap'

class Index extends React.Component {

  constructor() {
    super()

    this.state = {
      buildings: []
      //MapView: true,
      //ListView: false
    }
    //this.MapView = this.MapView.bind(this)
    //this.ListView = this.ListView.bind(this)
    //}

  // ListView() {
  //     this.setState({
  //       MapView: false,
  //       ListView: true
  //     })
  //   }
  //
  //   MapView() {
  //     this.setState({
  //       MapView: true,
  //       ListView: false
  //     })
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
