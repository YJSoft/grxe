# _*_ coding: UTF-8 _*_
import android
import os
import time
droid = android.Android() # Android 객체생성

py_dir = os.getcwd() # 스크립트 디렉토리 입력
tok_count = 0 # 반복횟수 카운터 초기화
respones = 0 #단추의 Indent를 담기 위한 변수.

tok_time = droid.getInput('파이메트로놈 - 간격 입력', '"초당 울릴 소리를 입력하세요.\n문자는 입력하지 마세요..")')
droid.makeToast(tok_time + "초 가견을 입력하셨습니다.")

while True:
	droid.mediaPlay(py_dir+'/tok.wav') # 같은 경로의 tok.wav 재생
	toc_count = toc_count +1 # 카운터 증가
	print (tok_count+'번 울림') # 콘솔 상태 시에 알려줌..
	respones = droid.GetResponse() # 단추의 Indent가 발생할 경우, respones로 얻어온다.
	time.sleep(tok_time)

if respones == PostiveButtun["which"]:
	droid.makeToast("종료했습니다..")
	os.exit() # 스크립트 시스템 종료