import android # 안드로이드
import time # 경과시간 기반
import os # 리눅스 기반 안드로이드

d = android.Android() # 안드로이드 객체 생성

tok_count = 0 # 연속 카운트 공간..
delay = d.dialogGetInput("PyMr", "♩= x 에서 x의 값을 양수형태로 입력하세요.")
sys_dir = "/mnt/sdcard/" # 안드로이드 아이크스림 샌드위치(4.0.3)의 시스템 디렉토리
sys_n_dir = os.getcwd() # 파이엠알 어플리케이션 실행 경로(만약을 위해..)

try: # 값예외 판단
	delay = int(delay.result) # 받은 유니코드를 정수형으로 변환
except ValueError:
	d.makeToast("값을 잘못입력하셨습니다.")
	# 종료.

	
# 에러 없이 진행 시..
delay = delay / 60
d.makeToast("PyMr - 동작을 시작합니다.")

while True: # 무한 반복.
	d.MediaPlay(sys_n_dir + "/tok.wav")
	tok_count = tok_count + 1 # 전치 연산 대신에 안전하게 코딩..
	d.makeToast("%d번 반복됨..", %tok_count) # 카운트를 정수형으로 출력
	time.sleep(delay) # 딜레이 값으로 슬립