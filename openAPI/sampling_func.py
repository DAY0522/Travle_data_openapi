import requests
import json
import pandas as pd
import url_Info
import random

def sampling_data_df(url): # url에 있는 필요한 정보를 불러오는 함수
    # url 불러오기
    response = requests.get(url, verify=False)
    # verify=False는 requests.exceptions.SSLError: HTTPSConnectionPool(host='apis.data.go.kr', port=443) 에러를 방지하기 위함.
    # 넣었는데도 에러가 발생한다면 사용중인 와이파이를 바꿔보자.

    #데이터 값 출력해보기
    Data = response.text # str

    # apiData를 json으로 변경
    json_Data = json.loads(Data) # json type으로 변경
    apiData = json_Data["response"]["body"]["items"]["item"] # 필요 부분만 가져옴

    df_data = pd.json_normalize(apiData) # Dataframe으로 변경
    return df_data

def sampling_data_json(url): # url에 있는 필요한 정보를 불러오는 함수
    # url 불러오기
    response = requests.get(url, verify=False)
    # verify=False는 requests.exceptions.SSLError: HTTPSConnectionPool(host='apis.data.go.kr', port=443) 에러를 방지하기 위함.
    # 넣었는데도 에러가 발생한다면 사용중인 와이파이를 바꿔보자.

    #데이터 값 출력해보기
    data = response.text # str

    # apiData를 json으로 변경
    json_data = json.loads(data) # json type으로 변경
    api_data = json_data["response"]["body"]["items"]["item"]
    
    return api_data

def make_area_key(area: str): 
    """ openAPI에 저장된 데이터에 접속해 사용자가 입력한 지역(area)의 고유번호를 반환.

    Args:
        area (str): 여행지를 검색하려는 지역명(ex. 서울, 부산, 대구 등)
    """
    
    area_url = url_Info.url_base # 지역이 담긴 api 주소 반환
    df_area = sampling_data_df(area_url) # 지역에 대한 데이터 샘플링

    # 입력한 지역에 대한 고유 번호 출력
    df_area = df_area.loc[df_area['name']==area]
    df_area_dict = df_area.to_dict()['code']
    
    for k, _ in df_area_dict.items(): # 더 효율적으로 짤 수 있을 거 같다.
        area_key = df_area_dict[k]
    
    return area_key 

def make_sigungu_key(area: str, sigungu: str): 
    """ openAPI에 저장된 데이터에 접속해 사용자가 입력한 시군구(sigungu)의 고유번호를 반환.

    Args:
        area (str): 여행지를 검색하려는 지역명(ex. 서울, 부산, 대구 등)
        sigungu (str): 여행지를 검색하려는 시군구명(ex. 관악구, 동대문구, 영등포구 등)
    """
    area_key = make_area_key(area) # 지역의 고유키 구하기
    sisgungu_url = url_Info.url_area.format(area=area_key) # 시군구가 담긴 api 주소 반환
    
    df_sigungu = sampling_data_df(sisgungu_url)

    # 입력한 지역에 대한 고유 번호 출력
    df_sigungu = df_sigungu.loc[df_sigungu['name']==sigungu]
    df_sigungu_dict = df_sigungu.to_dict()['code']
    
    for k, _ in df_sigungu_dict.items(): # 해당 코드 개선하자.
        sigungu_key = df_sigungu_dict[k]
    
    return (area_key, sigungu_key)

def search_landmark(area: str, sigungu: str):
    """ 사용자가 입력한 지역, 시군구에 대한 여행지 중 하나를 반환
    (일단 랜덤으로 반환하도록 설정)

    Args:
        area (str): 여행지를 검색하려는 지역명(ex. 서울, 부산, 대구 등)
        sigungu (str): 여행지를 검색하려는 시군구명(ex. 관악구, 동대문구, 영등포구 등)
    """
    
    key = make_sigungu_key(area, sigungu) # 알고 싶은 여행지의 지역 ket, 시군구 key 호출
    url_landmark = url_Info.url_sigungu.format(area=key[0], sigungu=key[1]) # 지역/시군구에 대한 여행지 url 생성
    json_landmark = sampling_data_json(url_landmark)
    index_landmark = random.randint(0, len(json_landmark)) # 출력할 landmark의 index를 랜덤으로 호출
    
    json_landmark = json_landmark[index_landmark] # 여행지 정보를 json type으로 변경
    img_landmark = get_landmark_img(json_landmark) # 여행지에 대한 img url 반환
    
    return json_landmark, img_landmark

def get_contentid(landmark):
    return landmark['contentid']

def get_landmark_img(landmark: json):
    """ 입력한 landmark에서 img 파일을 불러오는 함수

    Args:
        landmark (json): 특정 여행지에 대한 정보

    Returns:
        _type_: landmark's img url
    """
    contentid = get_contentid(landmark)
    url_img = url_Info.url_img.format(contentId=contentid)

    try:
        json_img = sampling_data_json(url_img)
    except:
        print("no image of the landmark.")
        return False
    
    # 이미지 정보를 2개 가져옴.
    # 2개보다 적을 경우를 대비해 전체 json 길이와 2 중 작은 값을 가져옴.
    max_img = min(len(json_img), 2)

    img_landmark = list()
    for i in range(max_img):
        img_landmark.append(json_img[i]['originimgurl']) # img url 저장

    return img_landmark