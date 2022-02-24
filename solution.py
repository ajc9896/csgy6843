from socket import *
import base64


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\nMy message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    # Fill in end

    # recv = clientSocket.recv(1024).decode()

    #comment print before submitting
    # print(recv) #You can use these print statement to validate return codes from the server.
    # if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())


    # recv1 = clientSocket.recv(1024).decode()

    #comment print before submitting
    # print(recv1)
    # if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start

    mailFrom = "MAIL FROM: <ac0590@yahoo.com>\r\n"
    clientSocket.send(mailFrom.encode())
    # recv2 = clientSocket.recv(1024)

    ####
    # print(recv2)

    # if recv1[:3] != '250':
    #     print('250 reply not recieved from server')
    ###


    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcptTo = "RCPT TO: <destination@gmail.com> \r\n"
    clientSocket.send(rcptTo.encode())
    # recv3 = clientSocket.recv(1024)
    # print(recv3)
    # if recv1[:3] != '250':
    #     print('250 reply not received from server.')
    # Fill in end

    # Send DATA command and handle server response.

    # Fill in start
    data = "DATA\r\n"
    clientSocket.send(data.encode())
    # recv4 = clientSocket.recv(1024)
    # print(recv4)
    # if recv1[:3] != '250':
    #     print('250 reply not received from server.')
    # Fill in end

    # Send message data.
    
    # Fill in start

    clientSocket.send(msg.encode())
    
    # # Fill in end

    
    
    # Message ends with a single period, send message end and handle server response.
   
    # Fill in start

    clientSocket.send(endmsg.encode())

    # recv_msg = clientSocket.recv(1024)
    # print(recv_msg)


    # Fill in end


    # Send QUIT command and handle server response.

    # Fill in start
    quit = "QUIT \r\n"
    clientSocket.send(quit.encode())

    # end = clientSocket.recv(1024)
    # print(end)


    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')