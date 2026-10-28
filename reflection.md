&#x09;# Lab 5: Static Code Analysis — Reflection



\## 1. How did Pylint, Bandit, and Flake8 help improve the code?



Pylint helped identify code quality issues such as missing docstrings, inconsistent naming conventions, and overly long lines. Bandit detected security problems, including a hardcoded password, unsafe use of `eval()`, and SQL query construction using string formatting. Flake8 identified formatting issues and violations of Python style guidelines. After fixing the issues, the Pylint score improved from 2.41/10 to 10.00/10, Bandit reported no remaining issues, and Flake8 produced no errors.



\## 2. What security issues were identified, and how were they fixed?



Bandit identified three security findings in the original program. First, a hardcoded password was present in the source code. Second, SQL queries were constructed using string formatting, which could introduce an SQL injection vulnerability. Third, the program used `eval()`, which can execute arbitrary Python expressions. These issues were addressed by removing the hardcoded password, using parameterized SQL queries, and replacing `eval()` with a safer approach.



\## 3. What was the most challenging part of this lab?



The most challenging part was understanding the warnings produced by the three static analysis tools and deciding how to fix them without changing the program's intended behaviour. Security findings required particular attention because simply changing the code's appearance would not eliminate the underlying risk. Running the tools again after making changes helped verify that the reported issues had been addressed.



\## 4. Why is static code analysis important in software development?



Static code analysis helps identify potential bugs, security vulnerabilities, and coding style problems before software is deployed. It improves code readability, maintainability, and security. Using multiple tools is useful because each tool focuses on different aspects of code quality. This lab demonstrated that static analysis can help developers produce cleaner and safer code while making issues easier to identify and correct.



