from argparse import ArgumentParser
import requests


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-u', '--auth_user', type=str)
    parser.add_argument('-p', '--auth_password', type=str)
    parser.add_argument('-o', '--project_user', type=str)
    parser.add_argument('-r', '--project_reponame', type=str)
    parser.add_argument('-n', '--pr_number', type=str)
    args = parser.parse_args()

    pr_rest_url = "https://api.bitbucket.org/2.0/repositories/{}/{}/pullrequests/{}".format(args.project_user,
                                                                                            args.project_reponame,
                                                                                            args.pr_number)
    response = requests.get(pr_rest_url, auth=(args.auth_user, args.auth_password))
    response.raise_for_status()
    pr_target = response.json()['destination']['commit']['hash']
    print(pr_target)
