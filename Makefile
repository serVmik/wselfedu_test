lint:
	poetry run flake8

pytest:
	pytest

check: lint pytest

pw-debug:
	PWDEBUG=1 pytest