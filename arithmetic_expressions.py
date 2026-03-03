from abc import ABC, abstractmethod
from numbers import Number


class AExpr(ABC):
    """ This class is abstract and serves as a superclass for all Arithmetic Expressions
    """

    @abstractmethod
    def eval(self, env: dict = None) -> Number:
        """Evaluate the expression with an optional environment (dict of variable names to values)
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class Litteral(AExpr):
    """ This class represents the constant expressions. It inherits from AExpr and, unlike AExpr,
        it is a concrete class (because 'eval' is implemented).
    """
    def __init__(self, v: Number = 0) -> None:
        super().__init__()
        self._value = v

    def eval(self, env: dict = None) -> Number:
        return self._value

    def __str__(self) -> str:
        return str(self._value)


class BExpr(AExpr):
    """ This class represents the binary expressions and, by inheritance, it is abstract.
        The reason is that the 'eval' abstract method is not yet implemented.
        This class has four concrete subclasses that represent 
        addition, subtraction, multiplication and division expressions.
    """

    def __init__(self, l: AExpr = None, r: AExpr = None) -> None:
        super().__init__()
        self._left = l
        self._right = r


class AddExpr(BExpr):
    """ Now come the concrete instances of binary expressions
    """

    def eval(self, env: dict = None):
        return self._left.eval(env) + self._right.eval(env)

    def __str__(self) -> str:
        return f"({self._left} + {self._right})"


class SubExpr(BExpr):
    def eval(self, env: dict = None):
        return self._left.eval(env) - self._right.eval(env)

    def __str__(self) -> str:
        return f"({self._left} - {self._right})"


class MulExpr(BExpr):
    def eval(self, env: dict = None):
        return self._left.eval(env) * self._right.eval(env)

    def __str__(self) -> str:
        return f"({self._left} * {self._right})"


class DivExpr(BExpr):
    def eval(self, env: dict = None):
        return  self._left.eval(env) / self._right.eval(env)

    def __str__(self) -> str:
        return f"({self._left} / {self._right})"


class UExpr(AExpr):

    def __init__(self, e: AExpr = None) -> None:
        super().__init__()
        self._expr = e

class OppExpr(UExpr):

    def eval(self, env: dict = None):
        return - self._expr.eval(env)

    def __str__(self) -> str:
        return f"(-{self._expr})"


class Variable(AExpr):
    """ This class represents a variable. It looks up its value in the environment.
    """
    def __init__(self, name: str) -> None:
        super().__init__()
        self._name = name

    def eval(self, env: dict = None) -> Number:
        if env is None:
            raise ValueError(f"No environment provided for variable '{self._name}'")
        if self._name not in env:
            raise ValueError(f"Undefined variable: '{self._name}'")
        return env[self._name]

    def __str__(self) -> str:
        return self._name

class Assignment(AExpr):
    """ This class represents an assignment statement (e.g., x <- 5).
        It updates the environment and returns the assigned value.
    """
    def __init__(self, var_name: str, expr: AExpr) -> None:
        super().__init__()
        self._name = var_name
        self._expr = expr

    def eval(self, env: dict = None) -> Number:
        if env is None:
            raise ValueError("Cannot assign without an environment")
        value = self._expr.eval(env)
        env[self._name] = value
        return value

    def __str__(self) -> str:
        return f"{self._name} <- {self._expr}"




if __name__ == "__main__":
    onePlusTwo = AddExpr(Litteral(1), Litteral(2))
    print(f"Hello, World 1+2={onePlusTwo.eval()}")
    e = MulExpr(AddExpr(Litteral(1),Litteral(2)),DivExpr(Litteral(2),Litteral(2)))
    print(f"value should be 3 : {e.eval()}")
    
    obj_1 = AddExpr(Litteral(2), AddExpr(Litteral(2), Litteral(2))) #(2 + (2 + 2))
    obj_2 = AddExpr(AddExpr(Litteral(2), Litteral(2)), Litteral(2)) #((2 + 2) + 2)

    print(f"And to be sure (2 + (2 + 2)) = ((2 + 2) + 2) = {obj_1.eval()} = {obj_2.eval()}")