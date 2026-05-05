import { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const uploadFile = async () => {
    const formData = new FormData();
    formData.append("file", file);

    await fetch("http://127.0.0.1:8000/upload-doc", {
      method: "POST",
      body: formData,
    });

    alert("File uploaded");
  };

  const askQuestion = async () => {
    const res = await fetch("http://127.0.0.1:8000/ask", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ question }),
    });

    const data = await res.json();
    setAnswer(data.answer);
  };

  return (
    <div style={{ padding: 40 }}>
      <h2>AI Assistant</h2>

      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={uploadFile}>Upload</button>

      <br /><br />

      <input
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask question"
      />
      <button onClick={askQuestion}>Ask</button>

      <h3>Answer:</h3>
      <p>{answer}</p>
    </div>
  );
}

export default App;