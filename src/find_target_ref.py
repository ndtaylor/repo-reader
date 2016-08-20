from argparse import ArgumentParser
import re

pr_id_pattern = re.compile('^https://bitbucket.org/(.+?)/(.+?)/pull-requests/(\d+)$]')


def get_bitbuck_pr_api_url(user_pr_url: str) -> str:
    match = pr_id_pattern.match(user_pr_url)
    if match:
        user = match.group(1)
        repo = match.group(2)
        pr_id = match.group(3)
    else:
        raise RuntimeError("Url provided does not match known pattern: {}".format(user_pr_url))

    return "https://api.bitbucket.org/2.0/repositories/{}/{}/pullrequests/{}".format(user, repo,
                                                                                     pr_id)


if __name__ == 'main':
    parser = ArgumentParser()
    parser.add_argument('pull_request_url', type=str)
    args = parser.parse_args()

    pr_rest_url = get_bitbuck_pr_api_url(args.pull_request_url)
