# -*- coding: utf-8 -*-

from pylt.base import ModuleTest
from pylt.requests import CurlRequest, TEST_TXT


class TestRewrite1(CurlRequest):
    URL = "/somefile"
    EXPECT_RESPONSE_BODY = TEST_TXT
    EXPECT_RESPONSE_CODE = 200
    EXPECT_RESPONSE_HEADERS = [("Content-Type", "text/plain; charset=utf-8")]
    config = """
rewrite "^/somefile$" => "/test.txt";
defaultaction;
"""


class TestRewrite2(CurlRequest):
    URL = "/somefile"
    EXPECT_RESPONSE_BODY = TEST_TXT
    EXPECT_RESPONSE_CODE = 200
    EXPECT_RESPONSE_HEADERS = [("Content-Type", "text/plain; charset=utf-8")]
    config = """
rewrite "/somethingelse" => "/nothing", "^/somefile$" => "/test.txt";
defaultaction;
"""


class Test(ModuleTest):
    plain_config = """
setup { module_load "mod_rewrite"; }
"""
