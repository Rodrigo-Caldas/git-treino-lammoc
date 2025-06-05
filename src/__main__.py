"""Módulo principal da aplicação src."""

from datetime import datetime

import pandas as pd

from src.merge import obter_merge


def handler(data_inicio: datetime = datetime(2025, 1, 1), data_fim: datetime = datetime.today()) -> None:
    """
    Função para baixar os dados do merge a partir de uma data início e data fim.

    Parameters
    ----------
    data_inicio : datetime, optional
        Data início, by default datetime(2025, 5, 31)
    data_fim : datetime, optional
        Data fim, by default datetime.today()
    """
    datas = pd.date_range(start=data_inicio, end=data_fim, freq="D").tolist()

    for data in datas:
        obter_merge(data)

if __name__ == "__main__":

    handler()