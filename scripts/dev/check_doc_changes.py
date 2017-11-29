#!/usr/bin/env python3
# vim: ft=python fileencoding=utf-8 sts=4 sw=4 et:

# Copyright 2016-2017 Florian Bruhin (The Compiler) <mail@qutebrowser.org>

# This file is part of qutebrowser.
#
# qutebrowser is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# qutebrowser is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with qutebrowser.  If not, see <http://www.gnu.org/licenses/>.

"""Check if docs changed and output an error if so."""

import sys
import subprocess
import os

code = subprocess.run(['git', '--no-pager', 'diff',
                       '--exit-code', '--stat']).returncode

if os.environ.get('TRAVIS_PULL_REQUEST', 'false') != 'false':
    if code != 0:
        print("Docs changed but ignoring change as we're building a PR")
    sys.exit(0)

if code != 0:
    print()
    print('The autogenerated docs changed, please run this to update them:')
    print('   tox -e docs')
    print('   git commit -am "Update docs"')
    print()
    print('(Or you have uncommitted changes, in which case you can ignore '
          'this.)')
    if 'TRAVIS' in os.environ:
        print()
        print("travis_fold:start:gitdiff")
        subprocess.run(['git', '--no-pager', 'diff'])
        print("travis_fold:end:gitdiff")
sys.exit(code)