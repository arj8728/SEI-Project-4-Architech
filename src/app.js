import React from 'react'
import ReactDOM from 'react-dom'
// import axios from 'axios'
import { HashRouter as Router, Route, Switch } from 'react-router-dom'

import 'bulma'
import './style.scss'

import Navbar from './components/Navbar'
import FlashMessages from './components/FlashMessages'
import Home from './components/Home'
import Register from './components/Register'
import Login from './components/Login'
// import SecureRoute from './components/SecureRoute'

import BuildingNew from './components/BuildingNew'
import BuildingEdit from './components/BuildingEdit'
import BuildingShow from './components/BuildingShow'
import BuildingsIndex from './components/BuildingsIndex'


class App extends React.Component {

  render() {

    return (
      <Router>
        <main>
          <Navbar/>
          <FlashMessages />
          <Switch>

            <Route path="/buildings/:id/edit" component={BuildingEdit} />
            <Route path="/buildings/new" component={BuildingNew} />
            <Route path="/buildings/:id" component={BuildingShow} />
            <Route path="/buildings" component={BuildingsIndex} />

            <Route path="/register" component={Register} />
            <Route path="/login" component={Login} />
            <Route path="/" component={Home}/>

          </Switch>

        </main>
      </Router>
    )
  }
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
)
