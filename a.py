#
#!/usr/bin/env python3.3
#!/usr/bin/env python2.7
#!/usr/bin/python3.3
#!/usr/bin/python2.7
#
# Yufei <yufeixiaoyu@gmail.com>
#
'''This modules is for something.

description
'''

author = 'Yufei'
email = 'yufeixiaoyu@gmail.com'
coding_style ='''\
    4-space indentation, no tabs.
    Wrap lines, don't exceed 79 characters.
    Blank lines separate functions, classes, larger blocks inside functions.
    When possible, comments on a line of their own.
    Use docstrings.
    Use spaces around operators and after commas, but not directly inside
        bracketing constructs: a = f(1, 2) + g(3, 4)
    CamelCase for classes and lower_case_with_underscores for
        functions and methods. Use self as the first method argument.
    UTF-8 even plain ASCII encoding.
    Don't use non-ASCII characters in identifiers.
    '''

# Startup file in script.
import os
filename = os.environ.get('PYTHONSTARTUP')
if filename and os.path.isfile(filename):
    exec(open(filename).read())

##############################################################################
def f(x, *args, **kwargs):
    '''Object's purpose.

    Describling the object's calling conventions, side effects, etc.
    '''
    pass

# f.__doc__
# f.__annotations__
# Defina a function
# range(*args)) func(**dict)
# lambda x: x
#lambda a, b: a+b
# Call a function
#f(x)
#
# list comprehensions: squares = [x**2 for x in range(10)]
# [(x, y) for x in [1,2,3] for y in [4,5,6] if x != y]
# from A import B
#
#builtin
# del
# int() print() list() dict() len() map() zip() round() sorted() reversed()
# dir() does not list the names of built-in functions and variables, need import builtins; dir(builtins) # it seemd different with __builtins__
# vars() return a dict containing all local variables.
#
#str
#    immutable
#    multiline strings 1, \ 2, '''''' 3, r''
#    unicode \u0020 (unicode ordinal value)
#
#bytes b'\xxxx'
#
#list
#    a[:n] + a[n:] = a
#    a[:] do not change in loop, make copy with this
#    a[:] = []
#    list comprehension x=[expression for xxx for xxx for xxx if xxx if andsoon]
#    x is list and if expression is tuple, it must be parenthesized with ()
#    expression can be another list comprehension (nested)
#        matrix = [ [1,2,3,4],[5,6,7,8],[9,10,11,12] ]
#        [[row[i] for row in matrix] for i in range(4)]
#
#tuple
#    immutable, but can contain mutable objects
#    tuple = aaa,aaa,aaa,
#    empty_tuple = ()
#    single_value_tuple = 'hello',   # ('hello',)
#    tuple packing and sequence unpacking: (eg. multiple assignment)
#        t = 1,2,'hello'         x, y, z = t      a,b,c=1,2,3 ?
#
#set
#    set() for empty set, not {}, which is a empty dict
#    set() or {x,y,z} for set
#    set comprehension: a ={x for x in 'abcdef' if x not in 'egsa'}
#    & | ^
#
#dict
#    keys: immutable,str,number,or tuples with only immutable element.
#    {} for empty dict
#    dict() build dict directly from sequences of key-value pairs
#        dict([(1,10),(2,10),(3,10)]) => {1: 10, 2: 10, 3: 10}
#    dict comprehension: {x: x**2 for x in (1,2,3)}
#    when key is simple string, it's sometimes easier to specify pairs using keyword arguments:
#    dict(a=1,b=2,c=3)
#
#
#
#
#
#loop for,while 
#    for k, v in dict.items():
#        print(k, v)
#    for i, v in enumerate( a_sequence):
#        print(i, v)   # index and sequence element
#    questions =[q1,q1,q3]; answers = [a1,a2,a3] #zip for more sequences
#    for q, a in zip(questions, answers):
#        print('wha's the {0}? it is {1}.'.format(q,a))
#    MAKEING A COPY first if change a sequence while inside the loop list[:]
#
#conditions on while and if
#    in, not in, is, is not, (and or not)
#    short-circuit operators(and or) return the last evaluated argument when used as a general value not as a boolean.
#    assignment cannot occur inside expressions
#
#
#
#
#iterators
#
#    iterator iterate over iterable
#    eg. for               eg. range() list,tuple,dict,str,file
#
#    Behind the scenes, the for statement calls iter() on the container object. The function returns an iterator object that defines the method __next__() which accesses elements in the container one at a time. When there are no more elements, __next__() raises a StopIteration exception which tells the for loop to terminate. You can call the __next__() method using the next() built-in function.
#
#    it is easy to add iterator behavior to your classes. Define an __iter__() method which returns an object with a __next__() method. If the class defines __next__(), then __iter__() can just return self:
#
#generators
#
#    Generators are a simple and powerful tool for creating iterators. They are written like regular functions but use the yield statement whenever they want to return data. Each time next() is called on it, the generator resumes where it left-off (it remembers all the data values and which statement was last executed).
#    Anything that can be done with generators can also be done with class based iterators like above. What makes generators so compact is that the __iter__() and __next__() methods are created automatically. Another key feature is that the local variables and execution state are automatically saved between calls. This made the function easier to write and much more clear than an approach using instance variables like self.index and self.data.
#    In addition to automatic method creation and saving program state, when generators terminate, they automatically raise StopIteration. In combination, these features make it easy to create iterators with no more effort than writing a regular function.
#
#    Generator Expressions: Some simple generators can be coded succinctly as expressions using a syntax similar to list comprehensions but with parentheses instead of brackets.
#    These expressions are designed for situations where the generator is used right away by an enclosing function. Generator expressions are more compact but less versatile than full generator definitions and tend to be more memory friendly than equivalent list comprehensions.
#
#
#
#
#
#
#range() len() enumerate() collections.deque for queues implentation
#
#function
#    local symbol -> enclosing function symbol -> global symbol table -> builtin names
#    only see but not change/assign (unless use global keyword)
#    return None
#    caller -> callee (call by object reference)
#
#    default argument values (when define), different when immutable or muutable
#    keyword arguments       (when calling or define)
#    arbitrary argument lists(when define)
#
#    def f(formal_parameter_list, *positional_arguments, **keyword_arguments):
#        '''The function description'''
#        pass
#        *positional_arguments receive tuple
#        **keyword_arguments receive dict
#    unpacking argument lists with *list or *tuple and **dict
#
#    all mutable data structures in python does not return object, they return None, which means methods chaining is not avaliable.

#module
#    import module_name
#    import module.submodule.subsubmodule
#    from module_name.submodule_name import something,other
#    from module_name import * #import all names except beginning with an underscore(_) eg. _.* # avoid this
#    module statements are executed only the first time the module is imported somewhere
#    module's private symbo table used as global symbol table by all the functions defined in the module
#    import can be anywhere, the imported module names are placed in the imorting modules' global symbol table
#    each module is only imported once per interpreter session. if change module, must restart interpreter or use:
#        import imp; imp.reload(module_name)
#    if __name__ == '__main__':   # as script or module, for provide a convenient user interface to a module or for testing purposes(running the module as a script executes a test suite)
#    when import module_name, interpreter_starton=>built-in=>module_name.py in sys.path  #sys.path is initialized from the input script direcoty(or current directory), PYTHONPATH, installation-dependent default
#    .pyc file record the modification time of .py file. .pyc file platform independent.
#    python -O, generate .pyo file from .py file, ignore .pyc file
#    python -OO, avoid now.
#    .pyc .pyo just improve the loading speed, not running speed than .py file
#    because script running on command line doesnt write .pyc .pyo file. recommend write a small bootstrap script and import the module which include the code to reduce the startup time
#    .pyc .pyo can be used independent on anywhere without .py file
#    compileall can create .pyc .pyo files for a directory
#
#packages
#    __init__.py empty or initialize the package or set __all__ variable
#    from package import item, the import will try the the item defined in pakcage(eg. function,class,variable), if fail, then try the module_name, if fail, ImportError.
#    import item.subitem.subsubitem, each item except the last one must be a package, the last item must be a module or package but not class,function,variable.
#    __all__ list is the solution for package author provideing the explicit index to fix import * problems.
#    WHEN from package import *, when __all__ list defined in __init__.py, use this, if no __all__ found in __init__.py, it just ensure package has been imported (and possibly running any initialization code in __init__.py) and whatever names are defined in the package(include names or explicitly loaded module in __init__.py, and previous imporoted submodule by previous import statements in this package) but not all submodules,  # BAD, avoid
#    from package import specific_submodule    # recommended
#    absolute import, relative import with 'from module import name' form
#        from . import module # current
#        from .. import module # parent
#        from ..module_name import module # parent_then_child
#    relative import based on the current module name, since the main module name is always '__main__', modules intended for use as the main module of applicaion must always use absolute import.
#    __path__, initialized to be a list containing the directory name holding the __init__.py before the code executing.
#
#
#
#class
#    class are created at runtime, and can be modified further after creation. as is true for module.
#    objects can have many name (in multiple scopes) bounded to it, it's like alias or pointer and in python, there seems only arguments passing by pointer.
#    a namespace is a mapping from names to objects. strictly speaking, references to names in modules are attribute references, in this case there happens to be a straightforward mapping between the module's attributes and the global names defined in the module: they share the same namespace, except for one thing: module objects have a secret read-only atribute called __dict__, which returnes the dictionary used to implement the modules' namespaces, it's an attribute but not a global name. should be restricted to things like post-mortem debuggers.
#
#    Namespaces are created at different moments and have different lifetimes. The namespace containing the built-in names is created when the Python interpreter starts up, and is never deleted. The global namespace for a module is created when the module definition is read in; normally, module namespaces also last until the interpreter quits. The statements executed by the top-level invocation of the interpreter, either read from a script file or interactively, are considered part of a module called __main__, so they have their own global namespace. (The built-in names actually also live in a module; this is called builtins.) The local namespace for a function is created when the function is called, and deleted when the function returns or raises an exception that is not handled within the function. (Actually, forgetting would be a better way to describe what actually happens.) Of course, recursive invocations each have their own local namespace.
#
#    A scope is a textual region of a Python program where a namespace is directly accessible. "Directly accessible" here means that an unqualified reference to a name attempts to find the name in the namespace.
#
#    Although scopes are determined statically, they are used dynamically. At any time during execution, there are at least three nested scopes whose namespaces are directly accessible:
#        the innermost scope, which is searched first, contains the local names
#        the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contains non-local, but also non-global names
#        the next-to-last scope contains the current module’s global names
#        the outermost scope (searched last) is the namespace containing built-in names
#
#    nonlocal variable will be read-only to inner scope since the assignment will create a new local avairble in inner scope. which should mean that: outer variable is read-only to inner scope. global will go to global directly.
#
#    nonlocal global
#    if no global statement is in effect – assignments to names always go into the innermost scope. Assignments do not copy data—they just bind names to objects. The same is true for deletions: the statement del x removes the binding of x from the namespace referenced by the local scope. In fact, all operations that introduce new names use the local scope: in particular, import statements and function definitions bind the module or function name in the local scope.
#    The global statement can be used to indicate that particular variables live in the global scope and should be rebound there; the nonlocal statement indicates that particular variables live in an enclosing scope and should be rebound there.
#
#    Class Objects support two kinds of operations: attribute references and instantiation, the instantiation create an empty object, therefore a class can define a special method __init__() to custimize to a specific initial state. arguments given to the class instantiation operator are passed to __init__()
#
#    Instance Objects only support attribute references. there are two kinds of valid attribute names: data attributes and methods. data attribute need NOT be declared, all attributes of a class that are function objects define corresponding methods of its instances.
#    ClassName.function is not x.function (x=ClassName())
#    function_object           method_object
#
#    the special thing about methods is that the object is passed as the first argument of the function. In our example, the call x.f() is exactly equivalent to MyClass.f(x). In general, calling a method with a list of n arguments is equivalent to calling the corresponding function with an argument list that is created by inserting the method’s object before the first argument.
#
#    data attributes override method attributes with the same name.
#
#    Methods may reference global names in the same way as ordinary functions. The global scope associated with a method is the module containing its definition. (A class is never used as a global scope.) While one rarely encounters a good reason for using global data in a method, there are many legitimate uses of the global scope: for one thing, functions and modules imported into the global scope can be used by methods, as well as functions and classes defined in it. Usually, the class containing the method is itself defined in this global scope, and in the next section we’ll find some good reasons why a method would want to reference its own class.
#
#    Each value is an object, and therefore has a class (also called its type). It is stored as object.__class__.
#
#    Derived classes may override methods of their base classes. A simple way to call the base class method directly: just call BaseClassName.methodname(self, arguments). This only works if the base class is accessible as BaseClassName in the global scope.
#
#    For multiple inheritance, a simple understanding, the search for attributes inherited from a parent class as depth-first, left-to-right, not searching twice in the same class where there is an overlap in the hierarchy.
#    In fact, it is slightly more complex, the method resolution order changes dynamically to support cooperative calls to super()
#    mro: method resolution order, (dynamic ordering)
#
#    all classes inherit from object
#
#    2 built-in functions work with inheritance:
#        isinstance(obj, type), True if obj.__class__ is type or some class derived from type
#        issubclass(dev_type, base_type), True if dev_type is a subclass of base_type
#
#    Notice that code passed to exec() or eval() does not consider the classname of the invoking class to be the current class; this is similar to the effect of the global statement, the effect of which is likewise restricted to code that is byte-compiled together. The same restriction applies to getattr(), setattr() and delattr(), as well as when referencing __dict__ directly.
#
#    simulate the C struct, an empty class definition:
#        class Employee:
#            pass
#        john = Emplyee()
#        john.name = 'John Doe'
#
#    A piece of Python code that expects a particular abstract data type can often be passed a class that emulates the methods of that data type instead.
#
#    Instance method objects attributes:
#        m.__self__ is the instance object with the method m().
#        m.__func__ is the function object corresponding to the method.
#
#
#
#
#
#
#
#
#
#
#
#
#
#    class ClassName:
# or class ClassName(BaseClass1, BaseClass2,...):
# or class ClassName(modname.BaseClassName1, ...):
#
#        def __init__(self, args):
#            self.data = []
#        def f(self, args):
#            pass
#        pass
#    x = ClassName() or x = ClassName(args)
#    x.f()
#
#    private variables convention:
#        _something (function, method, data member)
#    class private members, name mangling(to avoid name clash with names defined by subclass)
#        __something[_]
#        will be replaced by _classname__something[_]
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#    __str__()
#
#
#
#
#
#error and exception
#    errors detected during execution are called exceptions
#
#    try clause -> no exception occurs -> finish
#               -> exception occurs -> have related except clause -> continue
#                                   -> no related except clause -> pass on to outer try statements. -> if no, it's an unhandled exception
#    
#    if an exception occurs which does not match the exception named in the except clause, it is passed on to outer try statements. if no handler is found, it is an unhandled exception and execution stops with a error message.
#
#    the last except clause may omit exception name(s) to serve as a wildcard, extreme caution,it is easy to mask a real programming error! it can also be used to print an error message and then re-raise the exception(allowing a caller to handle the exception as well):
#
#    unhandled exceptions will be re-raised after the finally clause has een executed, the finally clause is also executed "on the way out" when any other clause of the try statement is left via a break, continue or return statement.
#    in real world applications, the finally clause is useful for releasing external resources, such as files or network connections, regardless of whether the use of the resource was successfull
#
#
#    Exception classes are usually kept simple, often only offering a number of attributes that allow information about the error to be extracted by handlers for the exception. When creating a module that can raise several distinct errors, a common practice is to create a base class for exceptions defined by that module, and subclass that to create specific exception classes for different error conditions:
#    class Error(Exception):
#        '''Base class for exceptions in this module.'''
#        pass
#    class AbcError(Error):
#        '''Exception raised for errors in the Abc.
#
#        Attributes:
#            value1 -- descriptions
#            value2 -- descriptions
#        '''
#        def __init__(self, value1, value2):
#            self.value1 = value1
#            self.value2 = value2
#
#
#    raise Class (a shorthand of raise Class() )
# or raise Instance
# or raise Class()
#
#    except clause will catch the derived subclass and baseclass excepton. so, list the derived bottommost sub-exception first in the except clause.
#
#    When an error message is printed for an unhandled exception, the exception’s class name is printed, then a colon and a space, and finally the instance converted to a string using the built-in function str().
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#    try:
#        raise Exception('spam', 'eggs')
#    except Exception as e:
#        e is the instance of class Exception, and e.args is ('spam', 'eggs'), we can print(e) directly since e has a __str__() function defined.
#
#    try:
#        pass
#    except Exception or except Exception as e: or except (Except1,Except2,Except3):
#        pass
#    except:  # see comments above, last except can omit expept name
#        pass
#    else:    # must be executed if try clause doesn't raise an exception
#        pass
#    finally: # must be executed under all circumstances, it's clean-up actions
#        pass
#
#    raise or raise ExceptionName('args')
#        ExceptionName must be a exception instance or an exception class which derives from Exception
#
#        re-raise the exception if just wonder whether an exception was raised but dont't intend to handle it.
#        try:
#            raise NameError('hi')
#        except NameError:
#            print('an ecepiton')
#            raise
#
#    class MyError(Exception):
#        def __init__(self, value):
#            self.value = value
#        def __str__(self):
#            return repr(self.value)
#
#    BaseException -> Exception -> user defined exception
#                  -> SystemExit
#                  -> KeyboardInterrupt
#                  -> GeneratorExit
#
#    with, used with object like file, which has predefined clean-up actions, ensure object cleaned up promptly and correctly. like the try/finally clause
#        with open(file) as f: pass
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#input and output, file
#    wrting values: expression statement, print(), file_object.write()
#    control output format: string hanlding by ownself, or str.format(), string module's Template class also do some substitute job.
#    convert (any) values to strings: repr() or str()
#        For most object types, eval(repr(object)) == object.
#    str(): return human-readable value representations
#    repr(): generate representation read by interpreter or SyntaxError if can not convert
#    strings, have two distinct representations, repr() of a string adds string quotes and backslashes
#    str. ljust/rjust/center/zfill
#    str.format()
#        print('{} or {0} or {key}'.format('str1',...), empty or positional and keyword arguments can be used and combined.
#        {!a} {!s} {!r} apply ascii(),str(),repr() they convert the value before it's formatted.
#        an optional ':' and format specifier can follow the field name, e.g. print('{0:.3f})'.format(math.pi)) print('{0:10} {1:10d}'.format(a_str,a_num)) int after : cause the field a minimum char wide.
#        '{0[key]:d}'.format(dict) or '{key:d}'.format(**dict)  This is particularly useful in combination with the built-in function vars(), which returns a dictionary containing all local variables
#    old string formatting
#        print('%5.3f' % math.pi)
#
#file
#    f=open(filename,mode) r(default)|w|a|r+ (the file is encoded in a specific encoding, default is utf-8)  rb|wb|ab|rb+ (for binary mode, bytes object)
#    text mode: when read, convert platform-specific line endings \n(unix) \r\n(windows) to \n, when write, convert \n to platform-specific line endings in background
#    for efficient reading large file, use f.readlines([sizehint]) or for line in file: looping
#    f.write() need convert to str if it is not string
#    f.tell() return bytes number from the beginning, f.seek(offset, from_what) 0 for head, 1 for current, 2 for end of the file, text file only can seek from head (0) and with one exception seek(0,2)
#    f.close() or
#        with open(filename, mode) as f:
#            pass
#    with close the file properly after its suite finishes, even exception raised.
#
#    pickle.dump(object, file) object = pickle.load(file), convert almost any python object to a string representation
#
#
#
#dir()
#help()
#os: os.path
#shutil: for daily file and directory management tasks
#glob: for file wildcards
#sys: sys.argv for command line arguments
#     sys.stdin
#     sys.stdout
#     sys.stderr (sys.stderr.write('error'))
#     sys.exit()
#getopt:
#argparse:
#re: when simple, prefere to use string methods like str.replace()
#math:
#random:
#urllib:
#smtplib:
#datetime: timezone aware
#zlib:
#gzip:
#bz2:
#lzma:
#zipfile:
#tarfile:
#timeit: performance measurement
#profile:
#pstats:
#doctest: test
#unittest:
#xmlrpc: server and client
#email:
#poplib:
#xml: dom and sax
#csv:
#gettext: i18n
#locale:
#codecs:
#
#reprlib: repr() output formatting
#pprint:
#textwrap:
#locale:
#
#string: Template class, ${python_identifiers}, $$ create a single escaped $.
#struct: pack() & unpack(), working with binary data record layouts
#
#threading:
#queue:
#Queue
#    While locks,events,condition variables,semaphores, are powerful, minor design errors can result in problems that are difficult to reproduce. So, the preferred approach to task coordination is to concentrate all access to a resource in a single thread and then use the queue module to feed that thread with requests from other threads. Applications using Queue objects for inter-thread communication and coordination are easier to design, more readable, and more reliable.
#
#logging:
#
#gc
#weakref:
#    The weakref module provides tools for tracking objects without creating a reference. When the object is no longer needed, it is automatically removed from a weakref table and a callback is triggered for weakref objects. Typical applications include caching objects that are expensive to create.
#
#list
#array: array(), regular lists of python int objects is usual 16 bytes per entry
#collections: deque()
#bisect:
#heapq
#
#decimal: is helpful for financial applications
#
#
#
#scipy.org
#docs.python.org
#pypi.python.org
#http://code.activestate.com/recipes/langs/python/
#
#comp.lang.python
#python-list@python.org
#
#Based on GNU Readline library:
#
#line editing
#    If supported, input line editing is active whenever the interpreter prints a primary or secondary prompt. The current line can be edited using the conventional Emacs control characters. The most important of these are:
#    C-A (Control-A) moves the cursor to the beginning of the line
#    C-E to the end
#    C-B moves it one position to the left
#    C-F to the right
#    Backspace erases the character to the left of the cursor
#    C-D the character to its right
#    C-K kills (erases) the rest of the line to the right of the cursor
#    C-Y yanks back the last killed string
#    C-underscore undoes the last change you made, it can be repeated for cumulative effect
#
#history substitution
#    History substitution works as follows. All non-empty input lines issued are saved in a history buffer, and when a new prompt is given you are positioned on a new line at the bottom of this buffer.
#    C-P moves one line up (back) in the history buffer
#    C-N moves one down
#    Any line in the history buffer can be edited; an asterisk appears in front of the prompt to mark a line as modified.
#    Pressing the Return key passes the current line to the interpreter.
#    C-R starts an incremental reverse search
#    C-S starts a forward search
#
#key bindings
#    The key bindings and some other parameters of the Readline library can be customized by placing commands in an initialization file called ~/.inputrc. Key bindings have the form
#    key-name: function-name    eg. Meta-h: backward-kill-word
# or "string": function-name    eg. "\C-x\C-r": re-read-init-file
#and options can be set with
#    set option-name value      eg. set editing-mode vi
#
#    Note that the default binding for Tab in Python is to insert a Tab character instead of Readline’s default filename completion function. If you insist, you can override this by putting
#    Tab: complete
#    in your ~/.inputrc
#
#    Automatic completion of variable and module names is optionally available. To enable it in the interpreter’s interactive mode, add the following to your startup file(python read PYTHONSTARTUP when start an interactive interpreter.):
#    import rlcompleter, readline
#    readline.parse_and_bind(’tab: complete’)
#
#A more capable startup file might look like this example.(interactive environment)
#
## Add auto-completion and a stored history file of commands to your Python
## interactive interpreter. Requires Python 2.0+, readline. Autocomplete is
## bound to the Esc key by default (you can change it - see readline docs).
##
## Store the file in ~/.pystartup, and set an environment variable to point
## to it: "export PYTHONSTARTUP=~/.pystartup" in bash.
#
#import atexit
#import os
#import readline
#import rlcompleter
#
#historyPath = os.path.expanduser("~/.pyhistory")
#
#def save_history(historyPath=historyPath):
#    import readline
#    readline.write_history_file(historyPath)
#
#if os.path.exists(historyPath):
#    readline.read_history_file(historyPath)
#
#atexit.register(save_history)
#del os, atexit, readline, rlcompleter, save_history, historyPath
#
#
#alternatives to the interactive interpreter: IPython and bpython
#
#
# round() can be useful for post-rounding during floating point arithmetic
# decimal:
# fractions:
# float.as_integer_ratio() method expresses the value of a float as a fraction
# float.hex() again giving the exact value stored by the computer
# math.fsum()
#
#
#
#
#
#
#
#
#
#
#
##############################################################################

import os
import sys

def main():
    pass

if __name__ == '__main__':
    main()
    pass
    import sys
    print(sys.argv)
    user_interface() # samle ?
    testing()
