import operator

from . import jsonrpc

@jsonrpc.method("logic.and")
def logic_and(A: bool, B: bool):
    """
    Логическое И
    """
    return operator.and_(A, B)

@jsonrpc.method("logic.not")
def logic_not(A: bool):
    """
    Логическое НЕ
    """
    return operator.not_(A)

@jsonrpc.method("logic.or")
def logic_or(A: bool, B: bool):
    """
    Логическое ИЛИ
    """
    return operator.or_(A, B)

@jsonrpc.method("logic.xor")
def logic_xor(A: bool, B: bool):
    """
    Логическое ИСКЛЮЧАЮЩЕЕ ИЛИ
    """
    return operator.xor(A, B)