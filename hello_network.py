import socket


def simple_http_request():
    # telnet data.pr4e.org 80
    # GET /romeo.txt HTTP/1.1
    # Host: data.pr4e.org
    cmd = 'GET /romeo.txt HTTP/1.1\r\n'
    cmd += 'Host: data.pr4e.org\r\n\r\n'
    # encode() converts unicode python string with default system encoding (usually UTF-8)
    cmd = cmd.encode()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('data.pr4e.org', 80))
    s.send(cmd)

    print('***** START RECEIVING RESPONSE *****')
    buffer_size = 256
    data = s.recv(buffer_size)
    print(data.decode())

    while len(data) > 0:
        print('********** LOOP ITERATION **********')
        data = s.recv(buffer_size)
        print(data.decode())

    s.close()


simple_http_request()
