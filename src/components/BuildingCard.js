import React from 'react'

const BuildingCard = ({ name, images, architect }) => {
  return (
    <div className="card">
      <div className="card-header">
        <h3 className="topcard card-header-title">{name}</h3>
      </div>
      <div className="card-image">
        <figure className="image">
          <img src={images[0]} alt={name} />
        </figure>
      </div>
      <div className="card-content">
        <div className="content">
          <p>Architect: {architect}</p>
        </div>
      </div>

    </div>
  )
}

export default BuildingCard

// , style, construction, address

// <div className="card-content">
//   <div className="content">
//     <p>Architectural Style: {style.name}</p>
//   </div>
// </div>
// <div className="card-content">
//   <div className="content">
//     <p>Construction: {construction.name}</p>
//   </div>
// </div>
// <div className="card-content">
//   <div className="content">
//     <p>{address}</p>
//   </div>
// </div>
