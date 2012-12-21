#!/usr/bin/python

# Copyright (C) 2012 Reece H. Dunn
#
# This file is part of ucd-tools.
#
# ucd-tools is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ucd-tools is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ucd-tools.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys
import ucd

ucd_rootdir  = sys.argv[1]
unicode_data = ucd.parse_ucd_data(ucd_rootdir, 'UnicodeData')

if __name__ == '__main__':
	sys.stdout.write("""/* Unicode General Categories
 *
 * Copyright (C) 2012 Reece H. Dunn
 *
 * This file is part of ucd-tools.
 *
 * ucd-tools is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * ucd-tools is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with ucd-tools.  If not, see <http://www.gnu.org/licenses/>.
 */

// NOTE: This file is automatically generated from the UnicodeData.txt file in
// the Unicode Character database by the ucd-tools/tools/categories.py script.

#include "ucd/ucd.h"

using namespace ucd;
""")

	sys.stdout.write('\n')
	sys.stdout.write('ucd::category ucd::lookup_category(codepoint_t c)\n')
	sys.stdout.write('{\n')
	sys.stdout.write('\treturn Cn;\n')
	sys.stdout.write('}\n')
