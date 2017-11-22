# Sentiment Analyzer

## 선행연구(단어강도점수)
-가설에 사용될 요소들을 보다 원활하게 판단하기 위하여 사용할 단어 마다 신뢰도를 바탕으로 강도 점수를 측정함.

[긍정단어](https://github.com/hyunjunbrucelee/2017sejongAI/blob/master/Homework1/Codes/%EB%8B%A8%EC%96%B4%EB%B3%84%20%EA%B0%95%EB%8F%84%20%EC%A0%90%EC%88%98%20%EA%B8%8D%EC%A0%95.py)

[부정단어](https://github.com/hyunjunbrucelee/2017sejongAI/blob/master/Homework1/Codes/%EB%8B%A8%EC%96%B4%EB%B3%84%20%EA%B0%95%EB%8F%84%20%EC%A0%90%EC%88%98%20%EB%B6%80%EC%A0%95.py)

제시된 코드를 이용하여 긍,부정 각 10개의 단어를 실험 해본 결과는 아래와 같다.

* 긍정: great(60), special(54), best(58), classic(63), master piece(66), awesome(69), unique(69), perfect(71),  marvelous(81),   smooth(79)

* 부정: outrageous(56), trash(61),  irritating(65), rude(71), terrible(75), stupid(80), worst(81),  awful(85), unacceptable(90), insulting(93)

----------------------------------------------------------

## 가설1: 단어의 수, 어순이 평가에 영향을 미칠 것이다.
**-검증방법:** 긍정의 키워드로만 구성된 문장의 길이를 달리하여 실험, 어순을 달리하여 실험.

[Used code](https://github.com/hyunjunbrucelee/2017sejongAI/blob/master/Homework1/Codes/%EA%B0%80%EC%84%A41.%EC%96%B4%EC%88%9C%2C%20%EB%8B%A8%EC%96%B4%EC%88%98.py)

>**Out put**

Review | Status
------------ | -------------
great great great great | positive (0.6)
great | Positive (0.6)
perfect perfect perfect perfect perfect | Positive (0.71)
perfect  | Positive (0.71)
bad bad bad bad bad bad  | Negative (0.66)
bad | Negative (0.66)
good perfect | Positive (0.71)
perfect good | Positive (0.71)

>결론

**-단어의 순서 혹은 개수와 평가는 관계가 없다.**

------------------------------------------------------------------
## 가설2: 다양한(반어적, 은유적 등) 표현을 이해할 것이다.
**-검증방법:** 다양한 표현을 이용하여 검증


[Used code](https://github.com/hyunjunbrucelee/2017sejongAI/blob/master/Homework1/Codes/%EA%B0%80%EC%84%A42.%EB%8B%A4%EC%96%91%ED%95%9C%20%ED%91%9C%ED%98%84.py)

>**Out put**

**Review**: it was so good, that i want to shit on directors face
*(Positive: 0.6)*

**Review**: i wish im the only one who can enjoy this movie, dont watch it.
*(Negative: 0.94)*

**Review**: its unacceptable!, how can human make such thing!
*(Positive: 0.62)*

**Review**: it was so painful when the ending credit showed up
*(Negative: 0.7)*

**Review**: this is crazy, the best movie ever
*(Positive: 0.6)*

>결론

**-5개중 2개 만을 성공적으로 분석하였다. 정확할 때도 있으나 대부분 틀린 결과를 기대할 수 있다.**

-----------------------------------------------------

## 가설3: 상반되는 두 개의 단어를 같이 사용할 시 신뢰도가 더 높은 단어 쪽으로 평가될 것이다.
**-검증방법:** 강도 점수를 측정한 단어들을 이용하여 검증


[Used code](https://github.com/hyunjunbrucelee/2017sejongAI/blob/master/Homework1/Codes/%EA%B0%80%EC%84%A43.%EC%83%81%EB%B0%98%EB%90%98%EB%8A%94%EB%8B%A8%EC%96%B4.py)

>**Out put**

Review | Status | Prediction 
------------ | ------------- | -------------
insulting, perfect | positive (0.71) | Negative
smooth, rude | Positive (0.71) | Positive
best, trash | Negative (0.61) | Negative
stupid, masterpiece  | Positive (0.74) | Negative
outrageous, awesome  | Positive (0.69) | Positive
marvelous, irritating | Negative (0.65) | Positive
perfect, rude | Positive (0.71) | Neutral

>결론

**-단어의 신뢰도 와 긍, 부정의 평가는 상관관계가 없다.**

------------------------------------------------------------

## 가설4: 단어를 추가하여 강조 시에 이를 알아 차릴 것이다.
**-검증방법:** 강도 점수를 측정한 단어들 앞에 강조의 의미를 지닌 단어를 추가하여 분석하고 그에 따른 신뢰도로 판단.

[Used code](https://github.com/hyunjunbrucelee/2017sejongAI/blob/master/Homework1/Codes/%EA%B0%80%EC%84%A44.%20%EA%B0%95%EC%A1%B0%20%EB%8B%A8%EC%96%B4%20%EC%B6%94%EA%B0%80.py)

>**Out put**


Review | Status | Origin 
------------ | ------------- | -------------
so great | Positive (0.59) | 0.60
so unique | Positive (0.68) | 0.69
so special | Positive (0.53) | 0.54
the best  | Positive (0.58) | 0.58
the master piece  | Positive (0.66) | 0.66
so stupid | Negative (0.81) | 0.8
so rude | Negative (0.7) | 0.71
so terrible | Negative (0.76) | 0.75
too awful | Negative (0.85) | 0.85
the worst | Negative (0.81) | 0.81

>결론

**-변화가 없거나 0.01점의 변화가 있다. 따라서 단어의 강조는 유 의미하나 주요 요인이 아니다.**

---------------------------------------------------

## 가설5: 영화의 장르를 이용하여 해당장르에 해당하는 단어로 평가된 것을 잡아낼 수 있다.
**-검증방법:** 액션은 액션, 공포는 공포 등 장르에 맞는 단어를 이용하여 검증한다.

[Used code](https://github.com/hyunjunbrucelee/2017sejongAI/blob/master/Homework1/Codes/%EA%B0%80%EC%84%A45.%EC%98%81%ED%99%94%20%EC%9E%A5%EB%A5%B4.py)

>**Out put**


**Review**: in terms of horror movie, it was horrifying.
*(Positive: 0.66)*

**Review**: in terms of romance movie, it was romantic.
*(Positive: 0.67)*

**Review**: As its fantasy movie, it was fantastic.
*(Positive: 0.64)*

**Review**: As its a thriller, i was thrilled.As its genre is mystery, it was mysterious.
*(Positive: 0.54)*

>결론

**-영화의 장르를 언급 시 그에 따라 판단을 내릴 수 있는 것으로 보인다.**
