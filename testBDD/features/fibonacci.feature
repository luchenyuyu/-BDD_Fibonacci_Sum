Feature: 斐波那契数列求和验证

  Scenario: 测试斐波那契数列特定数字的计算结果
    Given 假如我有数字0
    When 计算它的斐波那契值
    Then 应该看到数字0
    Given 假如我有数字1
    When 计算它的斐波那契值
    Then 应该看到数字1
    Given 假如我有数字2
    When 计算它的斐波那契值
    Then 应该看到数字1
    Given 假如我有数字3
    When 计算它的斐波那契值
    Then 应该看到数字2
    Given 假如我有数字4
    When 计算它的斐波那契值
    Then 应该看到数字3
    Given 假如我有数字5
    When 计算它的斐波那契值
    Then 应该看到数字5
