import "./App.css";
import { useMemo, useState } from "react";
import ChemicalCard from "./components/ChemicalCard";
import DetailPanel from "./components/DetailPanel";
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
  const [selectedChemicalId, setSelectedChemicalId] = useState(null);

  const filteredChemicals = useMemo(() => {
    return CHEMICALS.filter((chemical) => {
      const tabMatch = selectedTab === "all" || chemical.category === selectedTab;
      const queryMatch = matchesSearch(chemical, searchTerm);
      return tabMatch && queryMatch;
    });
  }, [searchTerm, selectedTab]);

  const selectedChemical =
    filteredChemicals.find((chemical) => chemical.id === selectedChemicalId) ?? filteredChemicals[0] ?? null;

  return (
    <main className="app-shell">
      <header className="app-header">
        <p className="kicker">Field Reference</p>
        <h1>Rapid Chemical Response Guide</h1>
        <p>Search, select, and review full chemical response details.</p>
      </header>

      <section className="controls" aria-label="chemical search and filters">
        <SearchBar value={searchTerm} onChange={setSearchTerm} />
        <TabFilters tabs={CHEMICAL_TABS} selectedTab={selectedTab} onSelect={setSelectedTab} />
      </section>

      <ResultsSummary total={CHEMICALS.length} visible={filteredChemicals.length} />

      <section className="workspace" aria-label="chemical workspace">
        <section className="card-grid" aria-label="chemical results">
          {filteredChemicals.map((chemical) => (
            <ChemicalCard
              key={chemical.id}
              chemical={chemical}
              isActive={chemical.id === selectedChemicalId}
              onSelect={(item) => setSelectedChemicalId(item.id)}
            />
          ))}
        </section>

        <DetailPanel chemical={selectedChemical} />
      </section>
    </main>
  );
}
