import pytest
import time
import logging
import requests
from threaders import threaders
import statistics
log = logging.getLogger()


@pytest.fixture(scope="session")
def stats():
    f = open("stats.txt", "w")
    results = {}
    total_time = time.time()

    yield results

    lowest_time = 99999999999999999
    highest_time = 0
    passtimes = []
    avg = 0
    med = 0
    passed = 0
    failed = 0
    total = len(results)
    pass_rate = 0

    for k in results:
        if results[k]["time"] < lowest_time:
            lowest_time = results[k]["time"]
        if results[k]["time"] > highest_time:
            highest_time = results[k]["time"]
        if results[k]["result"] == "pass":
            passed += 1
            passtimes.append(results[k]["time"])
        else:
            failed += 1

    if len(passtimes) > 0:
        avg = sum(passtimes)/len(passtimes)
        med = statistics.median(sorted(passtimes))
        pass_rate = passed*100/total

    f.write("best response: {}\n".format(lowest_time))
    f.write("worst response: {}\n".format(highest_time))
    f.write("avg: {}\n".format(avg))
    f.write("med: {}\n".format(med))
    f.write("passed: {}\n".format(passed))
    f.write("failed: {}\n".format(failed))
    f.write("total requests: {}\n".format(total))
    f.write("pass rate: {}\n".format(pass_rate))
    f.write("total duration: {}\n".format(total_time))
    f.close()


@threaders.threader()
def client_request(name, stats):
    """assert request is valid"""
    t = time.time()
    try:
        assert requests.get("https://www.qaviton.com/").status_code == 200
        stats[name] = {"result": "pass"}

    except Exception as e:
        stats[name] = {"result": "fail"}
        log.exception(e)
    stats[name]["time"] = time.time() - t