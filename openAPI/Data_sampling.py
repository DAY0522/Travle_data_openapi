# 한국관광공사_국문 관광정보 서비스_GW
# https://www.data.go.kr/data/15101578/openapi.do

# openAPI에서 받아온 data를 샘플링하는 코드

import sampling_func

# url 입력
print(sampling_func.search_landmark('서울', '마포구'))
# 서울 / 마포구
# 경기도 / 수원시