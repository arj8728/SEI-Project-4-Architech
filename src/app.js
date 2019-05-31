import React from 'react'
import ReactDOM from 'react-dom'
// import axios from 'axios'
import { HashRouter as Router, Route, Switch } from 'react-router-dom'

import Navbar from './components/Navbar'
import FlashMessages from './components/FlashMessages'
import Home from './components/Home'
import Register from './components/Register'
import Login from './components/Login'
// import SecureRoute from './components/SecureRoute'

import BuildingNew from './components/BuildingNew'
import BuildingEdit from './components/BuildingEdit'
import BuildingsIndex from './components/BuildingsIndex'
import BuildingShow from './components/BuildingShow'
import IndexMap from './components/IndexMap'


import 'bulma'
import './style.scss'

class App extends React.Component {

  render() {

    return (
      <Router>
        <main>
          <Navbar/>
          <FlashMessages />
          <Switch>

            <Route path="/buildings/map" component={IndexMap} />

            <Route path="/buildings/:id/Edit" component={BuildingEdit} />
            <Route path="/buildings/new" component={BuildingNew} />

            <Route path="/register" component={Register} />
            <Route path="/login" component={Login} />

            <Route path="/buildings/:id" component={BuildingShow} />
            <Route path="/buildings" component={BuildingsIndex} />
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
