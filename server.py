from socket import * #to use all the functions in the socket library
import pandas as pd  #to read excel
import random        #to make a random selection

#the port the server will run on and the required buffer size
serverport = 65432
buffersize = 1024

data = pd.read_excel("country_capital_list.xlsx") #reading an Excel file


#capture of countries and their capitals
country_capital = {}

for i in range(len(data)):
    country = str(data.iloc[i, 0]).strip()
    capital = str(data.iloc[i, 1]).strip()
    country_capital[country] = capital


#the creation of a TCP socket allows the server to connect to the specified IP and port and begin listening
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("127.0.0.1", serverport))
serverSocket.listen(1)

print("Server is listening on 127.0.0.1: " + str(serverport))

running = True #flag that controls whether the server should continue running
numCleint = 1  #counter to track which client it is


#wait for the client while the server is running
while running:
    print("Waiting for client #" + str(numCleint) + " ...")

    connectionSocket, addr = serverSocket.accept() #client connection is accepted and a new socket is created.
    print("Client connected from", addr)

    #random country is selected, its capital is found, the country name is converted from a string to a byte, and sent to the client
    country = random.choice(list(country_capital.keys()))
    correctCapital = country_capital[country]
    connectionSocket.send(country.encode())

    attempts = 0 #number of attempts by the user
    connected = True #checks client connection

    while connected:
        try:
            ans = connectionSocket.recv(buffersize).decode().strip() #receiving response from the client and converting it to a string
        except:
            break #the loop exits when an error occurs.
        
        if ans == "":
            connected = False

        elif ans == "END":
            print("END received. Server is closing.")
            running = False
            connected = False

        elif ans.replace(" ", "").isalpha() == False:
            connectionSocket.send("Numeric input is not allowed for capital names. Connection will close.".encode())
            print("Numeric input is not allowed; closing connection.")
            connected = False

        elif ans.lower() == correctCapital.lower():
            response = "Correct! " + correctCapital + " is the capital of " + country + ". Closing connection."
            connectionSocket.send(response.encode())
            print("Correct; closing connection.")
            connected = False

        else:
            attempts = attempts + 1


            #checking the user's response
            guess = ""

            for c in country_capital:
                if country_capital[c].lower() == ans.lower():
                    guess = c
                    break

            if guess != "":
                firstPart = "'" + ans + "' is the capital of " + guess + ", not " + country + "."
            else:
                firstPart = "'" + ans + "' is not the capital of " + country + "."

            if attempts < 3:
                response = firstPart + "\n" + "Wrong answer. Attempts left: " + str(3 - attempts) + ". Try again:"
                connectionSocket.send(response.encode())
            else:
                response = firstPart + "\n" + "Maximum attempts reached (3). The correct answer is " + correctCapital + ". Closing connection."
                connectionSocket.send(response.encode())
                print("Max attempts reached; closing connection.")
                connected = False

    connectionSocket.close() #the connection with the client is closed.
    numCleint = numCleint + 1 #next client number is increased

serverSocket.close() #server is completely shut down
