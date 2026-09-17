# ruff: noqa: I001
# ruff: noqa: BLE001

# Imports
import os
import sys
import threading as thr
import time
import typing
import keyboard as kb
import typer
from modules import clear_cls_command, hotkeys, install_libs
from rich import print

install_libs.installlibs("rich", "keyboard", "typer")

# Inicializamos la aplicación Typer
app = typer.Typer(help="NameTitleApp CLI con Typer")


def run_app(name: str) -> None:
    """
    Logica central de la aplicacion que ejecuta los hilos y espera la salida.
    """
    thr_clearcls = thr.Thread(target=clear_cls_command.clear_cls)
    thr_inithotkeys = thr.Thread(target=hotkeys.init_hotkeys)

    thr_clearcls.start()
    time.sleep(0.1)
    thr_inithotkeys.start()
    time.sleep(0.1)

    print(f"Bienvenido. {name}")

    print("Presiona [ESC] para terminar.")
    kb.wait("esc")


# Callback principal: Maneja el comando base, argumentos de nombre y la flag --debug
@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    name_arg: str | None = typer.Argument(
        None, help="Nombre ingresado directamente por argumento"
    ),
    debug: bool = typer.Option(
        False,
        "--debug",
        help="Activa el modo debug (asigna nombre admin automáticamente)",
    ),
) -> typing.Any:
    """
    Funcion principal con soporte para argumentos directos y flags.
    """
    # Si el usuario ejecuta un subcomando (ej. 'init' o 'run'), dejamos que actúe dicho subcomando
    if ctx.invoked_subcommand is not None:
        return

    # Evaluamos la logica de negocio
    if debug:
        name = "Admin"
    elif name_arg:
        name = name_arg.strip().title()
    else:
        name = str(input("Ingresa tu nombre: ")).strip().title()

    run_app(name)


# Subcomando 'init' (ej: nametitleapp init)
@app.command()
def init(
    debug: bool = typer.Option(False, "--debug", help="Activa el modo debug en init"),
) -> None:
    """Subcomando init."""
    name = (
        "Admin"
        if debug
        else str(input("Ingresa tu nombre para init: ")).strip().title()
    )
    run_app(name)


# Subcomando 'run' (ej: nametitleapp run)
@app.command()
def run(
    debug: bool = typer.Option(False, "--debug", help="Activa el modo debug en run"),
) -> None:
    """Subcomando run."""
    name = (
        "Admin" if debug else str(input("Ingresa tu nombre para run: ")).strip().title()
    )
    run_app(name)


if __name__ == "__main__":
    try:
        app()
    except Exception as exc:
        print(
            f"\n[ERROR CRÍTICO]: {os.strerror(exc.errno) if hasattr(exc, 'errno') else exc}"
        )
        sys.exit(1)
