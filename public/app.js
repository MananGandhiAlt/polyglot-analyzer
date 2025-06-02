document.getElementById("analyzeBtn").addEventListener("click", async () => {
  const text = document.getElementById("inputText").value.trim();
  const resultArea = document.getElementById("resultArea");

  if (!text) {
    resultArea.textContent = "Please enter some text first.";
    return;
  }

  resultArea.textContent = "Analyzing…";

  try {
    // BUG: Wrong URL (should be /analyze, not /anlyze)
    const resp = await fetch("http://127.0.0.1:5000/anlyze", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });
    if (!resp.ok) {
      const err = await resp.json();
      resultArea.textContent = "Error: " + JSON.stringify(err, null, 2);
      return;
    }
    const data = await resp.json();
    resultArea.textContent = JSON.stringify(data, null, 2);
  } catch (e) {
    resultArea.textContent = "Fetch error: " + e.message;
  }
});
