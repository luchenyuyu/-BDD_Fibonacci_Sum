from behave import given, when, then


def fibonacci(n):
    if n < 0:
        raise ValueError("输入的数字不能为负数")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


@given('假如我有数字{number}')
def step_given_number(context, number):
    try:
        context.number = int(number)
    except ValueError:
        context.number = number


@when('计算它的斐波那契值')
def step_when_calculate_fibonacci(context):
    try:
        if isinstance(context.number, int):
            context.fibonacci_result = fibonacci(context.number)
        else:
            raise TypeError("输入的不是合法数字类型，无法计算斐波那契值")
    except Exception as e:
        context.exception = e


@then('应该看到数字{expected_result}')
def step_then_verify_result(context, expected_result):
    expected_result = int(expected_result)
    assert context.fibonacci_result == expected_result


@then('应该抛出异常')
def step_then_verify_exception(context):
    assert isinstance(context.exception, (ValueError, TypeError))