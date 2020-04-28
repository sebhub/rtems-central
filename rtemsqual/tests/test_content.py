# SPDX-License-Identifier: BSD-2-Clause
""" Unit tests for the rtemsqual.content module. """

# Copyright (C) 2020 embedded brains GmbH (http://www.embedded-brains.de)
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import os

from rtemsqual.content import Content


def test_append():
    content = Content("BSD-2-Clause")
    content.append("")
    assert str(content) == """
"""
    content.append(["a", "b"])
    assert str(content) == """
a
b
"""
    with content.indent():
        content.append(["c", "d"])
        assert str(content) == """
a
b
  c
  d
"""


def test_prepend():
    content = Content("BSD-2-Clause")
    content.prepend("")
    assert str(content) == """
"""
    content.prepend(["a", "b"])
    assert str(content) == """a
b

"""
    with content.indent():
        content.prepend(["c", "d"])
        assert str(content) == """  c
  d
a
b

"""


def test_add():
    content = Content("BSD-2-Clause")
    content.add("")
    assert str(content) == ""
    content.add("a")
    assert str(content) == """a
"""
    content.add(["b", "c"])
    assert str(content) == """a

b
c
"""


def test_add_blank_line():
    content = Content("BSD-2-Clause")
    content.add_blank_line()
    assert str(content) == """
"""


def test_indent():
    content = Content("BSD-2-Clause")
    content.add_blank_line()
    content.append("x")
    content.indent_lines(3)
    assert str(content) == """
      x
"""


def test_write(tmpdir):
    content = Content("BSD-2-Clause")
    content.append("x")
    path = os.path.join(tmpdir, "x", "y")
    content.write(path)
    with open(path, "r") as src:
        assert src.read() == """x
"""
    tmpdir.chdir()
    path = "z"
    content.write(path)
    with open(path, "r") as src:
        assert src.read() == """x
"""
