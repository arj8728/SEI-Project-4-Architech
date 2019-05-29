import React from 'react'
import ReactDOM from 'react-dom'
import axios from 'axios'

class App extends React.Component {

  componentDidMount() {
    axios.get('/api/buildings')
      .then(res => this.setState({ buildings: res.data }))
  }

  render() {
    if(!this.state) return <p>Loading...</p>
    return (
      <div>
        {this.state.buildings.map(building => <div key={building.id}>
          <h2>{building.name}</h2>
          <p>{building.architect}</p>
          <p>{building.address}</p>
          <img src={building.image} alt="image" />
        </div>)}
      </div>
    )
  }
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
)
