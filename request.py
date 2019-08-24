import requests
import json


# image_url = 'https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2019/05/931/524/elon-musk-Reuters.jpg?ve=1&tl=1'

def req(image_url):
    subscription_key = "25b191679a0e4c128d914db84fe41bde"
    assert subscription_key
    face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

    # headers = {'Ocp-Apim-Subscription-Key': subscription_key}
    headers = {'Content-Type': 'application/octet-stream', 'Ocp-Apim-Subscription-Key': subscription_key}
    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,'
                                'accessories,blur,exposure,noise',
    }

    data = open(image_url, 'rb')
    response = requests.post(face_api_url, params=params,
                             headers=headers, data=data)  # json={"url": image_url})

    return json.dumps(response.json())
