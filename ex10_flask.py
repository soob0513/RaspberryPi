from flask import Flask
import led18
import ex09_select as db

app = Flask (__name__)

@app.route('/')

def index():
    return"<h1>Hello World!</h1>"   # --> http://localhost:5000/ 이었을 때 출력


# 라우팅 : 특정 엔드 포인트에 대한 클라이언트 요청에 서버가 응답하는 방법을 결정하는 것 (네비게이션과 비슷)
# --> 위에 한 건 '/'경로에 대한 응답 방법을 결정한 것

# /led/on 라우팅, 응답은 "LED ON"
# /led/off, "LED OFF"

@app.route('/led/on')
def led_on():
    led18.led_on()
    return "<h1>LED ON</h1>"  # --> http://localhost:5000/led/on 이었을 때 출력
    # return gp.output(18,gp.HIGH)

@app.route('/led/off')
def led_off():
    led18.led_off()
    return "<h1>LED OFF</h1>"   # --> http://localhost:5000/led/off 이었을 때 출력
    # return gp.output(18, gp.LOW)
    

@app.route('/select')
def slt():
    r = db.select_db()
    return r

# if __name__ == "__main__" :
#    app.run(host='localhost', port=5000)
    
if __name__ == "__main__" :
    app.run(host='192.168.219.56', port=5000)
# host : 터미널에서 ifconfig --> inet 

