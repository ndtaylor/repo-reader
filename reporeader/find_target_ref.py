from argparse import ArgumentParser

import re
import requests

_PR_REST_URL_TEMPLATE = "https://api.bitbucket.org/2.0/repositories/{}/{}/pullrequests/{}"
_PR_URL_PATTERN = re.compile('^https://bitbucket\.org/([^/]+)/([^/]+)/pull-requests/(\d+)$')


def _get_bitbuck_pr_rest_url(pr_url: str) -> str:
    match = _PR_URL_PATTERN.match(pr_url)
    if match:
        user = match.group(1)
        repo = match.group(2)
        pr_id = match.group(3)
    else:
        raise RuntimeError("Url provided does not match known pattern: {}".format(pr_url))

    return _PR_REST_URL_TEMPLATE.format(user, repo, pr_id)


def get_target_ref(args) -> str:
    if not args.pr_url:
        return 'origin/master'

    pr_rest_url = _get_bitbuck_pr_rest_url(args.pr_url)
    response = requests.get(pr_rest_url, auth=(args.auth_user, args.auth_password))
    response.raise_for_status()
    return response.json()['destination']['commit']['hash']


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-u', '--auth_user', type=str, required=True)
    parser.add_argument('-p', '--auth_password', type=str, required=True)
    parser.add_argument('-r', '--pr_url', type=str, nargs='?', default='')
    args = parser.parse_args()

    print(get_target_ref(args))
