export default function TabFilters({ tabs, selectedTab, onSelect }) {
  return (
    <div className="tabs" role="tablist" aria-label="Chemical categories">
      {tabs.map((tab) => (
        <button
          key={tab.id}
          type="button"
          role="tab"
          aria-selected={selectedTab === tab.id}
          className={selectedTab === tab.id ? "tab is-active" : "tab"}
          onClick={() => onSelect(tab.id)}
        >
          {tab.label}
        </button>
      ))}
    </div>
  );
}
