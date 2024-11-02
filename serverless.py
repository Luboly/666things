from waitress import serve
from app import app

def handle_request(req, res):
    # 这里可以添加一些逻辑来处理请求，例如日志记录或请求修改
    pass

if __name__ == "__main__":
    serve(app, host="127.0.0.1", port=5000)