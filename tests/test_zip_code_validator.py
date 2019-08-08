from django.core.exceptions import ValidationError
from django.test import TestCase
from gothamzip.forms import zip_validator


class ZipCodeValidatorTest(TestCase):
    def test_no_repetition_1(self):
        self.assertIsNone(zip_validator('523563'))

    def test_no_repetition_2(self):
        self.assertIsNone(zip_validator('112233'))

    def test_less_than_100000(self):
        self.assertRaises(ValidationError, zip_validator, '12345')

    def test_more_than_999999(self):
        self.assertRaises(ValidationError, zip_validator, '1234567')

    def test_1_repeated(self):
        self.assertRaises(ValidationError, zip_validator, '121426')

    def test_2_5_repeated(self):
        self.assertRaises(ValidationError, zip_validator, '552523')
