import React from 'react'
import axios from 'axios'
import Auth from '../lib/Auth'
import ReactFilestack from 'filestack-react'

// const choices = {
//   accept: 'image/*',
//   transformations: {
//     rotate: true,
//     crop: true,
//     circle: true
//   }
// }

class BuildingEdit extends React.Component {

  constructor() {
    super()

    this.state = {
      data: {},
      errors: {},
      styles: [],
      constructions: [],
      file: null

    }

    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
    this.handleUploadedImages = this.handleUploadedImages.bind(this)
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

  handleUploadedImages(result) {
    const data = { ...this.state.data, images: result.filesUploaded.map(file => file.url) }
    this.setState({ data })
  }

  handleSubmit(e) {
    e.preventDefault()
    const token = Auth.getToken()
    axios.get(`https://api.postcodes.io/postcodes/${this.state.data.postcode}`)
      .then(res => {
        console.log(res.data.result)
        const { longitude, latitude } = res.data.result
        // ...means data being spread is no longer an object with longitude and latitude next to it. ... is removing the { }, so now the contents of the inner brackets is state as key/value pairs, followed by lat as another (lat:value) key value pair, and longitude as another key value pair
        this.setState({ data: {...this.state.data, longitude, latitude} })
      })
      .then(() => {

        return axios.post('/api/buildings', this.state.data, {
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
          }
        })
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
    return(
      <section className="section">
        <div className="container">
          <div className="columns is-centered">
            <div className="column is-half-desktop is-two-thirds-tablet">


              <h1 className="title is-3"> Edit Building</h1>
              <form onSubmit={this.handleSubmit}>

                <div className="field">
                  <label className="label">Name</label>
                  <div className="control">
                    <input
                      className="input"
                      type="text"
                      name="name"
                      value={this.state.data.name || ''}
                      placeholder="eg: 5 London Road"
                      onChange={this.handleChange} />
                  </div>
                  {this.state.errors.name && <div className="help is-danger">{this.state.errors.name}</div>}
                </div>


                <div className="field">

                  <label className="label">Image</label>
                  <ReactFilestack
                    apikey= {process.env.FILESTACK_TOKEN}
                    buttonText="Upload Photo Building"
                    buttonClass="button"
                    options={{
                      accept: ['image/*'],
                      maxFiles: 4
                    }}
                    preload={true}
                    onSuccess={this.handleUploadedImages}


                  />
                  {this.state.data.image && <img src={this.state.data.image} />}

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
                    <select name="construction.id" defaultValue="Choose a construction..." onChange={this.handleChange}>
                      <option disabled>Choose a construction...</option>
                      {this.sortedConstructions().map(construction =>
                        <option
                          key={construction.id}
                          value={construction.id}>
                          {construction.name}
                        </option>
                      )}
                    </select>
                  </div>
                  {this.state.errors.construction.id && <div className="help is-danger">{this.state.errors.construction.id}</div>}
                </div>

                <div className="field">
                  <label className="label">Architectural Style:</label>
                  <div className="select">
                    <select name="style.id" defaultValue="Choose an architectural style..." onChange={this.handleChange} >
                      <option disabled>Choose an architectural style...</option>
                      {this.sortedStyles().map(style =>
                        <option
                          key={style.id}
                          value={style.id}>
                          {style.name}
                        </option>
                      )}
                    </select>
                  </div>
                  {this.state.errors.style.id && <div className="help is-danger">{this.state.errors.style.id}</div>}
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
                  <label className="label">About</label>
                  <div className="control">
                    <input
                      className="input"
                      name="about"
                      placeholder="eg: The building's Portland Stone façade masks a..."
                      value={this.state.data.about || ''}
                      onChange={this.handleChange}
                    />
                  </div>
                </div>
                {this.state.errors.about && <div className="help is-danger">{this.state.errors.about}</div>}

                <button
                  className="button is-warning is-centered">
                      Edit Building
                </button>

              </form>
            </div>
          </div>
        </div>

      </section>
    )
  }
}

export default BuildingEdit
