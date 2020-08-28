from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbonewal  # 'dbsparta'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/customFavor')
def customFavor():
    return render_template('customfavor.html')

## API 역할을 하는 부분
@app.route('/profile', methods=['POST'])
def write_profile():
	# 2. DB에 정보 삽입하기
	# 3. 성공 여부 & 성공 메시지 반환하기
    # title_receive로 클라이언트가 준 title 가져오기
    print(request.form)
    name_receive = request.form['name_give']
    # author_receive로 클라이언트가 준 author 가져오기
    age_receive = request.form['age_give']
    # review_receive로 클라이언트가 준 review 가져오기
    job_receive = request.form['job_give']
    company_receive = request.form['company_give']
    comment_receive = request.form['comment_give']
    cases_receive = request.form['cases_give']
    favor_receive = request.form['favor_give']

    # DB에 삽입할 review 만들기
    profile = {
        'name': name_receive,
        'age': age_receive,
        'job': job_receive,
        'company' : company_receive,
        'comment': comment_receive,
    }

    # reviews에 review 저장하기
    db.reviews.insert_one(profile)
    # 성공 여부 & 성공 메시지 반환
    return jsonify({'result': 'success', 'msg': '리뷰가 성공적으로 작성되었습니다.'})

@app.route('/update', methods=['POST'])
def update_profile():
	# 2. DB에 정보 삽입하기
	# 3. 성공 여부 & 성공 메시지 반환하기
    # title_receive로 클라이언트가 준 title 가져오기
    print(request.form)
    cases_receive = request.form['cases_give']
    favor_receive = request.form['favor_give']

    # DB에 삽입할 review 만들기

    update = {
        'cases' : cases_receive,
        'favor' : favor_receive
    }
    db.reviews.update_one(update)
    # 성공 여부 & 성공 메시지 반환
    return jsonify({'result': 'success', 'msg': '리뷰가 성공적으로 작성되었습니다.'})


@app.route('/review', methods=['GET'])
def read_reviews():
    # 1. DB에서 리뷰 정보 모두 가져오기
    reviews = list(db.reviews.find({}, {'_id': 0}))
    # 2. 성공 여부 & 리뷰 목록 반환하기
    return jsonify({'result': 'success', 'reviews': reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)