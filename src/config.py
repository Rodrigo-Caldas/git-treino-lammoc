
from pathlib import Path

from pydantic_settings import BaseSettings


class Configuracoes(BaseSettings):
    url_merge: str = "https://ftp.cptec.inpe.br/modelos/tempo/MERGE/GPM/DAILY"
    diretorio: Path = Path("MERGE")


config = Configuracoes()
config.diretorio.mkdir(parents=True, exist_ok=True)