## Description

`link_validator.py` contains the `check_validity` function which accepts a list of URLs and returns a subset of those URLs that are either written improperly or do not return a success status code, along with a helpful error message indicating what was wrong. 

## Usage

You can run the file with the following command:

`python link_validator.py`

However, running it this way will require a list of urls to be added to the file.

## Running tests

Simply run the following command to kick off the unit tests.

`python test_link_validator.py`

## Additional thoughts

> Could the function be improved if the same list of links is being passed in many times, and what are the tradeoffs?

If it was expected that the same urls would be passed in, we could cache the 'previously processed urls' and check the cache first before performing the checks on a url. This could improve execution time by eliminating repeated work, but would increase memory as we are now storing values in a cache.

> How might the function be written to process arbitrarily long lists of links?

Because the function has a few synchronous calls in it, the easiest way to have it handle longer lists of links would be to use multiple threads. This would allow us to run the blocking code on separate threads which would improve execution time.

> How might this function be exposed as an HTTP API to be used by a front-end application?

The function could be rewritten to work well with an HTTP API. If we threw this up as a simple Flask app, we could expose the endpoint and allow users to perform a GET to it with the url they would like to validate. This might look something like:

```python
@app.route('/validator/api/v1.0/check_validity/<str:url>', methods=['GET'])
def check_validity(url):
    # Our code
    return jsonify({'output': output})
```

We would then use basically the same code to perform our validation and return a JSON version of our output.
