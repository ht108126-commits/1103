from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 使用 List 作為暫存資料庫
homework_list = []

@app.route('/', methods=['GET'])
def index():
    # 將作業列表傳遞給 index.html 模板渲染
    return render_template('index.html', homeworks=homework_list)

@app.route('/add', methods=['POST'])
def add_homework():
    # 接收來自前端表單的資料
    course_name = request.form.get('course_name')
    homework_name = request.form.get('homework_name')
    due_date = request.form.get('due_date')
    
    # 確保所有欄位都有填寫才加入列表
    if course_name and homework_name and due_date:
        homework_list.append({
            'course': course_name,
            'homework': homework_name,
            'due_date': due_date
        })
        
    # 新增完成後，重新導向回首頁
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)