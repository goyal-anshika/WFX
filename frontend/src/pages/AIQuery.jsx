import { useState } from "react";
import { askAI } from "../services/api";
import Loading from "../components/Loading";

function AIQuery() {

  const [question, setQuestion] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const submitQuestion = async (event) => {

    event.preventDefault();

    if (!question.trim()) {
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);

    try {

      const data = await askAI(question);

      setResult(data);

    } catch (err) {

      setError(
        err.response?.data?.detail ||
        err.message ||
        "Unable to process question."
      );

    } finally {

      setLoading(false);

    }
  };

  return (
    <div className="page">

      <div className="page-header">
        <h1>AI Query</h1>
        <p>Ask questions about your WFX ERP data.</p>
      </div>

      <form
        className="query-box"
        onSubmit={submitQuestion}
      >

        <textarea
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Example: How many finished goods are there?"
          rows={4}
        />

        <button
          type="submit"
          disabled={loading}
        >
          {loading ? "Thinking..." : "Ask AI"}
        </button>

      </form>

      {error && (
        <div className="error">
          {error}
        </div>
      )}

      {loading && (
        <Loading text="AI is processing your question..." />
      )}

      {result && !loading && (

        <div className="ai-result">

          <section className="result-section">

            <h2>Answer</h2>

            <div className="answer">
              {result.answer}
            </div>

          </section>

          <section className="result-section">

            <h2>Generated SQL</h2>

            <pre>
              {result.sql}
            </pre>

          </section>

          <section className="result-section">

            <h2>Results</h2>

            <pre>
              {JSON.stringify(
                result.results,
                null,
                2
              )}
            </pre>

          </section>

        </div>

      )}

    </div>
  );
}

export default AIQuery;