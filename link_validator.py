from urllib.parse import urlparse
from urllib.request import urlopen, Request
from urllib import error


def check_validity(urls):
    """
    Accepts a list of urls and checks to see if they are formatted
    properly and are reachable.

    The function checks the scheme, then network location (hostname),
    and if both of those exist, it will attempt to request the url and
    record any error messages it receives. It uses a real User-Agent so
    it can get past redirects and 403s.

    urls: List of urls to be validated

    returns: List of all urls that are not valid with as well as a
    helpful error message.
    """

    invalid_urls = []
    user_agent = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X "
                                "10_12_3) AppleWebKit/537.36 (KHTML, like "
                                "Gecko) Chrome/56.0.2924.87 Safari/537.36"}

    for url in urls:
        result = urlparse(url)

        if not bool(result.scheme):
            invalid_urls.append([url, "Missing or invalid URL protocol."])
        elif not bool(result.netloc):
            invalid_urls.append([url, "Missing or invalid URL hostname."])
        else:
            try:
                req = Request(url, headers=user_agent)
                urlopen(req)
            except error.URLError as e:
                invalid_urls.append([url, "Failed to connect to URL. "
                                          "Reason: {}".format(e.reason)])

    return invalid_urls
