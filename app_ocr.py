import pyocr
from flask import Flask, render_template, request
from PIL import Image

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    # リクエストファイルの読込
    ocr_file = request.files["ocrFile"]
    img = Image.open(ocr_file)
    # OCR準備
    tools = pyocr.get_available_tools()
    tool = tools[0]
    # OCR
    txt = tool.image_to_string(
        img,
        lang="eng+jpn",
        builder=pyocr.builders.TextBuilder()
    )
    print(txt)
    if txt == "":
        txt == "読み取りエラー"
    return render_template("index.html",)
#  txt == "txt"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
