# Unittests and Integration Tests

![img](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/1/f088970b450e82c881ea.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20231019%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20231019T090716Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5d430d7084faefdc0ac1fe2752f0008707beab58caa1932e90fbe765ae0a6338)

Unit testing is the process of testing that a particular function returns expected results for different set of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mocked, especially if they make network or database calls.

The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?

Integration tests aim to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.

Integration tests will test interactions between every part of your code.

Execute your tests with

```
$ python -m unittest path/to/test_file.py
```

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, `without the help of Google`:

- The difference between unit and integration tests.
- Common testing patterns such as mocking, parametrizations and fixtures
