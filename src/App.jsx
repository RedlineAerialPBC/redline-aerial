import "./App.css";
import { useMemo, useState } from "react";
import ChemicalCard from "./components/ChemicalCard";
import ResultsSummary from "./components/ResultsSummary";
import SearchBar from "./components/SearchBar";
import TabFilters from "./components/TabFilters";
import { CHEMICALS, CHEMICAL_TABS } from "./data/chemicals";

function matchesSearch(chemical, query) {
  const normalized = query.trim().toLowerCase();

  if (!normalized) return true;

  const haystack = [
    chemical.name,
    chemical.unNumber,
    chemical.casNumber,
    chemical.category,
    ...(chemical.aka || []),
    ...(chemical.synonyms || []),
    ...chemical.hazards,
    chemical.threat,
    chemical.idlh,
    chemical.rel,
    chemical.pel,
    chemical.vaporDensity,
    chemical.flashPoint,
    chemical.flammableRange,
    chemical.boilingPoint,
    chemical.specificGravity,
    chemical.waterSolubility,
    chemical.physicalProperties,
    chemical.waterReactivity,
    chemical.incompatibles,
    chemical.meters,
    chemical.firstDueActions,
    chemical.hazmatTeamActions,
    chemical.ppeTree,
  ]
    .join(" ")
    .toLowerCase();

  return haystack.includes(normalized);
}

export default function App() {
  const [selectedTab, setSelectedTab] = useState("all");
  const [searchTerm, setSearchTerm] = useState("");

  const filteredChemicals = useMemo(() => {
    return CHEMICALS.filter((chemical) => {
      const tabMatch = selectedTab === "all" || chemical.category === selectedTab;
      const queryMatch = matchesSearch(chemical, searchTerm);

      return tabMatch && queryMatch;
    });
  }, [searchTerm, selectedTab]);

  return (
    <main className="app-shell">
      <header className="app-header">
        <p className="kicker">Field Reference</p>
        <h1>Rapid Chemical Response Guide</h1>
        <p>
          Mobile-first hazardous material lookup for firefighters. Use category tabs and search to quickly find
          UN/CAS identifiers, key hazards, and initial action reminders.
        </p>
      </header>

      <section className="controls" aria-label="chemical search and filters">
        <SearchBar value={searchTerm} onChange={setSearchTerm} />
        <TabFilters tabs={CHEMICAL_TABS} selectedTab={selectedTab} onSelect={setSelectedTab} />
      </section>

      <ResultsSummary total={CHEMICALS.length} visible={filteredChemicals.length} />

      {filteredChemicals.length === 0 ? (
        <div className="empty-state">
          <h2>No results found</h2>
          <p>Try a different search term or switch to another tab.</p>
          <button
            type="button"
            onClick={() => {
              setSearchTerm("");
              setSelectedTab("all");
            }}
          >
            Clear filters
          </button>
        </div>
      ) : (
        <section className="card-grid" aria-label="chemical results">
          {filteredChemicals.map((chemical) => (
            <ChemicalCard key={chemical.id} chemical={chemical} />
          ))}
        </section>
      )}
    </main>
  );
}
