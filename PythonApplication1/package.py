# package
# effective maintenance of pathon modules hierarchically
# no keyword. conceptual
# directory base

# e.g: game package
# game/
#     __init__.py
#     sound/
#         __init__.py
#         echo.py
#         wav.py
#     graphic/
#         __init__.py
#         screen.py
#         render.py
#     play/
#         __init__.py
#         run.py
#         test.py


# game, sound, graphic, play is directory name. "directory name" itself means "package"
# *.py files are module
# "__init__.py" is special file which notify the directory contain this file is "package"
# for >= python3.3, it is optional, but for compatibility, it had better exist in the folder

# if module name  A.B, then A means "package" and B means "module"

# for exercise,
# 1. create "game" directory and subsequent directories and simple python under that folder
# 2. set pythonpath=C:\git\private\Python\C
# SharpWithPython\PythonApplication1
# 3. then, open python shell
# 4. following one of three ways to execute
# (NOTE) Once one of ways is executed, then exit python shell to avoid unexpected error by "Ctrl+Z"

# 4-1.
# import game.sound.echo
# game.sound.echo.echo_test()

# 4-2.
# from game.sound import echo
# echo.echo_test()

# 4-3.
# from game.sound.echo import echo_test
# echo_test()

# NOTE: On importing with . (dot operator), the last item must be package or module