<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>
<body>

  <h1>Morse Code Converter 🔤➡️⚫️⚪️</h1>

  <p>This is a simple Python script that converts a user-inputted message into <strong>Morse code</strong>. It supports uppercase and lowercase letters, numbers, punctuation, and spaces.</p>

  <h2>📌 Features</h2>
  <ul>
    <li>Converts letters (A–Z) and digits (0–9)</li>
    <li>Handles common punctuation (e.g., <code>.</code> <code>,</code> <code>?</code> <code>!</code> <code>@</code>)</li>
    <li>Represents spaces between words as <code>/</code></li>
    <li>Easy to use and beginner-friendly</li>
  </ul>

  <h2>🧠 How It Works</h2>
  <ol>
    <li>The script defines a dictionary called <code>morse_code</code> where each character is mapped to its Morse code equivalent.</li>
    <li>It takes a message from the user via <code>input()</code>.</li>
    <li>Each character in the message is converted to Morse code using the dictionary.</li>
    <li>The converted Morse code is printed, with characters separated by spaces.</li>
  </ol>

  <h2>🚀 Usage</h2>
  <p>To run the script:</p>
  <pre><code>python morse_code_converter.py</code></pre>

  <p><strong>Example:</strong></p>
  <pre>
what is your message? Hello, world!
.... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--
  </pre>

  <h2>📝 Code Overview</h2>
  <pre><code>
# Dictionary mapping letters, numbers, and symbols to Morse code
morse_code = {
    'A': '.-', 'B': '-...', ... ' ': '/'
}

# List to store the converted Morse code symbols
morse_code_message = []

# Function to convert message to Morse code
def msg_converter(message):
    for char in message:
        code = morse_code[char.upper()]
        morse_code_message.append(code)
    return print(' '.join(morse_code_message))

# Run the converter
msg_converter(input("what is your message?"))
  </code></pre>

  <h2>🛠️ Improvements (Optional Ideas)</h2>
  <ul>
    <li>Create a GUI version with Tkinter</li>
    <li>Allow saving Morse output to a file</li>
  </ul>

  <h2>📄 License</h2>
  <p>This project is open-source and free to use for learning and experimentation.</p>

</body>
</html>
