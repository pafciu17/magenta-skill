import socketio
from cachecontrol.controller import logger

logger.info("Connect!")
sio = socketio.Client()


def connectIfNeeded():
    if not sio.connected:
        logger.info("Connect!")
        print('connecting!')
        sio.connect('http://localhost:4021')
        logger.info("Connected!")
    else:
        print('already connected!')
connectIfNeeded()


def emit(type, value):
    print('emit')
    print(type, value)
    sio.emit(type, {'value': value})


def getConnection():
    return sio;
