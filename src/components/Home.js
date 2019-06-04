import React from 'react'
// import { Redirect } from 'react-router'
import { Link } from 'react-router-dom'


const Home = () => {

  //   if(Auth.getToken()){
  //   return (<Redirect to="/BuildingsIndex" />)
  // } else {

  return (
    <div className="home-page">
      <div className="container">
        <br />
        <br />
        <br />
        <br />
        <br />
        <br />
        <div className="text container">
          <h1 className="title hometitle1">Architech</h1>
          <br />
          <div className="card-panel welcome">
            <div className="welcome-to-architect">
              <h5 className="intro-logo">Welcome to Architech</h5>
            </div>
            <br />
            <h6>A site for lovers of architecture. Join a community of like-minded enthusiasts and professionals. Architech is not just a site for the biggest and most famous buildings. Purvey the unique, undiscovered finds of  fellow Architechs by viewing their uploads, and sharing your own.</h6>
            <br />
            <div className="register-buttons">
              <Link to='/register' className="regnowbutt tab button is-warning has-text-grey">  Register Now  </Link>
              <br />
              <Link to='/buildings' className="reglaterbutt tab button is-warning has-text-grey">Register Later</Link>
            </div>
            <br />
            <div className="already-registered">
              <span>
               Already registered?
                <Link to="/login">&nbsp;Login here.</Link>
              </span>
            </div>
            <br />
          </div>

        </div>
      </div>

    </div>
  )
}


export default Home


//
// import React from 'react'
//
//
// const imagesBuildings  =[
//   'https://images.unsplash.com/photo-1490642914619-7955a3fd483c?ixlib=rb-1.2.1&auto=format&fit=crop&w=1070&q=80',
//   'https://pixel.nymag.com/imgs/daily/urbanist/2018/05/30/london-architecture/st-pauls-cathedral.w710.h473.jpg',
//   'https://www.britishtours.com/storage/files/architecture-city_4f8dc0ebd4bfe.jpg',
//   'https://images.unsplash.com/photo-1486623021874-2d24a5b1e148?ixlib=rb-1.2.1&auto=format&fit=crop&w=1489&q=80'
// ]
//
// class Home extends React.Component {
//   constructor(props) {
//     super(props)
//
//     this.state = {
//       images: imagesBuildings,
//       actualImage: 0
//     }
//   }
//


// <h2 className="subtitle1">London Buildings</h2>

// <section className="hero is-fullheight" style={{
//   backgroundImage: `url(${imagesBuildings[this.state.actualImage]})`
// }}>
//   <div className="hero-body">
//     <div className="container">
//       <h1 className="title hometitle1">Architech</h1>
//     </div>
//
//   </div>
//
// </section>
