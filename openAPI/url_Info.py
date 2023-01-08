# 본인이 openAPI 사이트에서 발급받은 인증키 입력

serviceKey = ''

url_base = 'https://apis.data.go.kr/B551011/KorService/areaCode?MobileOS=ETC&MobileApp=AppTest&_type=json&serviceKey=' + serviceKey
url_area = 'http://apis.data.go.kr/B551011/KorService/areaCode?serviceKey='+ serviceKey +'&numOfRows=100&pageNo=1&MobileOS=ETC&MobileApp=AppTest&_type=json&areaCode={area}'
url_sigungu = 'https://apis.data.go.kr/B551011/KorService/areaBasedList?MobileOS=ETC&MobileApp=AppTest&_type=json&numOfRows=50000&serviceKey=' + serviceKey + '&areaCode={area}&sigunguCode={sigungu}'
url_img = 'http://apis.data.go.kr/B551011/KorService/detailImage?serviceKey=' + serviceKey + '&numOfRows=10&pageNo=1&MobileOS=ETC&MobileApp=AppTest&contentId={contentId}&subImageYN=Y&_type=json'