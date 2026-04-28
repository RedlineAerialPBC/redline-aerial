export default function ChemicalCard({ chemical, isActive, onSelect }) {
  return (
    <article className={isActive ? "chemical-card is-active" : "chemical-card"}>
      <button type="button" className="card-button" onClick={() => onSelect(chemical)}>
        <div className="card-top-row">
          <h2>{chemical.name}</h2>
          <span className="placard">Placard {chemical.placard}</span>
        </div>
        <p className="card-sub">{chemical.category} • {chemical.unNumber} • {chemical.casNumber}</p>
        <p className="card-threat">{chemical.threat}</p>
      </button>
    </article>
  );
}
