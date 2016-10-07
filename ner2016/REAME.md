ner 2016
===

- 2016 국어정보처리 경진대회(개체명인식)에서 배포한 학습 및 개발 데이터를 가지고 간단하게 CRF로 테스트해본 결과
- 실행
```
$ ./crf.sh -v -v
```
- 결과
```
# 타깃 클래스는 'O'가 아닌 것으로 가정한 경우
number_of_sent = 501
number_of_success = 16440
number_of_success_pos = 1824
number_of_success_neg = 14616
number_of_failure = 953
number_of_failure_pos = 732
number_of_failure_neg = 221
precision(positive) = 0.713615
precision(negative) = 0.985105
accuracy  = 0.849360
```
