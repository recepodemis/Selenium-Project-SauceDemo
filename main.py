from Test_Sauce import Test_SauceDemo



testClass = Test_SauceDemo()

testResult = testClass.test_username_and_password_required()
print(f"username and password are blank result: {testResult}")

testResult = testClass.test_password_required()
print(f"Only password is blank result: {testResult}")

testResult = testClass.test_invalid_login()
print(f"locked_out_user error result: {testResult}")

testResult = testClass.succesfully_login()
print(f"There are 6 item result: {testResult}")
