async function fetchSSLInfo() {
  const website = document.getElementById("website").value;
  const response = await fetch(
    `http://127.0.0.1:5000/get-ssl-info?website=${encodeURIComponent(website)}`
  );
  const data = await response.json();

  const certificateInfo = document.getElementById("certificate-info");
  if (data.success) {
    certificateInfo.innerHTML = `
                    <h2>SSL Certificate Information:</h2>
                    <pre>${JSON.stringify(data.certificate, null, 2)}</pre>
                `;
  } else {
    certificateInfo.innerHTML = `
                    <h2>Error:</h2>
                    <p>${data.error}</p>
                `;
  }
}
