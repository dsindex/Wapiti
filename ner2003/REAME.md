NER Task 2003
===

- CoNLL 2003 shared task 데이터를 가지고 CRF로 테스트해본 결과

- 데이터 구성
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
processed 46666 tokens with 5648 phrases; found: 5568 phrases; correct: 4646.
accuracy:  96.37%; precision:  83.44%; recall:  82.26%; FB1:  82.85
              LOC: precision:  86.57%; recall:  86.21%; FB1:  86.39  1661
             MISC: precision:  79.43%; recall:  74.79%; FB1:  77.04  661
              ORG: precision:  81.52%; recall:  74.35%; FB1:  77.77  1515
              PER: precision:  83.65%; recall:  89.55%; FB1:  86.50  1731

```

- 참고
  - [final results of 2003 shared task for NER](https://www.clips.uantwerpen.be/conll2003/ner/)

