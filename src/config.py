"""Arquivo de configurações."""

from pathlib import Path 

url = "https://ftp.cptec.inpe.br/modelos/tempo/MERGE/GPM/DAILY"
diretorio = Path("MERGE")

diretorio.mkdir(parents=True, exist_ok=True)