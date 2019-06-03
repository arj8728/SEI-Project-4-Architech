import React from 'react'
import SlideShow from 'react-image-show'

const Slider = (props) => {
  console.log(props)
  return (
    <SlideShow
      images={props.images}
      width="800px"
      imagesWidth="600px"
      imagesHeight="450px"
      imagesHeightMobile="56vw"
      thumbnailsWidth="920px"
      thumbnailsHeight="12vw"
      thumbnails fixedImagesHeight
      infinite
    />
  )
}

export default Slider
