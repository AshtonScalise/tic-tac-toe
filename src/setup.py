from cx_Freeze import setup, Executable


base = "Win32GUI"

build_exe_options = {}

setup(  name = "TicTacToe",
        version = "0.1",
        description = "My GUI application!",
        options={"build_exe": build_exe_options},
        executables=[Executable("tic_tac_UI.py")]
)
