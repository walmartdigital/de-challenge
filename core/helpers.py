import sys
import os
import traceback



# for current func name, specify 0 or no argument.
# for name of caller of current func, specify 1.
# for name of caller of caller of current func, specify 2. etc.
this_function = lambda n=0: sys._getframe(n + 1).f_code.co_name #+ " Line :" + str(sys._getframe(n + 1).f_lineno)


class Emoji():
    ok= '[✔️]'
    bad= '[❌]'
    info= '[🔍]'
    fire= '[🔥]'
    warning= '[⚠️]'
    note= '[📑]'
    danger= '[❗]'
    save= '[💾]'
    con= '[🔌]'
    zip= '[🗜️]'
    screen= '[🖥️]'
    comment= '[💬]'
    mage= '[🧙]'
    nice='[👌]'
    next='[⏭️]'
    race='[🏁]' 



def log(Exception=None):
    T, V, TB = sys.exc_info()
    return ''.join(traceback.format_exception(T, V, TB))  # +str(Exception)




def make_folder(route, permissions=755):
    def_name = sys._getframe().f_code.co_name
    try:
        os.system(f"mkdir -m {permissions} -p {route}")

        print(
            f"{Emoji.ok} {def_name} {route} {permissions}")

    except Exception as e:
        print(
            f"{Emoji.fire} {def_name}\n       ", log(e))



def error_handler(status, errors):
    error_status = {"status": status, "errors": errors}
    return error_status

 