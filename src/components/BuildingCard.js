import React from 'react'

const BuildingCard = ({ name, image, architect, style, constructions, address }) => {
  return (
    <div className="card">
      <div className="card-header">
        <h3 className="card-header-title">{name}</h3>
      </div>
      <div className="card-image">
        <figure className="image">
          <img src={image} alt={name} />
        </figure>
      </div>
      <div className="card-content">
        <div className="content">
          <p>Architect: {architect}</p>
        </div>
      </div>
      <div className="card-content">
        <div className="content">
          <p>Architectural Style: {style.name}</p>
        </div>
      </div>
      <div className="card-content">
        <div className="content">
          <p>Construction: {constructions.name}</p>
        </div>
      </div>
      <div className="card-content">
        <div className="content">
          <p>{address}</p>
        </div>
      </div>
    </div>
  )
}

export default BuildingCard
