#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

# 터미널창에 sudo pip3 install boto3 해서 설치
import boto3
# boto3 = aws에서 제공하는 sdk
# sdk = software development kit


def detect_labels_local_file(photo):


    client=boto3.client('rekognition')  # AWS의 rekognition에 boto3를 통해 접근 
   
    with open(photo, 'rb') as image:   # 매개변수로 받은 사진의 경로를 열고, image 변수로 사용(read byte)
        # 클라이언트의 detect_labels  
        response = client.detect_labels(Image={'Bytes': image.read()})
        # image 라는 것으로 받아올 건데 key는 Bytes이고 value는 image 파일 자체
        
#    print(response) 
        
#     print('Detected labels in ' + photo)  
#     for label in response['Labels']:
#         print (label['Name'] + ' : ' + str(label['Confidence']))

# 검출된 객체가 00일 확률은 00.00% 입니다.
    print('검출된 객체가 ' + response['Labels'][0]['Name'] + '일 확률은 '+ str(round(response['Labels'][0]['Confidence'],2)) + '%입니다.')
    return len(response['Labels'])

def main():
    photo='jisoo.jpg'

    label_count=detect_labels_local_file(photo)
    print("Labels detected: " + str(label_count))


if __name__ == "__main__":
    main()



