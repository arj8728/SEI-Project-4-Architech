import React from 'react'
import axios from 'axios'

import Auth from '../lib/Auth'

class BuildingNew extends React.Component {

  constructor() {
    super()

    this.state = {
      data: {},
      errors: {}



    }

    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  componentDidMount() {
    axios.get('/api/constructions')
      .then(res => this.setState({ constructions: res.data }))
  }

  handleChange(e) {
    const data = { ...this.state.data, [e.target.name]: e.target.value }
    this.setState({ data })
  }

  handleSubmit(e) {
    e.preventDefault()

    const token = Auth.getToken()

    axios.post('/api/buildings', this.state.data, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
      .then(() => this.props.history.push('/buildings'))
  }

  render() {
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
                      name="title"
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
                      placeholder="eg: https://gameofthrones.fandom.com/jon-snow.png"
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
                  <label className="label">Architectural Styles:</label>
                  <div className="control">
                    <input
                      className="input"
                      type="text"
                      name="style"
                      placeholder="eg: 4"
                      onChange={this.handleChange} />
                  </div>
                  {this.state.errors.style&& <div className="help is-danger">{this.state.errors.style}</div>}
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
