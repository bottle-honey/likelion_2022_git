import smtplib
from email.message import EmailMessage
#이미지의 확장자 판단모듈
import imghdr
#정규표현식 모듈
import re
#서버 주소와 포트번호가 필요
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

def sendEmail(addr):
    #유효성 검사
    #이메일 주소 정규표현식 : ^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    
    #3 SMTP 서버에 메일을 보냄(메일 내용)
    if bool(re.match(reg,addr)):
       smtp.send_message(message)
       print("전송완료")
    else:
        print("유효한 이메일 주소가 아닙니다.")
EMAIL = "honey_sheep@likelion.org"
#MIME : SMTP 서버가 이해할 수 있는 형식 ))으로 변환해야함
message = EmailMessage()
content = "안녕하세요"
message.set_content(content)

#Header(subject, from, to), content
message["Subject"] = "양병헌입니다."
message["From"] = EMAIL
message["To"] = "honey_sheep@naver.com"

with open("cat.jpg","rb") as img:
    img_file = img.read()
image_type = imghdr.what('cat',img_file)

#텍스트 이외의 포맷을 보내는 방법 : add_attachment    
#file, maintype, subtype 필요
message.add_attachment(img_file,maintype="image",subtype=image_type)

#1 SMTP 서버에 연결
#SSL(암호화방식)이 필요
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)

#2 SMTP 서버에 로그인 필요(아이디, 비밀번호)
smtp.login(EMAIL,"powerful1010@")

#메일 전송
sendEmail(EMAIL)

#SMTP 서버 DISCONNECT
smtp.quit()

