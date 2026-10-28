\# Lab 5: Static Code Analysis — Issue Documentation



| Issue                           | Type         | Line(s)   | Description                                              | Fix Approach                                    |

| ------------------------------- | ------------ | --------- | -------------------------------------------------------- | ----------------------------------------------- |

| Hardcoded password              | Security     | 5         | Password stored directly in source code.                 | Removed the hardcoded password.                 |

| SQL injection risk              | Security     | 11        | SQL query constructed using string formatting.           | Used parameterized SQL queries.                 |

| Unsafe eval()                   | Security     | 21        | eval() can execute arbitrary Python expressions.         | Replaced eval() with a safer approach.          |

| Missing docstrings              | Code quality | Multiple  | Module and functions lacked descriptions.                | Added appropriate docstrings.                   |

| Naming conventions              | Code quality | Multiple  | Function names did not follow snake\_case.                | Renamed functions to follow Python conventions. |

| Long lines                      | Style        | 4, 11, 27 | Lines exceeded the configured length limit.              | Reformatted long statements.                    |

| Multiple statements on one line | Style        | 27        | Conditional and return statements shared one line.       | Moved the return statement to a separate line.  |

| Broad exception handling        | Code quality | 22        | Generic exception handling could hide unexpected errors. | Narrowed exception handling.                    |



\## Summary



Pylint, Bandit, and Flake8 were used to identify code quality, security, and formatting issues. The code was updated, and the tools were run again to verify the changes.



