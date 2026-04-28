function valueOrDash(value) {
  if (Array.isArray(value)) return value.length ? value.join(", ") : "—";
  return value && String(value).trim() ? value : "—";
}

function Field({ label, value }) {
  return (
    <div className="field-row">
      <dt>{label}</dt>
      <dd>{valueOrDash(value)}</dd>
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

      <dl className="details-grid">
        <Field label="AKA" value={chemical.aka} />
        <Field label="Category" value={chemical.category} />
        <Field label="UN number" value={chemical.unNumber} />
        <Field label="CAS number" value={chemical.casNumber} />
        <Field label="Threat" value={chemical.threat} />
        <Field label="IDLH" value={chemical.idlh} />
        <Field label="REL" value={chemical.rel} />
        <Field label="PEL" value={chemical.pel} />
        <Field label="Vapor density" value={chemical.vaporDensity} />
        <Field label="Flash point" value={chemical.flashPoint} />
        <Field label="Flammable range" value={chemical.flammableRange} />
        <Field label="Boiling point" value={chemical.boilingPoint} />
        <Field label="Specific gravity" value={chemical.specificGravity} />
        <Field label="Water solubility" value={chemical.waterSolubility} />
        <Field label="Physical properties" value={chemical.physicalProperties} />
        <Field label="Water reactivity" value={chemical.waterReactivity} />
        <Field label="Incompatibles" value={chemical.incompatibles} />
        <Field label="Meters" value={chemical.meters} />
        <Field label="First-due actions" value={chemical.firstDueActions} />
        <Field label="HazMat team actions" value={chemical.hazmatTeamActions} />
        <Field label="PPE tree" value={chemical.ppeTree} />
      </dl>
    </article>
  );
}
