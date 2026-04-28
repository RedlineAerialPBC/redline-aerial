function Stat({ label, value }) {
  return (
    <div className="stat">
      <p>{label}</p>
      <strong>{value}</strong>
    </div>
  );
}

export default function ChemicalCard({ chemical }) {
  return (
    <article className="chemical-card">
      <header>
        <h2>{chemical.name}</h2>
        <span className="placard">Placard {chemical.placard}</span>
      </header>

      <div className="stat-grid">
        <Stat label="UN Number" value={chemical.unNumber} />
        <Stat label="CAS Number" value={chemical.casNumber} />
        <Stat label="Category" value={chemical.category.replace("-", " ")} />
      </div>

      <section>
        <h3>Primary Hazards</h3>
        <ul>
          {chemical.hazards.map((hazard) => (
            <li key={hazard}>{hazard}</li>
          ))}
        </ul>
      </section>

      <section>
        <h3>Recommended PPE</h3>
        <p>{chemical.ppe}</p>
      </section>

      <section>
        <h3>Initial Actions</h3>
        <p>{chemical.initialActions}</p>
      </section>
    </article>
  );
}
