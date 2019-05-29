import React from 'react'
import ReactDOM from 'react-dom'
// import axios from 'axios'
import { HashRouter as Router, Route, Switch } from 'react-router-dom'

import Home from './components/Home'


import 'bulma'
import './style.scss'

class App extends React.Component {

  render() {

    return (
      <Router>
        <main>
          <Switch>

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
