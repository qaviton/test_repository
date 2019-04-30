Qaviton-Repo: functional web
============================

this project is intended to provide an open source repository 
of automated functional web tests to help testers 
with repeating and similar scenarios to test and maintain 
a generic collection of tests intended to be copied 
into other testing projects or to be used for examples to these projects.  


Installing
----------

make sure you have python 3.7+ installed.
Install and update using `pip`_:

```
    pip install functional_web_tests -U
    python -m qaviton create tests
```  

A Simple Example
----------------

```
    
    tests/test_health_check.py
    --------------------
       
    from functional_web_tests.tests.services.app import App
    from functional_web_tests.tests.execute_tests.login.test_health_check import test_health_check as health_check
    
    def test_health_check(app):
        app = App(driver=app.driver, platform=app.platform)
        health_check(app)
        
```
```

    python -m pytest tests/test_health_check.py
```  

Contributing
------------

For guidance on setting up a development environment and how to make a
contribution to Qaviton, see the `contributing guidelines`_.

.. _contributing guidelines: https://github.com/qaviton/test_repository/blob/master/CONTRIBUTING.rst


Links
-----

* Open Source Framework: https://github.com/qaviton/qaviton
* Website: https://www.qaviton.com
* Documentation: https://github.com/qaviton/qaviton/blob/master/docs/
* License: `Apache License 2.0 <https://github.com/qaviton/qaviton/blob/master/LICENSE>`_
* Code: https://github.com/qaviton/test_repository/
* Issue tracker: https://github.com/qaviton/test_repository/issues
