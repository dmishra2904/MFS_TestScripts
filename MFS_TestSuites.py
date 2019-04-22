import unittest
import AddCustomerfromcsv, login, AddProduct, AddServices, DeleteCustomer, DeleteProducts, DeleteServices, \
    EditCustomer, EditProduct, EditServices, ReadCustomerSummary, logout

import logging

logging.basicConfig(
    filename="devanshika_test_scripts.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(message)s"
)


class ConfigTestCase(unittest.TestCase):

    def setUp(self):
        print('set up')

    def runTest(self):
        print('run test')


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.loader.findTestCases(login))
    test_suite.addTest(unittest.loader.findTestCases(AddCustomerfromcsv))
    test_suite.addTest(unittest.loader.findTestCases(EditCustomer))
    test_suite.addTest(unittest.loader.findTestCases(DeleteCustomer))
    test_suite.addTest(unittest.loader.findTestCases(AddServices))
    test_suite.addTest(unittest.loader.findTestCases(EditServices))
    test_suite.addTest(unittest.loader.findTestCases(DeleteServices))
    test_suite.addTest(unittest.loader.findTestCases(AddProduct))
    test_suite.addTest(unittest.loader.findTestCases(EditProduct))
    test_suite.addTest(unittest.loader.findTestCases(DeleteProducts))
    test_suite.addTest(unittest.loader.findTestCases(ReadCustomerSummary))
    test_suite.addTest(unittest.loader.findTestCases(logout))

    return test_suite


mySuit = suite()

log_file = 'log_file.txt'
f = open(log_file, "w")
runner = unittest.TextTestRunner(f)
runner.run(mySuit)
f.close()