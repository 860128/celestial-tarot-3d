import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8899
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run():
    os.chdir(DIRECTORY)
    # 查找可用端口
    global PORT
    while PORT < 9000:
        try:
            with socketserver.TCPServer(("", PORT), Handler) as httpd:
                url = f"http://localhost:{PORT}/index.html"
                print(f"==================================================")
                print(f"  3D 虚幻塔罗牌已启动！")
                print(f"  本地运行地址: {url}")
                print(f"  正在自动为你打开浏览器...")
                print(f"  (关闭此黑色窗口即可停止运行)")
                print(f"==================================================")
                webbrowser.open(url)
                httpd.serve_forever()
                break
        except OSError:
            PORT += 1

if __name__ == '__main__':
    run()
