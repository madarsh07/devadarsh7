<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Contact Form</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f4f4f4;
      padding: 20px;
    }
    .container {
      background: white;
      padding: 20px;
      max-width: 400px;
      margin: auto;
      box-shadow: 0 0 10px rgba(0,0,0,0.2);
      border-radius: 8px;
    }
    input, textarea {
      width: 100%;
      padding: 10px;
      margin-top: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    button {
      background-color: #4CAF50;
      color: white;
      padding: 10px;
      margin-top: 10px;
      border: none;
      width: 100%;
      cursor: pointer;
      font-size: 16px;
    }
    button:hover {
      background-color: #45a049;
    }
  </style>
</head>
<body>
  <div class="container">
    <h2>Contact Us</h2>
    <form id="contactForm">
      <label for="name">Name:</label>
      <input type="text" id="name" required>

      <label for="email">Email:</label>
      <input type="email" id="email" required>

      <label for="message">Message:</label>
      <textarea id="message" rows="4" required></textarea>

      <button type="submit">Send Message</button>
    </form>
    <p id="statusMsg" style="color: green;"></p>
  </div>

  <script>
    document.getElementById("contactForm").addEventListener("submit", function(e) {
      e.preventDefault(); // prevent real form submission
      const name = document.getElementById("name").value;
      document.getElementById("statusMsg").innerText = "Thanks, " + name + "! Your message was sent.";
    });
  </script>
</body>
</html>

