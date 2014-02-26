from setuptools import setup

setup(name='python-paymentslip',
      version='0.1.0',
      description='Function for generating ESR-numbers for orange swiss payment slips (so called \"Oranger Einzahlungsschein\").',
      url='http://github.com/philippeowagner/python-payment-slip',
      author='Philippe O. Wagner',
      author_email='wagner@arteria.ch',
      license='BSD',
      packages=['payment_slip'],
      zip_safe=False)