export default function SearchBar({ value, onChange }) {
  return (
    <label className="search-bar" htmlFor="chemical-search">
      <span className="search-label">Search chemical, UN number, CAS, or synonym</span>
      <input
        id="chemical-search"
        type="search"
        value={value}
        onChange={(event) => onChange(event.target.value)}
        placeholder="Example: chlorine, UN1017, 7664-41-7"
        autoComplete="off"
      />
    </label>
  );
}
