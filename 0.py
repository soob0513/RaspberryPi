# 한영 변경은 쉬프트 + 스페이스
# 확대는 컨트롤 쉬프트=
# 축소는 컨트롤 -
# 실행하는 단축키는 F5 혹은 위에 있는 Run버튼 클릭
# 여러 줄 주석은 alt + 3 주석 취소는 alt + 4 

# if True :
#     print("True")


# =====================================
# MariaDB 설치하기
# sudo apt-get install mariadb-server
# sudo mysql -u root
# alter user 'root'@'localhost' identified by '1234';  : 비밀번호 설정 
# 나가기 : Ctrl + C
# mysql -u root -p
# --> 비밀번호 1234 입력 (화면에 안 보임)
# create database test;
# use test;
# create table class (name varchar(5), age int, number varchar(15));
# insert into class(name, age, number) values ('김민수', 20, '010-7115-4513');
# select * from class;
# desc class;    --> 속성보기 
# create table sensordb(sensing int, ts timestamp default current_timestamp);
# desc sensordb;
# Thonny로 데이터 넣기 ex08_db.py
# select * from sensordb; 


# 새 터미널 창
# sudo pip3 install PyMySQL

# 테이블 삭제
# drop table 테이블명;
# 다시 create ~~;

# 테이블명 확인
# show tables;


# ======================================
# 카메라 설정
# sudo raspi-config
