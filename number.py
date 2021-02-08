from pywinauto import Desktop, Application
from time import sleep
import warnings
import datetime
warnings.simplefilter("ignore", UserWarning)


def findRoblox():
    app = Application().connect(title="Roblox")
    windowsclient = app.Roblox

    return windowsclient

def clickKey(client):
    client.type_keys('{F9 down}{F9 up}')
    sleep(0.5)


client = None

while(True):
    
    if client is None:
        client = findRoblox()
    

    isMin = client.is_minimized()

    clickKey(client)
    # dlg = app.window()
    clickKey(client)
    
    if isMin == True:
        client.minimize()

    print('Send Key : ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    sleep(300)
    