# Copyright (C) 2020 Francisco Munoz, Aldo Romero, Sobhit Singh, Uthpala Herath, Pedram Tavadze, Eric Bousquet, Xu He, Reese Boucher, Logan Lang, Freddy Farah
#
# This file is part of PyProcar.
#
# PyProcar is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyProcar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pyprocar.  If not, see <http://www.gnu.org/licenses/>.

from .version import version as __version__
from .version import author as __author__
from .version import copyright as __copyright__
from .version import email as __email__
from .version import status as __status__
from .version import date as __date__


import logging
import re
import sys

import ase
import matplotlib.pyplot as plt
import numpy as np
import seekpath
import skimage
# import pychemia
import pyvista
import trimesh

# Frmsf
from .frmsfparser import FrmsfParser

# Bxsf
from .bxsfparser import BxsfParser

# Abinit
from .abinitparser import AbinitParser

# Elk
from .elkparser import ElkParser

# Quantum Espresso
from .qeparser import QEParser, QEDOSParser, QEFermiParser

# Lobster
from .lobsterparser import LobsterParser, LobsterDOSParser, LobsterFermiParser

from pyprocar.fermisurface import FermiSurface
from pyprocar.fermisurface3d import FermiSurface3D, BrillouinZone

# from . import fermisurface3d
from .procarfilefilter import ProcarFileFilter
from .procarparser import ProcarParser
from .procarplot import ProcarPlot
from .procarselect import ProcarSelect
from .procarsymmetry import ProcarSymmetry
from .utilsprocar import UtilsProcar
from . import doscarplot
from . import vaspxml
from . import core

from .scriptBandsDosplot import bandsdosplot
from .scriptBandsplot import bandsplot
from .scriptCat import cat
from .scriptDosplot import dosplot
from .scriptFermi2D import fermi2D
from .scriptFermi3D import fermi3D

# from .scriptSpin_asymmetry import spin_asymmetry
from .scriptFilter import filter
from .scriptKmesh2D import generate2dkmesh
from .scriptKpath import kpath
from .scriptRepair import repair
from .scriptUnfold import unfold
from .scriptVector import Vector
# from .scriptBandGap import bandgap
from .splash import welcome

from . import io