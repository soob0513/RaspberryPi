#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
import random as rd

def recognize_celebrities(photo):
    celeb = ['제니', '츄', '오해원', '김지원']
    client = boto3.client('rekognition')

    with open(photo, 'rb') as image:
        response = client.recognize_celebrities(Image={'Bytes': image.read()})
#    rand_num = rd.randint(0,4)
    rand_celeb = rd.choice(celeb)
    # 닮은 사람이 없을 때 리스트에서 랜덤으로 한 명 뽑아서 출력하기
    # 닮은 사람은 ooo입니다.
    if len(response['CelebrityFaces']) == 0 :
        print('닮은 사람은 {}입니다.'. format(rand_celeb))
    else :
        print('닮은 사람은 {}입니다.'.format(response['CelebrityFaces'][0]['Name']))
    
#     print('Detected faces for ' + photo)
#     for celebrity in response['CelebrityFaces']:
#         print('Name: ' + celebrity['Name'])
#         
#         print('Id: ' + celebrity['Id'])
#         print('KnownGender: ' + celebrity['KnownGender']['Type'])
#         print('Smile: ' + str(celebrity['Face']['Smile']['Value']))
#         print('Position:')
#         print('   Left: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Height']))
#         print('   Top: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Top']))
#         print('Info')
#         for url in celebrity['Urls']:
#             print('   ' + url)
#         print()
    return len(response['CelebrityFaces'])

def main():
    photo = 'six.jpeg'
    celeb_count = recognize_celebrities(photo)
    print("Celebrities detected: " + str(celeb_count))

if __name__ == "__main__": 
    main()