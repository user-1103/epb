"""
The top level program for epb
"""

from argparse import ArgumentParser, Namespace
from typing import Dict
from rich.progress import Progress
from rich.console import Console
from epb.stigs import STIGS
from epb.hash import SEALS, check, load_seals, mk_seal, save_seals
from subprocess import run


# get print log
log = Console()

def get_args() -> Namespace:
    """
    Get cli args
    
    :return: a dict of args
    """
    parser = ArgumentParser(description="Imutable STIG Hardener For Ubuntu")
    parser.add_argument("OPERATION",
                        choices=["harden", "check", "seal"],
                        help=("Harden system to STIG standards, "
                              " Chacks seals stored in a seals.json file"
                              ", Seal a directory and add it to seals.json."))
    parser.add_argument('--dry-run', default=False,
                        action='store_true',
                        help="Don't actualy modify the system.")
    args = parser.parse_args()
    return args

def main() -> None:
    """
    Run the program
    """
    args = get_args()
    if (args.OPERATION == "harden"):
        with Progress() as progress:
            task = progress.add_task("Applying STIGS...", total=len(STIGS))
            progress.advance(task)     
            for job in STIGS:
                progress.console.print(f"\nStarting STIG {job.uuid}: {job.description}")
                try:
                    if (job.function is not None):
                        if (not args.dry_run):
                            job.function()
                            mk_seal(job.path)
                    elif (job.command):
                        if (not args.dry_run):
                            run(job.command, shell=True, check=True, encoding='utf-8')
                            mk_seal(job.path)
                except Exception as e:
                    progress.console.print(f"Err in STIG {job.uuid}: {e}")
                else:
                    progress.console.print(f"Finished STIG {job.uuid}: ✔\n")
                progress.advance(task)     
        print(" ")
        log.log("Saving seals... Done...")
        save_seals()
    elif (args.OPERATION == "check"):
        load_seals()
        with Progress() as progress:
            task = progress.add_task("Checking STIGS...", total=len(SEALS))
            progress.advance(task)     
            for job in SEALS:
                try:
                    tmp = check(job)
                    if (tmp):
                        tmp = "[bold green]Valid[/bold green]"
                    else:
                        tmp = "[bold red]Invalid[/bold red]"
                    progress.console.print(f"\nSeal {job[0]}-{job[1]}: {tmp}")
                except Exception as e:
                    progress.console.print(f"Err in seal {job[0]-job[1]}: {e}")
                progress.advance(task)     
        print(" ")
        log.log("Done...")
        save_seals()
    elif (args.OPERATION == "seal"):
        dir = input("Directory to seal: ")
        log.log(f"Sealing: {dir}")
        load_seals()
        tmp = mk_seal(dir)
        dir = log.log(f"Seal {tmp[1]} added")
        save_seals()
    else:
        log.log(f"????")

if __name__ == "__main__":
    main()
