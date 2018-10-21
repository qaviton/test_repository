import pytest
import time
from load_tests.utils import client_request, stats


@pytest.mark.parametrize('n', range(20))
def test_ramp(n, stats):
    """iterate 20 times, each time increase the number of requests, wait 0.4 secs between iterations"""

    delay = 0.4

    r = []
    for i in range(n+1):
        r.append(client_request("{}:{}".format(n, i), stats))
        time.sleep(delay)
    for thread in r:
        thread.join()


