TCP Client-Server Project
📌 Project Description

This project is a simple TCP-based client-server application developed in Python.
The system works as a quiz game where the server asks the client about capital cities of countries, and the client tries to guess the correct answer.

The communication between client and server is established using TCP sockets.

⚙️ Technologies Used
-Python
-Socket Programming (TCP)
-Pandas (for reading Excel file)
-Random module

📁 Project Structure
TCP-Client-Server/
│── client.py
│── server.py
│── country_capital_list.xlsx

🚀 How It Works
-Server Side
-Reads country-capital data from an Excel file
-Selects a random country
-Sends the country name to the client
-Receives guesses from the client
-Checks correctness and sends feedback
-Allows up to 3 attempts

Client Side
-Connects to the server
-Receives a country name
-Sends guesses for the capital city
-Displays server responses
-Terminates when:
  -Correct answer is given
  -Maximum attempts reached
  -Invalid input is entered
  -User types END
  
▶️ How to Run
1. Start the Server
-python server.py
2. Start the Client
-python client.py

📌 Important Notes
-Make sure country_capital_list.xlsx is in the same directory as server.py
-Server must be running before starting the client
-Default configuration:
  IP: 127.0.0.1
  Port: 65432

🧠 Features
-TCP socket communication
-Input validation (no numeric values allowed)
-Case-insensitive answer checking
-Maximum attempt limit
-Graceful connection handling

❗ Error Handling
The system handles:
 -Invalid inputs
 -Connection termination
 -Maximum attempt limit
 -Server/client disconnection
