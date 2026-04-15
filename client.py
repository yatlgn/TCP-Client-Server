from socket import * #for functions in the socket library


#server's port and IP address
servername = "127.0.0.1"
serverport = 65432
buffersize = 1024 #sufficient buffer size for the strings to be entered


#socket creation and connection to the designated server
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((servername, serverport))

country = clientSocket.recv(buffersize).decode().strip() #getting the country name from the server, converting bytes to strings, and removing spaces

finished = False #flag that checks if the program has finished
question = True #flag for the first question to be asked in a different format


#the loop continues until the program finishes
while finished == False:

    #It sends the question and then asks subsequent questions accordingly
    if question == True:
        ans = input("What is the capital city of " + country + "? Your guess (or 'END' to finish): ").strip()
        question = False
    else:
        ans = input("Your guess (or 'END' to finish): ").strip()

    clientSocket.send(ans.encode()) #the user's response is sent to the server and the string is converted to a byte

    if ans == "END":
        print("Client closed.")
        finished = True

    else:
        try:
            message = clientSocket.recv(buffersize).decode() #the response is received from the server and converted to a string

            if message == "":
                print("Connection closed.")
                finished = True

            #print the message received from the server to the screen and evaluate it accordingly.
            else:
                print(message)

                if "Correct" in message:
                    finished = True
                elif "invalid" in message.lower():
                    finished = True
                elif "connection will close" in message.lower():
                    finished = True
                elif "Maximum attempts reached" in message:
                    finished = True
        #this error occurs if the server closes the connection.
        except ConnectionAbortedError:
            print("Connection closed by server.")
            finished = True
        
        #general catch for all other errors
        except:
            print("Connection closed.")
            finished = True

clientSocket.close() #client is completely shut down