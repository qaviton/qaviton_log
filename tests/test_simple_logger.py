from qaviton_log import Logger
from os import sep


def test_log(tmpdir):
    file = f'{tmpdir}{sep}logfile.log'
    log = Logger(file=file, stream=False)
    log.info('hi')
    log.error('bye')
    with open(file) as f:
        lines = [line.split(' [', 1)[1] for line in f.read().splitlines()]
    assert lines[0] == 'INFO] hi'
    assert lines[1] == 'ERROR] bye'
