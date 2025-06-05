"""Módulo referente as funções merge."""

import requests
import pandas as pd

from src.config import config
from pathlib import Path


def obter_merge(data: pd.Timestamp) -> None:
    """
    Baixa MERGE.

    Parameters
    ----------
    data : pd.Timestamp
        Timestamp
    """
    with requests.Session() as session:
        arquivo = f'MERGE_CPTEC_{data.year}{data.strftime("%m")}{data.strftime("%d")}.grib2'
        url_requisicao = (
                f"{config.url_merge}/{data.year}/{data.strftime("%m")}/{arquivo}"
            )
        
        resposta = session.get(url_requisicao, timeout=30)

        if resposta.status_code == 200:
            conteudo = resposta.content
            diretorio_saida = Path(config.diretorio, arquivo)

            with open(diretorio_saida, "wb") as arquivo_:
                arquivo_.write(conteudo)

            print(f"{arquivo} [ok]")

        else:
            print(f"Não foi possível obter o {arquivo}.")