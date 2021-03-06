# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class RUuid(RPackage):
    """Tools for generating and handling of UUIDs (Universally Unique
    Identifiers)."""

    homepage = "http://www.rforge.net/uuid"
    url      = "https://cran.rstudio.com/src/contrib/uuid_0.1-2.tar.gz"

    version('0.1-2', 'f97d000c0b16bca455fb5bf2cd668ddf')
