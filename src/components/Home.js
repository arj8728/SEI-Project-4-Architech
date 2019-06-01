import React from 'react'

const imagesBuildings  =[
  'https://images.unsplash.com/photo-1490642914619-7955a3fd483c?ixlib=rb-1.2.1&auto=format&fit=crop&w=1070&q=80',
  'https://pixel.nymag.com/imgs/daily/urbanist/2018/05/30/london-architecture/st-pauls-cathedral.w710.h473.jpg',
  'https://www.britishtours.com/storage/files/architecture-city_4f8dc0ebd4bfe.jpg',
  'https://images.unsplash.com/photo-1486623021874-2d24a5b1e148?ixlib=rb-1.2.1&auto=format&fit=crop&w=1489&q=80'
]

class Home extends React.Component {
  constructor(props) {
    super(props)

    this.state = {
      images: imagesBuildings,
      actualImage: 0
    }
  }


  componentDidMount() {
    setInterval(() => {
      let actualImage = this.state.actualImage + 1
      actualImage === this.state.images.length ? actualImage = 0:null
      this.setState({ actualImage })
    }, 1900)
  }

  render() {
    return (
      <section className="hero is-fullheight" style={{
        backgroundImage: `url(${imagesBuildings[this.state.actualImage]})`
      }}>
        <div className="hero-body">
          <div className="container">
            <h1 className="title hometitle1">Architech</h1>
            <h2 className="subtitle1">London Buildings</h2>
          </div>

        </div>

      </section>

    )
  }
}




export default Home
