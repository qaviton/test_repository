import time
from load_tests.utils import client_request, stats


def test_peak(stats):
    """send 50 client requests at once with 0.3 delay between them"""

    n = 50
    delay = 0.3

    r = []
    for i in range(n):
        r.append(client_request("{}:{}".format(n, i), stats))
        time.sleep(delay)
    for thread in r:
        thread.join()
