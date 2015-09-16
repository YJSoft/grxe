# 지알보드 엑스 에디션(GR Board XKY Edition) #
![http://grxe.googlecode.com/files/come_on.jpg](http://grxe.googlecode.com/files/come_on.jpg)

어서와.

**GRXE** 는 처음이지?



---



## 목차 ##
> - 1. 개발배경과 목표

> - 2. 라이센스

> - 3. 버전 릴리즈 규칙

> - 4. 버전 히스토리

> - 5.자주 발생하는 에러들에 대한 해결방안

> - 6. 설치방법 및 버그 피드백

> - 7. 개발자 정보



---



# 1. 개발배경과 목적 #
## 처음만나게 된 지알보드(GR Board) ##

2012년 초, XKY(이 버전의 개발자 혹은 수정자..)는 작은 커뮤니티를 운영해보기 위해 작은 게시판 소프트웨어를 찾고 있었다. 마침 제로보드4는 개발중지, 익스프레스엔진(XE)은 무거웠으며 그누보드(GnuBoard)는 스킨과 같은 부가적인 부분들이 폐쇄적이였다. 이것저것 맘에 안들다가 지알보드(GR Board)를 만나자 마자 뿅 가버리게 된다.

최초로 지알보드(GR Board)의 봉고버전(1.9.3 [R1](https://code.google.com/p/grxe/source/detail?r=1) Beta)을 설치하고 사용하면서 자주 php 에러와 마주쳤었다. 봉고가 베타버전이라는 점을 감안하여 충분히 이해가 되는 일이였지만 사소한 에러들에 대해 분명 피드백을 남겨야 겠다는 생각을 하게 되었다. 결국 오프라인으로 활동하다가 본격적으로 시리니넷(http://sirini.net) 에 가입하고 활동하기 시작한다.
여러가지 지알 시리즈(GR Sirise)를 설치해보고 타사 소프트웨어와 비교해보거나 장단점을 분석하는 등등..

## 트윅을 하게 된 이유 ##
생각보다 많은 불안정요소를 가지고 있었던 봉고버전(1.9.3 [R1](https://code.google.com/p/grxe/source/detail?r=1) Beta)에서, 결국 안정화 버전인 커뮤니티 에디션(1.8.6 [R4](https://code.google.com/p/grxe/source/detail?r=4))로 판내림하게 된다.
유연한 동작과 부가기능들이나 스킨들과의 안정적인 호환성들이 좋게 느껴졌으나 치명적으로 봉고버전(1.9.3 [R1](https://code.google.com/p/grxe/source/detail?r=1) Beta)에 비해 **"무겁다"**는 단점을 발견한다.
또한 시스템 보안을 목적으로 ifame과 embed태그를 사용할 수 없는 점이 불편하게 느껴졌다.
> 그래서 매번 설치할 때마다 XKY(필자)가 원하던 대로 만들어 수정해쓰곤 했었는데, 한번 쓰고 버리는 것이 너무 비효율적이라는 것을 깨달았다. 아예 "융통성 있게 트윅에서 공개하자"는 생각으로 트윅을 하게 되었다.

## 현재 엑스 에디션의 목적 ##
![http://grxe.googlecode.com/files/admin_grboard_logo.gif](http://grxe.googlecode.com/files/admin_grboard_logo.gif)
  * "안정화버전 대의 GR보드를 가볍게 즐기자!"
  * "오픈소스의 즐거움을 우리 모두가 누리자!"
  * "제로보드4를 아직도 품고 있는, 소규모 사용자들의 자리를 지알보드(GR Board)가 채워나가자!"

지알보드 엑스 에디션(GR Board XKY Edition)은 줄여서 GRXE, 발음은 엑스 에디션이라 한다.



---



# 2. 라이센스 #
지알보드(GR Board) 원본에서는 GPL에 따라 소스코드가 공개되고 있으며 수정과 편집, 배포 등이 자유롭다. 지알보드 엑스 에디션(GRXE)이 탄생할 수 있었던 것도 **"원본 소스코드가 오픈소스"였기 때문이다.^^** 그 자유로운 이념을 물려받아, 지알보드 엑스 에디션(GR Board XE)도 마찬가지로 소스코드를 공개하며 수정과 편집, 배포를 자유롭도록 허락한다.

조금 더 명확하게 지알보드 엑스 에디션(GR Board XE)은 "GPL v3"원문서의 내용에 따라 적용된다.
자세한 내용은 GPL v3 원문서를 읽기 바란다.(http://www.gnu.org/licenses/gpl-3.0.html)



---



# 3. 버전 릴리즈 개념 #
지알보드 엑스 에디션(GR Board XE)버전 릴리즈 만큼은 엄격하고 명확하게 관리한다.
기본 코드 네이밍은 "GR Board XKY Edition ''CodeName R-x(etc)'"의 패턴을 가지고 있다.


![http://grxe.googlecode.com/files/grxe_codename.gif](http://grxe.googlecode.com/files/grxe_codename.gif)

(대충 그린 그림)




지알보드 엑스 에디션(GRXE)에서 가장 기초가 되는 부분이 바로 맨 밑에 위치하는 "GR Board XKY Edition"이다. 지알보드(GR Board) 안정화 버전을 표준으로 하여금 트윅하여 사용한다.

그 위로는 "CodeName"과 "ReEdit"가 있다.

"CodeName"은 지알보드(GR Board) 안정화 버전이 새로 출시됬을 경우, 그에 맞춰 수정했을 경우 변경한다.

되도록이면 "아름다운 한글을 이용한 동물 이름"을 찾아 쓰도록 노력하고 있다. 첫 출시 버전이"맑은 고양이(Lucid Cat)"을 사용한 것도 그 때문이다. 융통적이로 "많은 부분이 수정"된 경우에 가깝다.

"ReEdit"은 "CodeName"을 근간으로 하여 수정한다.

초기 "CodeName"을 바탕으로 사소한 수정과 고침이 적용되었을 경우, R-x에서 x의 자연수를 하나씩 증가한다.

(예: [R1](https://code.google.com/p/grxe/source/detail?r=1) → [R2](https://code.google.com/p/grxe/source/detail?r=2) → [R3](https://code.google.com/p/grxe/source/detail?r=3)..)



---



# 4. 버전 히스토리 및 내려받기 #

**현재 "맑은 고양이(LucidCat) R1이 최신버전" 이다.**

### 안정화 버전 ###
| | 코드네임(codename) | 재편집 | 공개날짜 | 개발 상태 | 고친내용| 내려받기 |
|:|:---------------|:----|:-----|:------|:----|:-----|
|맑은 고양이| Lucid Cat      | [R1](https://code.google.com/p/grxe/source/detail?r=1) | 2012.11.28 | 계속 개발중.. | [GRXE 위키참조](https://code.google.com/p/grxe/wiki/history_of_lc_r1) |[ZIP파일](http://grxe.googlecode.com/files/grxe_lc_r1.zip) |


### 불안정화 버전 ###
| | 코드네임(codename) | 재편집 | 공개날짜 | 개발 상태 | 고친내용| 내려받기 |
|:|:---------------|:----|:-----|:------|:----|:-----|
| 맑은고양이 | LucidCat       | [R2](https://code.google.com/p/grxe/source/detail?r=2) | 2012.12.23 | 계속 개발중.. | [GRXE 위키참조](https://code.google.com/p/grxe/wiki/history_of_lc_r2) | [ZIP파일](http://grxe.googlecode.com/files/grxe_lc_r2.zip) |



---



# 5. 자주 발생하는 에러들에 대한 해결방안 #

준비중..



---



# 6.설치방법 및 버그 피드백 #
## 설치방법에 대해 ##
준비중이다.

## 버그 피드백에 대해 ##
전문적인 피드백 도구를 갖추지 않은 상태라, 일단 트위터로 조금씩 받아볼려고 한다.

트위터 주소는 맨 마지막 목차의 "개발자 정보"를 참조하라.



---



# 7. 개발자 정보 #
**원시코드 제공: 시리니(http://sirini.net)***

**GRXE 개발자:**

**닉네임:** XKY(D4)

**취미:** 웹서핑, 독서, 음악과 애니 감상, 프로그래밍..

**연락처:** [@\_\_xky(트위터)](https://twitter.com/__xky)