# Important imports
from app import app
from flask import request, render_template
import os
from skimage.metrics import structural_similarity
import imutils
import cv2
from PIL import Image

# Adding path to config
app.config['INITIAL_FILE_UPLOADS'] = 'app/static/uploads'
app.config['EXISTNG_FILE'] = 'app/static/original'
app.config['GENERATED_FILE'] = 'app/static/generated'

# Route to home page
# 在 Flask 中，路由用于将 URL 请求映射到相应的视图函数。你可以使用装饰器（如 @app.route()）来定义路由。每个路由都与一个视图函数相关联，当匹配到对应的 URL 请求时，相应的视图函数将被调用来处理请求。
# 这里的视图函数是 index()，客户端通过浏览器或其他 HTTP 客户端访问根路径 / 时，index() 视图函数被调用。

@app.route("/", methods=["GET", "POST"])
def index():

    # request 是 Flask 中的一个对象，它代表了客户端发送的HTTP请求。在处理Web请求时，你可以使用 request 对象来访问请求中的各种信息，包括表单数据、URL参数、HTTP头部等。
	# Execute if request is get
    if request.method == "GET":
        # render_template 是 Flask web应用框架中的一个函数，它用于渲染HTML模板并将渲染后的HTML页面作为HTTP响应返回给客户端浏览器。这个函数通常用于生成动态的网页内容，其中包含了从服务器端传递到模板中的数据。
        # 一旦导入了render_template，你可以在路由处理函数中使用它来渲染HTML模板
        print('yes')
        return render_template("index.html")

	# Execute if reuqest is post
    if request.method == "POST":
        
        # Get uploaded image
        # request.files 是 request 对象的一个属性，用于访问客户端通过HTTP POST请求上传的文件数据。
        # 'file_upload' 是一个表单字段的名称，通常对应于HTML表单中的一个文件上传字段
        file_upload = request.files['file_upload']
        filename = file_upload.filename
        
        # Resize and save the uploaded image
        uploaded_image = Image.open(file_upload).resize((250,160))
        uploaded_image.save(os.path.join(app.config['INITIAL_FILE_UPLOADS'], 'image.jpg'))

        # Resize and save the original image to ensure both uploaded and original matches in size
        original_image = Image.open(os.path.join(app.config['EXISTNG_FILE'], 'image.jpg')).resize((250,160))
        original_image.save(os.path.join(app.config['EXISTNG_FILE'], 'image.jpg'))

        # Read uploaded and original image as array
        original_image = cv2.imread(os.path.join(app.config['EXISTNG_FILE'], 'image.jpg'))
        uploaded_image = cv2.imread(os.path.join(app.config['INITIAL_FILE_UPLOADS'], 'image.jpg'))

        # Convert image into grayscale
        original_gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
        uploaded_gray = cv2.cvtColor(uploaded_image, cv2.COLOR_BGR2GRAY)

        # Calculate structural similarity
        (score, diff) = structural_similarity(original_gray, uploaded_gray, full=True)
        diff = (diff * 255).astype("uint8")

        # Calculate threshold and contours
        thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        
        # Draw contours on image
        for c in cnts:
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(original_image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.rectangle(uploaded_image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Save all output images (if required)
        cv2.imwrite(os.path.join(app.config['GENERATED_FILE'], 'image_original.jpg'), original_image)
        cv2.imwrite(os.path.join(app.config['GENERATED_FILE'], 'image_uploaded.jpg'), uploaded_image)
        cv2.imwrite(os.path.join(app.config['GENERATED_FILE'], 'image_diff.jpg'), diff)
        cv2.imwrite(os.path.join(app.config['GENERATED_FILE'], 'image_thresh.jpg'), thresh)

        # 当视图函数返回一个内容时，Flask会默认将这个内容封装成一个HTTP响应对象并将其发送给客户端
        # 这个默认的HTTP响应对象使得在视图函数中返回内容非常方便，因为你只需要关注生成内容的逻辑，而不必担心创建和设置HTTP响应的细节。
        # 然后，Flask会自动处理这些细节，确保内容以正确的方式发送给客户端。
        return render_template('index.html',pred=str(round(score*100, 2)) + '%' + ' correct')
       
# Main function
if __name__ == '__main__':
    app.run(debug=True)
