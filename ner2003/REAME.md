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
  - [crf.pattern](https://github.com/dsindex/Wapiti/blob/master/ner2003/crf.pattern)
- 학습 및 평가
```
$ ./crf.sh -v -v
```
- 결과
```
processed 46666 tokens with 5648 phrases; found: 5596 phrases; correct: 4599.
accuracy:  96.16%; precision:  82.18%; recall:  81.43%; FB1:  81.80
              LOC: precision:  86.66%; recall:  85.67%; FB1:  86.16  1649
             MISC: precision:  78.35%; recall:  74.22%; FB1:  76.23  665
              ORG: precision:  76.88%; recall:  73.09%; FB1:  74.94  1579
              PER: precision:  84.26%; recall:  88.74%; FB1:  86.45  1703

```

