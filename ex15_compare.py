# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3

def compare_faces(sourceFile, targetFile):

    client = boto3.client('rekognition')

    imageSource = open(sourceFile, 'rb')
    imageTarget = open(targetFile, 'rb')

    # Similarity가 80 이상일 때만 같은 사람이라고 판단하고 결과를 가져옴 
    response = client.compare_faces(SimilarityThreshold=80,
                                    SourceImage={'Bytes': imageSource.read()},
                                    TargetImage={'Bytes': imageTarget.read()})

    for faceMatch in response['FaceMatches']:
        # 해당 얼굴이 인식된 좌표를 가져옴 
        # position = faceMatch['Face']['BoundingBox']
        # 얼마나 닮았는지 수치도 가져옴 
        similarity = str(faceMatch['Similarity'])
        # print('The face at ' +
        #      str(position['Left']) + ' ' +
        #      str(position['Top']) +
        #      ' matches with ' + similarity + '% confidence')
        print(similarity + '%')

    imageSource.close()
    imageTarget.close()
    return len(response['FaceMatches'])

def main():
    source_file = 'jisoo3.jpg'
    target_file = 'jennie.jpg'
    face_matches = compare_faces(source_file, target_file)
    print("Face matches: " + str(face_matches))

if __name__ == "__main__":
    main()