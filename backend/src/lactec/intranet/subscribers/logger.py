from lactec.intranet import logger

import os


def log_events(event: object):
    """Escreve no log todos os eventos disparados pelo processo do backend
    se a variável de ambiente DEBUG estiver definida.
    """
    if not os.environ.get("DEBUG"):
        return

    # Caminho do módulo que disparou o evento
    module_name = event.__class__.__module__

    # Classe que disparou o evento
    class_name = event.__class__.__name__

    # Caminho completo da classe que disparou o evento
    dotted_name = f"{module_name}.{class_name}"

    logger.info(f"\nEvento disparado: {dotted_name} ({event})\n")
