import { useState } from "react";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return alert("Select file first");

    const formData = new FormData();
    formData.append("file", file);

    await fetch("http://127.0.0.1:8000/upload-doc/", {
      method: "POST",
      body: formData,
    });

    alert("Uploaded ✨");
  };

  const handleAsk = async () => {
    if (!question) return alert("Enter question");

    setLoading(true);

    const res = await fetch("http://127.0.0.1:8000/ask/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ question }),
    });

    const data = await res.json();
    setAnswer(data.answer || data.error);
    setLoading(false);
  };

  return (
    <div className="main">
      <div className="glass">
        <h1>✨ AI Document Assistant</h1>
        <p className="subtitle">Ask anything from your uploaded document</p>

        <div className="section">
          <input
            type="file"
            onChange={(e) => setFile(e.target.files[0])}
          />
          <button onClick={handleUpload}>Upload</button>
        </div>

        <div className="section">
          <input
            type="text"
            placeholder="Type your question..."
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
          />
          <button onClick={handleAsk}>Ask</button>
        </div>

        <div className="answer">
          {loading ? "✨ Thinking..." : answer || "Your answer will appear here"}
        </div>
      </div>
    </div>
  );
}

export default App;