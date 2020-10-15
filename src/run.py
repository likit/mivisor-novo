import sys
import threading

import webview
from app import start_server

if __name__ == '__main__':
    t = threading.Thread(target=start_server)
    t.daemon = True
    t.start()

    webview.start(debug=True)
    sys.exit()
