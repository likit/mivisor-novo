import webview
import sys
import threading
import app

if __name__ == '__main__':
    t = threading.Thread(target=app.start_server)
    t.daemon = True
    t.start()

    webview.create_window('Mivisor Novo', f'http://localhost:{app.PORT}')
    webview.start(debug=True)
    sys.exit()
