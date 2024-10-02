
import argparse
import os
import sys
import subprocess
import yaml

INSTALL_PATH=os.path.expanduser("~/.workspace")
CONFIG_FILE_PATH=os.path.join(INSTALL_PATH, "config.yaml")
DOCKER_COMPOSE_FILE_PATH=os.path.join(INSTALL_PATH, "docker-compose.yaml")
BASE_DOCKER_COMMAND = ["docker", "compose", "-f", f"{DOCKER_COMPOSE_FILE_PATH}"]

parser = argparse.ArgumentParser(prog='workspace|wc',
                    description='What the program does',
                    epilog='Text at the bottom of help')

# required = parser.add_argument_group('required arguments')
# p1 = required.add_argument("koko", help="koko")
# p2 = required.add_argument("wawa", help="wawa")

actions_subparser = parser.add_subparsers(dest='action', help="Choose one of the actions", required=True)
up_parser = actions_subparser.add_parser("up", help="Create and start containers")
up_parser.add_argument('services', nargs='*', help="list of local stack services to deploy, if empty then all services will be deployed")

down_parser = actions_subparser.add_parser("down", help="Stop and remove containers, networks")
down_parser.add_argument('services', nargs='*', help="list of local stack services to terminate, if empty then all services will be terminated")

restart_parser = actions_subparser.add_parser("restart", help="Restart service containers")
restart_parser.add_argument('services', nargs='*', help="list of local stack services to restart, if empty then all services will be restarted")

go_parser = actions_subparser.add_parser('go', help="Manage go service")
go_operations = go_parser.add_subparsers(dest='operation', help="Choose one of the go operations", required=True)
go_run = go_operations.add_parser('run', help='Run go service')
go_run.add_argument('service', nargs=1, help="Run go service")
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')

def load_config_file():
    with open(CONFIG_FILE_PATH) as f:
        yaml_data = yaml.safe_load(f)
        return yaml_data
    return {}

def main(args):
    
    match args.action:
        case "up":
            if args.services :
                subprocess.run(BASE_DOCKER_COMMAND + ["start"] + args.services)
            else:
                subprocess.run(BASE_DOCKER_COMMAND + ["up", "--build", "-d"])
        case "down":
            if args.services :
                subprocess.run(BASE_DOCKER_COMMAND + ["stop"] + args.services)
            else:
                subprocess.run(BASE_DOCKER_COMMAND + ["down"])
        case "restart":
                subprocess.run(BASE_DOCKER_COMMAND + ["restart"] + args.services)
                print("restart is a test")
        case "go":
                print(f"Running go service {args=}")
        case _:
            print("Unknown command action")
            sys.exit(1)

if __name__ == '__main__':
    args = parser.parse_args()
    print(args)

    print(args.action)

    # print(args.filename, args.count, args.verbose)
    # print(args.accumulate(args.integers))
    # subprocess.run(["ls", "-l"])
    # print(INSTALL_PATH)

    print(f"config.yaml content: {load_config_file()}")

    
    main(args)
    