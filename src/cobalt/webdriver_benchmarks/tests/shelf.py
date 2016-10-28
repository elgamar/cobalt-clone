#!/usr/bin/python2
"""Simple shelf navigation test."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys

# The parent directory is a module
sys.path.insert(0, os.path.dirname(os.path.dirname(
    os.path.realpath(__file__))))

# pylint: disable=C6204,C6203
import tv
import tv_testcase
import partial_layout_benchmark

# selenium imports
keys = partial_layout_benchmark.ImportSeleniumModule("webdriver.common.keys")

DEFAULT_SHELVES_COUNT = 10
SHELF_ITEMS_COUNT = 10


class ShelfTest(tv_testcase.TvTestCase):

  def test_simple(self):
    self.load_tv()
    self.assert_displayed(tv.FOCUSED_SHELF)

    print(str(self.get_webdriver().execute_script(
        "h5vcc.system.recordStats = true")))

    for _ in xrange(DEFAULT_SHELVES_COUNT):
      self.send_keys(tv.FOCUSED_SHELF, keys.Keys.ARROW_DOWN)
      self.poll_until_found(tv.FOCUSED_SHELF)
      self.assert_displayed(tv.FOCUSED_SHELF_TITLE)
      self.wait_for_layout_complete()

    for _ in xrange(SHELF_ITEMS_COUNT):
      self.send_keys(tv.FOCUSED_TILE, keys.Keys.ARROW_RIGHT)
      self.poll_until_found(tv.FOCUSED_TILE)
      self.assert_displayed(tv.FOCUSED_SHELF_TITLE)
      self.wait_for_layout_complete()

    self.record_results("ShelfTest.test_simple")


if __name__ == "__main__":
  tv_testcase.main()
