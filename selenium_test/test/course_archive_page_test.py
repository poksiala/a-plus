import unittest

from test_initializer import TestInitializer
from page_objects import CourseArchivePage
from locators import CourseArchiveLocators


class CourseArchivePageTest(unittest.TestCase):
    def setUp(self):
        self.driver = TestInitializer().getFirefoxDriverWithLoggingEnabled()

    def testShouldOpenCourseArchivePage(self):
        courseArchivePage = CourseArchivePage(self.driver)
        self.assertTrue(courseArchivePage.isElementVisible(CourseArchiveLocators.APLUS_LINK))
        self.assertTrue(courseArchivePage.isElementVisible(CourseArchiveLocators.HOOK_LINK))

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)