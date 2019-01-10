NER Task 2003
===

- CoNLL 2003 shared task 데이터를 가지고 CRF로 테스트해본 결과

- 데이터 구성
```
- train 데이터는 약 219554 word
  - train.txt
- development 데이터는 약 55044 word
  - dev.txt
- test 데이터는 약 50350 word
  - test.txt
- 개체명 유형은 'PER(Person), LOC(Location), ORG(Organization), MISC(Miscellaneous)'
- 데이터 샘플
```
EU NNP B-NP B-ORG
rejects VBZ B-VP O
German JJ B-NP B-MISC
call NN I-NP O
to TO B-VP O
boycott VB I-VP O
British JJ B-NP B-MISC
lamb NN I-NP O
. . O O

Peter NNP B-NP B-PER
Blackburn NNP I-NP I-PER

BRUSSELS NNP B-NP B-LOC
1996-08-22 CD I-NP O
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

```

