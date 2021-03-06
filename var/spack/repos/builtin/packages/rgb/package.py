# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Rgb(AutotoolsPackage):
    """X color name database.

    This package includes both the list mapping X color names to RGB values
    (rgb.txt) and, if configured to use a database for color lookup, the
    rgb program to convert the text file into the binary database format.

    The "others" subdirectory contains some alternate color databases."""

    homepage = "http://cgit.freedesktop.org/xorg/app/rgb"
    url      = "https://www.x.org/archive/individual/app/rgb-1.0.6.tar.gz"

    version('1.0.6', '9759d058108f39066bbdf1d5d6de048c')

    depends_on('xorg-server')

    depends_on('xproto', type='build')
