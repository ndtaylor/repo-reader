from argparse import ArgumentParser
import requests


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--auth_user', type=str)
    parser.add_argument('--auth_password', type=str)
    parser.add_argument('--project_user', type=str)
    parser.add_argument('--project_reponame', type=str)
    parser.add_argument('--pr_number', type=str)
    args = parser.parse_args()

    pr_rest_url = "https://api.bitbucket.org/2.0/repositories/{}/{}/pullrequests/{}".format(args.project_user,
                                                                                            args.project_reponame,
                                                                                            args.pr_number)
    response = requests.get(pr_rest_url, auth=(args.auth_user, args.auth_password))
    response.raise_for_status()
    pr_target = response.json()['destination']['commit']['hash']
    print(pr_target)
