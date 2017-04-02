# Copyright 2016 Autodesk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from .displays import nbmolviz_installed


class NotebookNotInstalledMixin(object):
    def _raise_error(self, *args, **kwargs):
        raise ImportError("The `nbmolviz` package is not installed; this function is not availble.")

    draw = draw2d = draw3d = configure_methods = configure = _raise_error


if nbmolviz_installed():
    from nbmolviz.mixins import (AtomNotebookMixin,
                                 AtomGroupNotebookMixin,
                                 TrajNotebookMixin,
                                 MolNotebookMixin,
                                 ResidueNotebookMixin,
                                 MethodConfigurationMixin)
else:
    AtomNotebookMixin = NotebookNotInstalledMixin
    AtomGroupNotebookMixin = NotebookNotInstalledMixin
    TrajNotebookMixin = NotebookNotInstalledMixin
    MolNotebookMixin = NotebookNotInstalledMixin
    ResidueNotebookMixin = NotebookNotInstalledMixin
    MethodConfigurationMixin = NotebookNotInstalledMixin

