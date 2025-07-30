async function generateCaptions() {
  const theme = document.getElementById("theme").value;
  const tone = document.getElementById("tone").value;
  const mood = document.getElementById("mood").value;
  const platform = document.getElementById("platform").value;
  const hashtags = document.getElementById("hashtags").value
    .split(",")
    .map(tag => tag.trim())
    .filter(tag => tag !== "");

  const response = await fetch("/generate", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      theme,
      tone,
      mood,
      platform,
      hashtags
    })
  });

  const data = await response.json();
  const captionsDiv = document.getElementById("captions");
  captionsDiv.innerHTML = "";

  if (data.captions && data.captions.length) {
    data.captions.forEach(caption => {
      const div = document.createElement("div");
      div.className = "caption";
      div.textContent = caption;
      captionsDiv.appendChild(div);
    });
  } else {
    captionsDiv.textContent = "No captions generated.";
  }
}
