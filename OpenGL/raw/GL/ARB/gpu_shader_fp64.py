'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_ARB_gpu_shader_fp64'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_ARB_gpu_shader_fp64',error_checker=_errors._error_checker)
GL_DOUBLE=_C('GL_DOUBLE',0x140A)
GL_DOUBLE_MAT2=_C('GL_DOUBLE_MAT2',0x8F46)
GL_DOUBLE_MAT2x3=_C('GL_DOUBLE_MAT2x3',0x8F49)
GL_DOUBLE_MAT2x4=_C('GL_DOUBLE_MAT2x4',0x8F4A)
GL_DOUBLE_MAT3=_C('GL_DOUBLE_MAT3',0x8F47)
GL_DOUBLE_MAT3x2=_C('GL_DOUBLE_MAT3x2',0x8F4B)
GL_DOUBLE_MAT3x4=_C('GL_DOUBLE_MAT3x4',0x8F4C)
GL_DOUBLE_MAT4=_C('GL_DOUBLE_MAT4',0x8F48)
GL_DOUBLE_MAT4x2=_C('GL_DOUBLE_MAT4x2',0x8F4D)
GL_DOUBLE_MAT4x3=_C('GL_DOUBLE_MAT4x3',0x8F4E)
GL_DOUBLE_VEC2=_C('GL_DOUBLE_VEC2',0x8FFC)
GL_DOUBLE_VEC3=_C('GL_DOUBLE_VEC3',0x8FFD)
GL_DOUBLE_VEC4=_C('GL_DOUBLE_VEC4',0x8FFE)
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,arrays.GLdoubleArray)
def glGetUniformdv(program,location,params):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLdouble)
def glUniform1d(location,x):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLdoubleArray)
def glUniform1dv(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLdouble,_cs.GLdouble)
def glUniform2d(location,x,y):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLdoubleArray)
def glUniform2dv(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glUniform3d(location,x,y,z):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLdoubleArray)
def glUniform3dv(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glUniform4d(location,x,y,z,w):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLdoubleArray)
def glUniform4dv(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLdoubleArray)
def glUniformMatrix2dv(location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLdoubleArray)
def glUniformMatrix2x3dv(location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLdoubleArray)
def glUniformMatrix2x4dv(location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLdoubleArray)
def glUniformMatrix3dv(location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLdoubleArray)
def glUniformMatrix3x2dv(location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLdoubleArray)
def glUniformMatrix3x4dv(location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLdoubleArray)
def glUniformMatrix4dv(location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLdoubleArray)
def glUniformMatrix4x2dv(location,count,transpose,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,_cs.GLboolean,arrays.GLdoubleArray)
def glUniformMatrix4x3dv(location,count,transpose,value):pass
