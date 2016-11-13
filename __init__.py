"""
Simple module to import Jupyter Notebook files (.ipynb) as python modules

Based mostly off https://github.com/jupyter/notebook/blob/master/docs/source/examples/Notebook/Importing%20Notebooks.ipynb,
with modifications to support more recent notebook versions.
"""
import os
import sys
import types
import requests

import nbformat
from IPython import get_ipython
from IPython.core.interactiveshell import InteractiveShell

PREFIX = 'paws.'

class NotebookLoader:
    """Module Loader for Jupyter Notebooks"""
    def __init__(self, path=None):
        self.shell = InteractiveShell.instance()
        self.path = path

    def load_module(self, fullname):
        """import a notebook as a module"""
        if not fullname.startswith(PREFIX):
            return False
        parts = fullname[len(PREFIX):].split('.')
        if len(parts) == 1:
            # This is a top-level import, give back a package
            # So if I'm importing paws.YuviPanda.something.something, we will
            # return this for the paws.YuviPanda, so python will keep soldiering on
            # FIXME: Actually read the import hooks PEP and understand wtf I am doing!
            mod = types.ModuleType(fullname)
            mod.__file__ = fullname
            mod.__loader__ = self
            mod.__path__ = fullname
            sys.modules[fullname] = mod
            return mod
        
        url_segment = '/'.join([s.replace('_', ' ') for s in parts]) + '.ipynb?format=raw'
        url = 'https://paws-public.wmflabs.org/paws-public/User:' + url_segment
        resp = requests.get(url)
        if resp.status_code != 200:
            raise ImportError('No module {name} found - {code} response for {url}'.format(
                name=fullname,
                url=url,
                code=resp.status_code
            ))
        data = resp.text

        # load the notebook object
        nb = nbformat.reads(data, as_version=4)

        # create the module and add it to sys.modules
        # if name in sys.modules:
        #    return sys.modules[name]
        mod = types.ModuleType(fullname)
        mod.__file__ = fullname
        mod.__loader__ = self
        mod.__dict__['get_ipython'] = get_ipython
        sys.modules[fullname] = mod

        # extra work to ensure that magics that would affect the user_ns
        # actually affect the notebook module's ns
        save_user_ns = self.shell.user_ns
        self.shell.user_ns = mod.__dict__

        try:
            for cell in nb.cells:
                if cell.cell_type == 'code':
                    # transform the input to executable Python
                    code = self.shell.input_transformer_manager.transform_cell(cell.source)
                    # run the code in themodule
                    exec(code, mod.__dict__)
        finally:
            self.shell.user_ns = save_user_ns
        return mod


class NotebookFinder:
    """Module finder that locates Jupyter Notebooks"""
    def __init__(self):
        self.loaders = {}

    def find_module(self, fullname, path=None):
        if fullname.startswith(PREFIX):
            return NotebookLoader(path)
        

sys.meta_path.append(NotebookFinder())
