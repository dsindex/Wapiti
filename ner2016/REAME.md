NER Task 2016
===

- 2016 국어정보처리 경진대회(개체명인식)에서 배포한 학습 및 개발 데이터를 가지고 CRF로 테스트해본 결과
  - gazette 사전은 사용하지 않았다. 
- 데이터 구성
```
- train 데이터는 3549문장(63865어절)
- development 데이터는 500문장(9101어절)
- gazette 사전은 3755 단어
- 개체명 유형은 'DT(date) LC(location) OG(organization) PS(person) TI(time)'
- 데이터 샘플
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

U:wrd-1 X=%X[0,0]
U:tag-1 X=%X[0,1]

U:wrd-1 R=%X[1,0]
U:tag-1 R=%X[1,1]

U:wrd-1 RR=%X[2,0]
U:tag-1 RR=%X[2,1]
```
- 학습 및 평가
```
$ ./crf.sh -v -v
```
- 결과
```
# 타깃 클래스는 'O'가 아닌 것으로 가정한 경우
number_of_sent = 501
number_of_success = 16440
number_of_failure = 953
number_of_success_pos_rc = 1824
number_of_failure_pos_rc = 732
number_of_success_neg_rc = 14616
number_of_failure_neg_rc = 221
number_of_success_pos_pc = 1824
number_of_success_neg_pc = 14616
number_of_failure_pos_pc = 489
number_of_failure_neg_pc = 464
recall(positive) = 0.713615
recall(negative) = 0.985105
precision(positive) = 0.788586
precision(negative) = 0.969231
accuracy  = 0.878909
fmeasure(positive) = 0.749230
```
