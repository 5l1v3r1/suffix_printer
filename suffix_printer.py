#!/usr/bin/env python3

from sys import stdout,stderr

DEF = DEFAULT = '[+]'
NOT = NOTICE  = '[-]'
WAR = WARNING = '[!]'
ERR = ERROR   = '[ERROR]' 

def suffix(s,suf=DEFAULT):
    '''
    Suffix and return a string.
    '''

    return f"{suf} {s}"

def suffix_print(s,suf=DEFAULT,file=stdout,end="\n"):
    '''
    Suffix and print a string to stdout.
    '''

    print(suffix(s,suf), file=file, end=end)

def clean_suffix_print(end="",*args,**kwargs):
    '''
    Suffix and print a message without a newline.
    '''

    suffix_print(end=end,*args,**kwargs)

def suffix_print_stderror(*args, **kwargs):
    '''
    Suffix and print a message to stderr.
    '''

    suffix_print(file=stderr,*args,**kwargs)

sprint = suffix_print
csprint = clean_suffix_print
esprint = suffix_print_stderror
