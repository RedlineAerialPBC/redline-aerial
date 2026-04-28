export default function ResultsSummary({ total, visible }) {
  return (
    <p className="results-summary" aria-live="polite">
      Showing <strong>{visible}</strong> of <strong>{total}</strong> chemicals.
    </p>
  );
}
