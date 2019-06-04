import React from 'react'
import SlideShow from 'react-image-show'

const Slider = (props) => {
  console.log(props)
  return (
    <SlideShow
      images={props.images}
      width="500px"
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
