NER Task 2016
===

- 2016 국어정보처리 경진대회(개체명인식)에서 배포한 학습 및 개발 데이터를 가지고 CRF로 테스트해본 결과
  - gazette 사전은 사용하지 않았다. 
- 데이터 구성
```
- train 데이터는 3549문장(63865어절)
  - train.txt
- development 데이터는 500문장(9101어절)
  - dev.txt
- gazette 사전은 3755 단어
  - gazette
- 개체명 유형은 'DT(date) LC(location) OG(organization) PS(person) TI(time)'
- 데이터 샘플(by json2base.py)
1 데이비드 NNP B_PS
2 베컴 NNP I
2 ( SS O
2 33 SN O
3 · SP O
4 LA SL B_OG
4 갤럭시 NNP I
4 ) SS O
4 이 JKS O
5 8 SN B_DT
5 일 NNB I
5 ( SS O
5 한국 NNP B_LC
5 시간 NNG O
5 ) SS O
6 미국 NNP B_LC
6 프로 NNG O
6 축구 NNG O
6 ( SS O
6 MLS SL B_OG
6 ) SS O
7 출입 NNG O
8 기자단 NNG O
8 이 JKS O
9 뽑 VV O
9 은 ETM O
10 금주 NNG B_DT
10 의 JKG O
11 선수 NNG O
11 로 JKB O
12 선정 NNG O
12 되 XSV O
12 었 EP O
12 다 EC O
```
- 학습데이터를 Wapiti 입력 데이터 포맷에 맞게 변환
```
데이비드	NNP	B_PS
베컴	NNP	I
(	SS	O
33	SN	O
·	SP	O
LA	SL	B_OG
갤럭시	NNP	I
)	SS	O
이	JKS	O
8	SN	B_DT
일	NNB	I
(	SS	O
한국	NNP	B_LC
시간	NNG	O
)	SS	O
미국	NNP	B_LC
프로	NNG	O
축구	NNG	O
(	SS	O
MLS	SL	B_OG
)	SS	O
출입	NNG	O
기자단	NNG	O
이	JKS	O
뽑	VV	O
은	ETM	O
금주	NNG	B_DT
의	JKG	O
선수	NNG	O
로	JKB	O
선정	NNG	O
되	XSV	O
었	EP	O
다	EC	O
.	SF	O
```
- CRF feature 템플릿
```
U:wrd-1 LL=%X[-2,0]
U:tag-1 LL=%X[-2,1]

U:wrd-1 L=%X[-1,0]
U:tag-1 L=%X[-1,1]

*:wrd-1 X=%X[0,0]
*:tag-1 X=%X[0,1]

U:wrd-1 R=%X[1,0]
U:tag-1 R=%X[1,1]

U:wrd-1 RR=%X[2,0]
U:tag-1 RR=%X[2,1]

U:tag-2 XR=%X[0,1]/%X[1,1]

*:Pre-1 X=%m[ 0,0,"^.?"]
*:Pre-2 X=%m[ 0,0,"^.?.?"]
*:Pre-3 X=%m[ 0,0,"^.?.?.?"]
*:Pre-4 X=%m[ 0,0,"^.?.?.?.?"]

*:Suf-1 X=%m[ 0,0,".?$"]
*:Suf-2 X=%m[ 0,0,".?.?$"]
*:Suf-3 X=%m[ 0,0,".?.?.?$"]
*:Suf-4 X=%m[ 0,0,".?.?.?.?$"]

*:Caps? L=%t[-1,0,"\u"]
*:Caps? X=%t[ 0,0,"\u"]
*:Caps? R=%t[ 1,0,"\u"]

*:Punc? L=%t[-1,0,"\p"]
*:Punc? X=%t[ 0,0,"\p"]
*:Punc? R=%t[ 1,0,"\p"]

*:Numb? L=%t[-1,0,"\d"]
*:Numb? X=%t[ 0,0,"\d"]
*:Numb? R=%t[ 1,0,"\d"]
```
- 학습 및 평가
```
$ ./crf.sh -v -v
```
- 결과
```
processed 17393 tokens with 2190 phrases; found: 1999 phrases; correct: 1603.
accuracy:  95.25%; precision:  80.19%; recall:  73.20%; FB1:  76.53
                 : precision:  79.59%; recall:  71.38%; FB1:  75.26  539
                 : precision:  79.59%; recall:  71.38%; FB1:  75.26  539
               DT: precision:  95.62%; recall:  89.87%; FB1:  92.66  297
               LC: precision:  68.95%; recall:  80.25%; FB1:  74.17  277
               OG: precision:  68.14%; recall:  59.71%; FB1:  63.65  361
               PS: precision:  86.30%; recall:  72.63%; FB1:  78.88  489
               TI: precision:  86.11%; recall:  73.81%; FB1:  79.49  36
```

- 참고
  - 2016 국어 정보 처리 시스템 - 지정 분야: 개체명 인식 시스템 개발 및 적용( https://github.com/krikit/annie )
