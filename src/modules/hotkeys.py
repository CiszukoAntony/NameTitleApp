# Imports
import os
import sys

import keyboard as kb
from rich import print


def init_hotkeys() -> None:
    """
    Funcion que inicializa los hotkeys.
    """
    print("Usa CONTROL+Z para cerrar custom.")

    def ctrl_z_func():
        print("\nCerrado con control + z")
        os._exit(1)

    kb.add_hotkey(hotkey="ctrl+z", callback=ctrl_z_func)


if __name__ == "__main__":
    try:
        print("No se puede ejecutar este modulo por separado.")
        sys.exit(0)
    except Exception as exc:  # noqa: BLE001
        print(
            f"\n[ERROR CRÍTICO]: {os.strerror(exc.errno) if hasattr(exc, 'errno') else exc}"
        )
        sys.exit(1)
