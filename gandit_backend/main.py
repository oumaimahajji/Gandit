import serial
import socket

s = socket.socket()
host = socket.gethostname()

port = 6688
s.bind((host, port))
s.listen(5)


arduino = serial.Serial('/dev/ttyACM0', 9600) #ttyACM0


def main():
    data= str(arduino.readline(), 'utf-8')
    values = data.split(" ")


    value_P1 = int(values[1].strip())
    value_F2 = int(values[3].strip())
    gesteF2 = 'IDLE'
    gesteP1= 'IDLE'
    geste = 'aaaaa'

    if 600 >= value_F2 and value_F2 > 400:
        gesteF2 = 'IDLE'
    if 400 <= value_F2 and value_F2 >= 300:
        gesteF2 = 'BENT'
    if 299 <= value_F2 and value_F2 <= 0:
        gesteF2 = 'TOOBENT'
    # pour p
    if value_P1 == 0 :
        gesteP1 = 'IDLE'
    elif 700 < value_P1 :
        gesteP1 = 'PRESSED'
    elif value_P1 < 300:
        gesteP1 = 'LITTLEPRESSED'
    if gesteP1 == 'PRESSED' and gesteF2 == 'BENT':
        geste = 'STOP_MUSIC'
    elif gesteP1 == 'IDLE' and gesteF2 == 'BENT':
        geste = 'PLAY_MUSIC'
    
    #print(geste)
    return geste

#def main():
#    return 'killme'
c, addr = s.accept()
while True:
    
    value = main()
    print(value) # printing the value
     # Establish connection with client.
    c.send(str.encode(value))
