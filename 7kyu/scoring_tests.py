def score_test(tests, right, omit, wrong):
    good_a = tests.count(0)
    omit_a = tests.count(1)
    wrong_a = tests.count(2)
    result = (good_a * right) + (omit_a * omit) - (wrong_a * wrong)
    return result


print(score_test([0, 0, 0, 0, 2, 1, 0], 2, 0, 1))
