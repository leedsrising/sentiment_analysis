from monkeylearn import MonkeyLearn

API_KEY = "092c9806157cb60f124b38a6433dce235433e701"

ml = MonkeyLearn(API_KEY)
data = []
model_id = "cl_pi3C7JiL"
result = ml.classifiers.classify(model_id, data)
print(result.body)