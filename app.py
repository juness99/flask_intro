from flask import Flask, render_template
import random
app = Flask(__name__) #app로 변수 저장

@app.route("/") #@넣으면 시작을 정해줌
def hello():#def는 함수 hello를 정의
    return "<h1>안녕하세요</h1>" #안녕하세요를 반환
    
@app.route("/html_tag")#경로를 지정해준다
def html_tag():
    return """
    <h1>첫번째 줄!!!</h1>
    <h2>두번째 줄!!!</h1>
    """
    
#파일띄우기
#flask_intro 폴더안에 templates 폴더를 생성하고
#그안에 html_file.html파일을 생성

@app.route("/html_file")
def html_file():
    return render_template("html_file.html")
    
#templates 폴더안에 welcome.html 파일을 다시만든다.
@app.route("/welcome/<string:name>")#string 이안에 어떤 이름이던 변수로 저장시켜줌
def welcome(name):
    return render_template("welcome.html",people=name)
    
#http://0.0.0.0:8080/ 이주소는 그냥 기본 리턴주소

@app.route("/cube/<int:num>")
def cube(num): #메소드에 num 을쓸수있게 함
    triple= num*num*num
    return render_template("soso.html",triple=triple,num=num)#triple과 triple은 다른 개념
    #왼쪽triple은 cube.html에서만 사용가능한 변수
    #오른쪽 triple은 파이썬에서 사용하는 변수
    
@app.route('/lunch')
def lunch():
    menu=["돼지찌게","김치찌게","바보","돈까스"]
    pick = random.choice(menu)
    return render_template("httt.html",menu=pick)
    
@app.route('/rotto')#주소로들어가야 실행됨
def rotto():
    numttt = list(range(1,46))
    a=random.sample(numttt,6)
    s=sorted(a)
    return render_template("too.html",pi=s)
    

@app.route('/naver')
def naver():
    return render_template("naver.html")
    
@app.route('/google')
def google():
    return render_template("google.html")