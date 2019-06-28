# Project 4: Architech -  A React.js and Python Flask Full stack website

### Timeframe
7 days

## Technologies used
* JavaScript (ES6)
* ReactJS
* HTML5
* Python
* Flask
* Marshmallow
* PostgreSQL
* SCSS
* Bulma
* Axios
* PonyORM
* JWT
* Webpack
* Git/ GitHub
* Insomnia
* filestack-react
* react-image-show
* react-mapbox-gl


## APIs:
* Postcodes.io
* Google and CityMapper API


## Installation
1. Clone or download the repo
2. Open the `index.html` in your browser of choice
3. Install yarn for the JavaScript packages
4. Install pipenv for the Python packages
5. Launch the server with 'yarn run:server'
6. Launch the front-end with 'yarn run:client'

## Overview - Our Application: Architech

![Architech Screenshot](https://user-images.githubusercontent.com/43292507/59630903-67623500-913e-11e9-9408-4cc661f85a49.jpg)

### Introduction

This was a pair programmed project between Charlotte Haylins and myself. The technical requirements were to build a full-stack application, using React front-end with a Python, Flask and PostgreSQL back-end. It was also required to have multiple relationships and CRUD functionality.

Link to our deployed project:
_https://architech-hero.herokuapp.com/#/_

### Process

We wanted to choose a topic or interest to both of us, with strong high quality visuals. We also desired to work on certain features such as maps and image carousels and include them in this project.

After a wire-framing session we decided on an Architectural based app focused on famous buildings in London. We mapped out the relationships between each building, its architect, its architectural style and the construction materials it was built with. We used Entity relationship diagrams to work these relationships out.

We decided to call the app 'Architech' a fusion of the technology and the architectural aspect of the site. We decided that our MVP would be to register, login, view the buildings index page, view a map and add a building and edit an existing building the user themselves had created. As a bonus challenge we decided to add in an image carousel for each building using react-image-show and uploading multiple images to each building from Instagram, Facebook, local drive or Google Images using filestack-react.  

User Register Page:

![Register page project 4](https://user-images.githubusercontent.com/43292507/59631442-b8265d80-913f-11e9-84ae-319b7d45243e.jpg)

User Login Page:

![Login page project 4](https://user-images.githubusercontent.com/43292507/59631629-3682ff80-9140-11e9-8ffc-f896c987e295.png)


Our map page displaying the buildings location in London:

![building map page](https://user-images.githubusercontent.com/43292507/59631048-c6c04500-913e-11e9-98be-8581789a25d9.jpg)

List view of the Buildings Index page:

![project 4 index page](https://user-images.githubusercontent.com/43292507/59631911-e9535d80-9140-11e9-9513-0138697e2425.jpg)

Llyods Building show page, displaying the image carousel, the architect and architect style data from the seeds.py file. Also we managed to get directions to the building Google maps and CityMapper from the Users locations.

![buildings show page llyods](https://user-images.githubusercontent.com/43292507/59632221-9d54e880-9141-11e9-9c4a-0b035cc14d51.jpg)


Add a new building, the Construction dropdown highlights how we arranged this relationship using the building and construction Python models and the seeds Python files:

![Add a new building with construction categories](https://user-images.githubusercontent.com/43292507/59632813-fe30f080-9142-11e9-95f8-13cf1e7441b2.jpg)

Clicking on the map markers redirects the user to the building show page:

![london city hall clickable map](https://user-images.githubusercontent.com/43292507/59633201-e017c000-9143-11e9-8187-ef3a486c814d.jpg)


### Challenges

 The image carousel react-image-show was straightforward to work with. To display multiple images we passed the images as an array and changed the seeds and the respective names in the python models files. However this made an impact on the Filestack component as we were originally allowing for the upload of one image as a string.

 Below is the slide show component I built using react-image-show. I passed the images as props and set the image dimensions.

```JavaScript
Import React from 'react'
import SlideShow from 'react-image-show'

const Slider = (props) => {
  console.log(props)
  return (
    <SlideShow
      images={props.images}
      width="600px"
      imagesWidth="500px"
      imagesHeight="450px"
      imagesHeightMobile="56vw"
      thumbnailsWidth="500px"
      thumbnailsHeight="12vw"
      thumbnails fixedImagesHeight
      infinite
    />
  )
}

export default Slider
```

The render method in BuildingShow.js was changed so that the images from the slider were passed into state.

```JavaScript
render() {
  if(!this.state.building) return null

  const images = this.state.building.images
  const photos = images
  console.log(photos, 'photos')
  console.log(this.state, 'state')
```


 Now  the images in the Building.py model had to be changed to an array as we were trying to display multiple images.
```Python
class Building(db.Entity):
images = Required(StrArray) # changed from (str) as list of images for carousel

```

Then we had errors when submitting a new image. We had to change the Filestack code to handle the upload of multiple images. This was done in the render function of our BuildingNew.js. This functionality was the standard method needed to upload multiple images using ReactFilestack 2.x.x

```JavaScript
  <label className="label">Image</label>
  <ReactFilestack
    buttonText="Upload Building Photo"
    buttonClass="button"
    options={{
      accept: ['image/*'],
      maxFiles: 8
    }}
    preload={true}
    onSuccess={this.handleUploadedImages}
  />

```

 Another challenge was to get the map to display newly added buildings. In the BuildingNew.js this is the code that was used. I liked this as it built on what I understood about ReactJS. On handleSubmit of a new building the postcodes were found and passed into state, we then returned this data and pushed this into /buildings which was our index.

 ```JavaScript
 handleSubmit(e) {
   e.preventDefault()
   const token = Auth.getToken()
   axios.get(`https://api.postcodes.io/postcodes/${this.state.data.postcode}`)
     .then(res => {
       console.log(res.data.result)
       const { longitude, latitude } = res.data.result
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

 ```


### Wins

 On the whole we were pleased with getting the React front-end and the Python/Flask back-end to work together and allow a user to follow the CRUD and RESTful operations. We were also happy that we managed out time well and implemented the bonus features. Working as a pair was very efficient and we found that troubleshooting any errors became relatively straightforward.


### Future features

In future we would like to add in a site search feature using React select to search by Architect and Architectural style. We would also have liked to add in some more architecture categories on the seeds file.


In terms of my personal learning I found that using React.js and Python was a challenge. I got better at using React.js and found new React features such as the slider from react-image-show, react file stack, ReactMapboxGl to be interesting and implementing them a good experience. This built on previous React.js projects and helped solidify my understanding. I would like to build more React.js websites and hope to continue with a medical side project.
