import pytest
import pandas as pd

## example test. Can be run in terminal using pytest and the filepath. Requires 'test' in front of the function.
# def sum_xy(x, y):
#     sum = x + y
#     return sum

# def test_sum_xy():
#     test_output = sum_xy(x=1, y=2)
#     assert test_output == 3

def df_slicer(df, age):
    over_age = df[df['Age'] >= age]
    return over_age

def test_df_slicer():
    test_df = pd.DataFrame(
        [
            {"ChildId": "child1", "Age": 6},
            {"ChildId": "child3", "Age": 10},
            {"ChildId": "child2", "Age": 4},
            {"ChildId": "child4", "Age": 1},
        ]
    )

    test_over_5 = df_slicer(test_df, 5)
    test_over_7 = df_slicer(test_df, 7)
    test_df_minus5 = df_slicer(test_df, -5)

    expect_df_over_5 