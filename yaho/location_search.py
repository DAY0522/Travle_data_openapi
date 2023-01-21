from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'This is Home!'


@app.route('/test', methods=['POST'])
def get_req():
    req = request.get_json()
    print(req)
    return "good job!"


engTypeToKorJS='''
function success({ coords, timestamp }) {
    const latitude = coords.latitude;   // 위도
    const longitude = coords.longitude; // 경도
    
    alert(`위도: ${latitude}, 경도: ${longitude}, 위치 반환 시간: ${timestamp}`);
    return [latitude, longitude, timestamp] 
}
'''

engTypeToKorJS2='''
function getUserLocation() {
    if (!navigator.geolocation) {
        throw "위치 정보가 지원되지 않습니다.";
    }
    navigator.geolocation.getCurrentPosition(success);
}
'''

if __name__ == '__main__':  
    app.run('0.0.0.0',port=5000,debug=True)   
    # # engTypeToKor = js2py.eval_js(engTypeToKorJS2)
    # aa = engTypeToKor()




