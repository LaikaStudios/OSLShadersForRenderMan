#
#   Copyright 2022 Laika, LLC.
# 
#   Licensed under the Apache License Version 2.0 http://apache.org/licenses/LICENSE-2.0,
#   or the MIT license http://opensource.org/licenses/MIT, at your option.
# 
#   This program may not be copied, modified, or distributed except according to those terms.
#
'''
"Flatten" the relative shader pathname into a unique base file name
and optionally copy it to the destination location. No timestamp or
other make-like funtionality exists: just write the flattened shader
to the destination.
'''
import argparse
import os
import sys
import shutil
from collections import OrderedDict


class ShaderInfo(object):
    '''
    Creates a ShaderInfo object containing:
        pathname = The (source) path name of the compiled shader.
        flatname = The flattened name of the compiled shader file.
    '''
    def __init__( self, pathname, flatname ):
        self.pathname = pathname
        self.flatname = flatname


def _flatten( pathname ):
    '''
    Replace directory path separators with '_':
        data/FooBar.oso -> data_FooBar.oso
    '''
    return str(pathname).replace( os.sep, '_' )


def _flatten_osl_shader( pathname ):
    '''
    Create a ShaderInfo object containing the osl shader pathname
    and flattened name.
    '''
    flatname = _flatten( pathname )
    return ShaderInfo( pathname, flatname )


def _install_file( shader_info, destination, copy ):
    '''
    Move or copy the compiled shader 
    to the destination directory using its flattened file names.
    '''
    dstfile = os.path.join( destination, shader_info.flatname )
    if copy:
        shutil.copyfile( shader_info.pathname, dstfile )
    else:
        shutil.move( shader_info.pathname, dstfile )


def install_shaders( shaders, destination, copy ):
    '''
    shaders: The set of compiled shaders that contain their relative directory path.
    destination: The directory that will contain the flattened shader files.
    '''
    shader_dict = OrderedDict()
    success = True

    for shader in shaders:
        if shader.endswith( ".oso" ):
            shader_info = _flatten_osl_shader( shader )
        else:
            print( "ERROR: {} is not a .oso shader.".format( shader ))
            continue

        flatname = shader_info.flatname

        if flatname in shader_dict:
            print( "ERROR: {}'s flattened name collides with {}'s flattened name: {}"
                .format( shader, shader_dict[flatname], flatname ))
            success = False
            continue

        shader_dict[ flatname ] = shader

        _install_file( shader_info, destination, copy )

    return success


def _main():
    parser = argparse.ArgumentParser( description = "Installs shaders." )
    parser.add_argument( "destination", help = "Destination directory" )
    parser.add_argument( "shaders", nargs = "+", help = "Compiled shaders." )
    parser.add_argument( "--copy", default = False, action = 'store_true', help = "Copy the compiled shader to the destination instead of moving it." )

    args = parser.parse_args()

    success = install_shaders( args.shaders, args.destination, args.copy )

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(_main())
