# 얼굴 인식 
from flask import Flask, render_template
# rapissam.tistory.com  --> 5주차 main2.html
import os
import boto3

def compare_faces():

    client = boto3.client('rekognition')
    # 원본 파일
    sourceFile = 'jisoo2.jpg'
    # 방금 찍은 파일
    targetFile = 'temp.jpg'
    
    imageSource = open(sourceFile, 'rb')
    imageTarget = open(targetFile, 'rb')

    # Similarity가 80 이상일 때만 같은 사람이라고 판단하고 결과를 가져옴 
    resp
    
    
    onse = client.compare_faces(SimilarityThreshold=80,
                                    SourceImage={'Bytes': imageSource.read()},
                                    TargetImage={'Bytes': imageTarget.read()})

    result = response['FaceMatches'][0]['Similarity']

    imageSource.close()
    imageTarget.close()
    return result


app = Flask(__name__)

@app.route('/')

def home() :
    return render_template('main2.html')

@app.route('/detect')
def index() :
    os.system('raspistill -o temp.jpg')
    result = compare_faces()


return str(result)

if __name__ =="__main__" :
    app.run(host='localhost', port=5000)