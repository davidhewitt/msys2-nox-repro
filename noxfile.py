import nox
import sys

@nox.session()
def test(session: nox.Session) -> None:
    print("nox python is", sys.executable)
    session.install("tqdm")
