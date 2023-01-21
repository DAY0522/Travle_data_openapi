import Default_func_api, Url_info
import random
import json

def search_location(state: json):
    """ 사용자의 근처(5km 이내) 여행지를 반환
    (일단 랜덤으로 반환하도록 설정)

    Args:
        position(json): 위치의 상태(에러 등), 사용자의 위치 정보
    """

    pos = state['data']
    url_location = Url_info.url_location.format(latitude=pos['latitude'], longitude=pos['longitude'])  # 근처 여행지에 대한 url 생성

    json_location = Default_func_api.sampling_data_json(url_location)
    index_location = random.randint(0, len(json_location))  # 출력할 landmark의 index를 랜덤으로 호출

    json_location = json_location[index_location]  # 여행지 정보를 json type으로 변경
    img_location = Default_func_api.get_landmark_img(json_location)  # 여행지에 대한 img url 반환

    return json_location, img_location
