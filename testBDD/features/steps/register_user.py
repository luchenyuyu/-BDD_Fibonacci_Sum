
from behave import given, when, then
import math


def fibonacci(n):
    n = int(n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

@given('假如我有数字{n:d}')
def step_given_have_number(context, n):
    context.number = n


@when('计算它的斐波那契值')
def step_when_compute_fibonacci(context):
    context.fibonacci_result = fibonacci(context.number)


@then('应该看到数字{r:d}')
def step_then_see_result(context, r):
    assert context.fibonacci_result == r