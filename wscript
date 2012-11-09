# -*- python -*-
# @purpose the main entry point for driving the build and installation steps
# @author Sebastien Binet <binet@cern.ch>

# imports ---------------------------------------------------------------------
import os

# globals ---------------------------------------------------------------------
top = '.'
out = '__build__'
PREFIX = 'install_area'
VERSION = '0.0.1' # FIXME: should take it from somewhere else
APPNAME = os.path.basename(os.getcwd())

# imports ---------------------------------------------------------------------

# waf imports --
import waflib.Logs
import waflib.Utils
import waflib.Options
import waflib.Context
import waflib.Logs as msg

# functions -------------------------------------------------------------------

def go(ctx):
    from waflib.Options import commands, options
    from os import getcwd
    from os.path import join as pjoin
    options.prefix = pjoin(getcwd(), "install")
    commands += ["configure", "clean", "build", "install"]

def options(ctx):
    ctx.load('find_heplibs', tooldir='hep-waftools')
    return

def configure(ctx):
    ctx.load('find_heplibs', tooldir='hep-waftools')

    ctx.find_cernroot(
        #atleast_version="5.34/02",
        #atleast_version="6.0.0",
        version=(6,0,0),
        )

    ctx.find_clhep()
    ctx.find_boost()
    
    ctx.recurse('pkg/rootcomps')
    return

def build(ctx):
    ctx.recurse('pkg/rootcomps')
    return

def check(ctx):
    return

def regen(ctx):
    import subprocess
    subprocess.Popen(["./waffle/kit/create-kit.py"]).wait()
    return
