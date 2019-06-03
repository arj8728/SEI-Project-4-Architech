import React from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'


import BuildingCard from './BuildingCard'
import IndexMap from './IndexMap'

class BuildingsIndex extends React.Component {

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
                <Link to={`/buildings/${building.id}`}>
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

export default BuildingsIndex


//   {Auth.isAuthenticated() && <Link to="/buildings/new" className="button">Add Building</Link>} //this was in render just after div className="container"

//             <div className="container">
//
//
// styles: [],
// filteredBuildings: [],
// query: '',

// this.filterBuildings = this.filterBuildings.bind(this)


// // *****
// handleInputChange() {
//   this.setState({
//     query: this.search.value
//   }, this.filterBuildings)
//
// }
//
// filterBuildings(){
//   let filteredBuildings = this.state.filteredBuildings
//   const buildings = this.state.buildings
//   const query = this.state.query
//   filteredBuildings = buildings.filter(building =>
//     building.name.toLowerCase().includes(query.toLowerCase()) ||
//   building.architect.toLowerCase().includes(query.toLowerCase())
//   )
//   this.setState({ filteredBuildings: filteredBuildings })
//   console.log(this.state)
//
// }
// *****
//
//   <form>
//     <input
//       placeholder="Search by architectural style"
//       ref={input => this.search = input}
//       // value={this.search}
//       onChange={this.handleInputChange}
//       className="form-input subtitle is-size-6-mobile"
//     />
//   </form>
// </div>
// <div className="container">
//   <div>
//     {this.state.query === ''
//       ?
//       <h1 className="explore-title">All Buildings</h1>
//       :
//       <h1 className="explore-title">Search Results</h1>}
//   </div>
//   {!this.state.filteredBuildings.length > 0
//     ?
//     <div className="columns is-mobile">
//       <p className="column is-size-4 is-12 has-text-centered">No results found</p>
//     </div>
//     :
//     <div>
//       {this.state.filteredBuildings && this.state.filteredBuildings.map(
//         filteredBuilding => <BuildingCard key={filteredBuilding._id} filteredBuilding={filteredBuilding}/>
//       )}
//     </div>
//   }
//
// </div>
//
