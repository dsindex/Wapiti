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
- 학습데이터 샘플
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
  - [crf.pattern](https://github.com/dsindex/Wapiti/blob/master/ner2016/crf.pattern)
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
