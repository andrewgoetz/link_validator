import unittest
from link_validator import check_validity


class UrlValidityTests(unittest.TestCase):

    def test_url_has_no_scheme(self):
        urls = ['www.google.com']
        result = [['www.google.com', 'Missing or invalid URL protocol.']]
        self.assertEqual(result, check_validity(urls))

    def test_url_has_no_hostname(self):
        urls = ['http://']
        result = [['http://', 'Missing or invalid URL hostname.']]
        self.assertEqual(result, check_validity(urls))

    def test_url_returns_404(self):
        urls = ['http://httpstat.us/404']
        self.assertEqual(len(urls), len(check_validity(urls)))

    def test_url_returns_200(self):
        urls = ['http://httpstat.us/200']
        self.assertNotEqual(len(urls), len(check_validity(urls)))

    def test_url_that_causes_redirect(self):
        urls = ['https://www.myemma.com']
        self.assertNotEqual(len(urls), len(check_validity(urls)))

    def test_url_with_normal_formatting(self):
        urls = ['https://www.google.com']
        self.assertNotEqual(len(urls), len(check_validity(urls)))

    def test_url_that_is_poorly_formated(self):
        urls = ['htadff://askhfahjshf']
        self.assertEqual(len(urls), len(check_validity(urls)))

    def test_multiple_bad_urls(self):
        urls = ['htadff://askhfahjshf', 'www.yahoo.com', '132wewew',
                'httl://.com', 'fhasf:/shjfhsf.com']
        self.assertEqual(len(urls), len(check_validity(urls)))

    def test_multiple_good_urls(self):
        urls = ['http://www.yahoo.com', 'http://www.google.com',
                'https://aws.amazon.com/']
        self.assertNotEqual(len(urls), len(check_validity(urls)))


if __name__ == '__main__':
    unittest.main()
