import React from 'react'
import axios from 'axios'

class Register extends React.Component {


  constructor() {
    super()

    this.state = {
      data: {},
      errors: {}
    }

    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  handleChange(e) {
    // merge data on state with new data from the form
    const data = { ...this.state.data, [e.target.name]: e.target.value }
    // set the data back on state
    this.setState({ data }) // equivalent to { data: data }
  }

  handleSubmit(e) {
    e.preventDefault()
    axios.post('/api/register', this.state.data)
      .then(() => this.props.history.push('/login')) // redirect the user to the login page...
      .catch(err => this.setState({ errors: err.response.data.errors }))
  }

  render() {
    console.log(this.state)
    return (
      <section className="section">
        <div className="register-page">

          <div className="container">
            <div className="columns is-centered">
              <div className="column is-half-desktop is-two-thirds-tablet">
                <form onSubmit={this.handleSubmit}>

                  <div className="field">
                    <label className="label">Username</label>
                    <div className="control">
                      <input
                        className="input"
                        name="username"
                        placeholder="eg: leela3000"
                        onChange={this.handleChange}
                      />
                    </div>


                  </div>

                  <div className="field">
                    <label className="label">Email</label>
                    <div className="control">
                      <input
                        className="input"
                        name="email"
                        placeholder="eg: leela@planetexpress.nnyc"
                        onChange={this.handleChange}
                      />
                    </div>

                  </div>

                  <div className="field">
                    <label className="label">Password</label>
                    <div className="control">
                      <input
                        className="input"
                        name="password"
                        type="password"
                        placeholder="eg: ••••••••"
                        onChange={this.handleChange}
                      />
                    </div>

                  </div>

                  <div className="field">
                    <label className="label">Password Confirmation</label>
                    <div className="control">
                      <input
                        className="input"
                        name="password_confirmation"
                        type="password"
                        placeholder="eg: ••••••••"
                        onChange={this.handleChange}
                      />
                    </div>

                  </div>

                  <button className="button is-warning">Submit</button>
                </form>
              </div>
            </div>
          </div>
          <img className="loginPic" src="http://www.fixationsart.com/wp-content/uploads/2019/04/pin-on-house-with-regard-to-great-40-house-building-drawing.jpg" />
        </div>
      </section>
    )
  }
}

export default Register
