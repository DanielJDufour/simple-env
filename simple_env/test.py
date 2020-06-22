from unittest import TestCase
from subprocess import check_output

class HasTestCase(TestCase):
    def test_checking_null(self):
        statement = '''GREETING='null' python3 -c "import __init__ as se; print(se.has('GREETING') == True, end='')"'''
        output = check_output(statement, cwd="simple_env", shell=True, text=True)
        self.assertEqual(output, 'True')

class GetTestCase(TestCase):
    def test_getting_string(self):
        statement = '''GREETING='hello' python3 -c "import __init__ as se; print(se.get('GREETING'), end='')"'''
        output = check_output(statement, cwd="simple_env", shell=True, text=True)
        self.assertEqual(output, "hello")

    def test_getting_number(self):
        statement = '''PORT='1234' python3 -c "import __init__ as se; print(se.get('PORT') == 1234, end='')"'''
        output = check_output(statement, cwd="simple_env", shell=True, text=True)
        self.assertEqual(output, "True")

    def test_getting_zero(self):
        statement = '''DEBUG_LEVEL='0' python3 -c "import __init__ as se; print(se.get('DEBUG_LEVEL') == 0, end='')"'''
        output = check_output(statement, cwd="simple_env", shell=True, text=True)
        self.assertEqual(output, "True")

    def test_getting_none(self):
        statement = '''GREETING='null' python3 -c "import __init__ as se; print(se.get('GREETING') == None, end='')"'''
        output = check_output(statement, cwd="simple_env", shell=True, text=True)
        self.assertTrue(output)

    def test_getting_warning(self):
        statement = '''python3 -c "import __init__ as se; print(se.get('GREETING') == None, end='')"'''
        output = check_output(statement, cwd="simple_env", shell=True, text=True)
        self.assertEqual(output, "[simple-env] could not find GREETING.\nTrue")

    def test_suppressing_warning(self):
        statement = '''python3 -c "import __init__ as se; print(se.get('GREETING', ignore_warnings=True) == None, end='')"'''
        output = check_output(statement, cwd="simple_env", shell=True, text=True)
        self.assertEqual(output, "True")

    def test_suggestions(self):
        statement = '''EMAIL_USE_TLS=true python3 -c "import __init__ as se; se.get('USE_TLS')"'''
        output = check_output(statement, cwd="simple_env", shell=True, text=True)
        self.assertEqual(
            output, "[simple-env] could not find USE_TLS. Did you mean EMAIL_USE_TLS?\n"
        )

    def test_suggestions_again(self):
        statement = '''USE_TLS=true python3 -c "import __init__ as se; se.get('EMAIL_USE_TLS')"'''
        output = check_output(statement, cwd="simple_env", shell=True, text=True)
        self.assertEqual(
            output, "[simple-env] could not find EMAIL_USE_TLS. Did you mean USE_TLS?\n"
        )

    def test_string_trimming(self):
        statement = '''BROWSER="'Chrome'" python3 -c "import __init__ as se; print(se.get('BROWSER') == 'Chrome', end='')"'''
        output = check_output(statement, cwd="simple_env", shell=True, text=True)
        self.assertEqual(output, "True")
