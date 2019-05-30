import React from 'react'
import axios from 'axios'

import Auth from '../lib/Auth'

class BuildingNew extends React.Component {

  constructor() {
    super()

    this.state = {
      data: {},
      errors: {},
      styles: [],
      constructions: []
    }

    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  
  componentDidMount() {
    axios.get('/api/constructions')
      .then(res => this.setState({ constructions: res.data }))

    axios.get('/api/styles')
      .then(res => this.setState({ styles: res.data }))
  }


  handleChange(e) {
    const data = { ...this.state.data, [e.target.name]: e.target.value }
    this.setState({ data })
  }

  handleSubmit(e) {
    e.preventDefault()

    const token = Auth.getToken()

    axios.post('/api/buildings', this.state.data, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}` }
    })
      .then(() => this.props.history.push('/buildings'))
      .catch(err => this.setState({errors: err.response.data.errors}))
  }

  sortedConstructions(){
    return this.state.constructions.sort((a,b) => {
      if(a.name === b.name) return 0
      return a.name < b.name ? -1 : 1
    })
  }


  sortedStyles(){
    return this.state.styles.sort((a,b) => {
      if(a.name === b.name) return 0
      return a.name < b.name ? -1 : 1
    })
  }

  render() {
    console.log(this.state.constructions)
    return(
      <section className="section">
        <div className="container">
          <div className="columns is-centered">
            <div className="column is-half-desktop is-two-thirds-tablet">


              <h1 className="title is-3"> Add a new Building</h1>
              <form onSubmit={this.handleSubmit}>

                <div className="field">
                  <label className="label">Name</label>
                  <div className="control">
                    <input
                      className="input"
                      type="text"
                      name="name"
                      placeholder="eg: Building in London"
                      onChange={this.handleChange} />
                  </div>
                  {this.state.errors.name && <div className="help is-danger">{this.state.errors.name}</div>}
                </div>


                <div className="field">
                  <label className="label">Image</label>
                  <div className="control">
                    <input
                      className="input"
                      name="image"
                      placeholder="eg: https://bigbuilding.png"
                      onChange={this.handleChange}
                      value={this.state.data.image || ''}
                    />
                  </div>
                  {this.state.errors.image && <div className="help is-danger">{this.state.errors.image}</div>}
                </div>

                <div className="field">
                  <label className="label">Architect:</label>
                  <div className="control">
                    <input
                      className="input"
                      type="text"
                      name="architect"
                      placeholder="eg: Norman Foster"
                      onChange={this.handleChange} />
                  </div>
                  {this.state.errors.architect && <div className="help is-danger">{this.state.errors.architect}</div>}
                </div>

                <div className="field">
                  <label className="label">Construction:</label>
                  <div className="select">
                    <select onChange={this.handleChange} name="construction_id">
                      {this.sortedConstructions().map(construction =>
                        <option
                          key={construction.id}
                          value={construction.name}>
                          {construction.name}
                        </option>
                      )}
                    </select>
                  </div>
                  {this.state.errors.construction_id && <div className="help is-danger">{this.state.errors.construction_id}</div>}
                </div>

                <div className="field">
                  <label className="label">Architectural Style:</label>
                  <div className="select">
                    <select onChange={this.handleChange} name="style_id">
                      {this.sortedStyles().map(style =>
                        <option
                          key={style.id}
                          value={style.name}>
                          {style.name}
                        </option>
                      )}
                    </select>
                  </div>
                  {this.state.errors.style_id && <div className="help is-danger">{this.state.errors.style_id}</div>}
                </div>


                <div className="field">
                  <label className="label">Address</label>
                  <div className="control">
                    <input
                      className="input"
                      type="text"
                      name="address"
                      placeholder="eg: 1 Seaside Avenue, Hastings"
                      onChange={this.handleChange} />
                  </div>
                  {this.state.errors.address && <div className="help is-danger">{this.state.errors.address}</div>}
                </div>


                <div className="field">
                  <label className="label">Postcode</label>
                  <div className="control">
                    <input
                      className="input"
                      name="postcode"
                      placeholder="eg: SE1 4NN"
                      value={this.state.data.postcode || ''}
                      onChange={this.handleChange}
                    />
                  </div>
                </div>
                {this.state.errors.postcode && <div className="help is-danger">{this.state.errors.postcode}</div>}



                <div className="field">
                  <label className="label">Built</label>
                  <div className="control">
                    <input
                      className="input"
                      name="built"
                      placeholder="eg: 1806"
                      value={this.state.data.built || ''}
                      onChange={this.handleChange}
                    />
                  </div>
                </div>
                {this.state.errors.built && <div className="help is-danger">{this.state.errors.built}</div>}



                <button
                  className="button is-primary is-centered">
                      Add Building
                </button>
              </form>

            </div>
          </div>
        </div>


      </section>
    )
  }
}

export default BuildingNew

// {this.state.styles.map(style =>
//
//   <select value ={this.state.style_id} onChange={this.handleChange} name="style_id">
//     <option value="1">{style._id}</option>
//     <option value="2">Greek Revival</option>
//     <option value="3">Modern</option>
//     <option value="4">Brutalist</option>
//   </select>
// </div>
// )}
