#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by KinsiGamer
# Copyright (c) 2016 Kinsi
#
# License: MIT
#

"""This module exports the Spcomp plugin class."""

from SublimeLinter.lint import Linter, util


class Spcomp(Linter):
    """Provides an interface to spcomp."""

    syntax = ('sourcepawn', 'pawn')
    cmd = 'spcomp'
    executable = None
    version_args = ''
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.0'
    regex = (
        r'^.+?\.sp\((?P<line>\d+)\) : '
        r'(?:(?P<error>error)|(?P<warning>warning)) \d+:'
        r'(?P<message>.+)'
    )
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = 'sm_temp'
    error_stream = util.STREAM_STDOUT
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = r'\s*/[/*]'

    def build_cmd(self, cmd=None):
        """Return a tuple with the command line to execute."""

        executable = self.get_view_settings().get('executable', None)
        if executable:
            args = (cmd or self.cmd)[1:]
            cmd = (executable, ) + args
            return self.insert_args(cmd)
        else:
            return super().build_cmd(cmd)