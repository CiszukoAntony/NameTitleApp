# ruff: noqa: I001
# ruff:noqa: BLE001

# Imports
import os
import sys
import threading as thr
import time
import typing
import keyboard as kb
from modules import clear_cls_command, hotkeys, install_libs
from rich import print

install_libs.installlibs("rich", "keyboard")

print("\n--- Iniciando sistema principal ---")


def main() -> typing.Any:
    """
    Funcion principal
    """
    thr_clearcls = thr.Thread(target=clear_cls_command.clear_cls)
    thr_inithotkeys = thr.Thread(target=hotkeys.init_hotkeys)

    thr_clearcls.start()
    time.sleep(0.1)
    thr_inithotkeys.start()
    time.sleep(0.1)

    print("Presiona [ESC] para terminar.")
    kb.wait("esc")
    os._exit(1)


if __name__ == "__main__":
    try:
        main()
        sys.exit(0)
    except Exception as exc:
        print(
            f"\n[ERROR CRÍTICO]: {os.strerror(exc.errno) if hasattr(exc, 'errno') else exc}"
        )
        sys.exit(1)
