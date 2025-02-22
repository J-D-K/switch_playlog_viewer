#!/usr/bin/en python3
import sys
import argparse
import io
import datetime

# Argument parser.
argParser = argparse.ArgumentParser()

# Command line arguments.
argParser.add_argument("-l", "--log", dest="str_logFile", help="Log file from your Switch's system save data.", required=True)


def main() -> int:
    # Print an extra line to make stuff easier to read.
    print(end="\n")

    # Parse arguments
    cmdArgs = argParser.parse_args()

    try:
        # I'm assuming these file modes are the same as C?
        with io.open(cmdArgs.str_logFile, mode="rb") as file_logFile:

            # This file only stores the last 20 entries?
            for i in range(20):

                # Read everything off since python is weird and I can't do it like in superior C/C++.
                uint64_titleIdA = int.from_bytes(file_logFile.read(8), "little")
                uint64_unknownA = int.from_bytes(file_logFile.read(8), "little")
                uint64_titleIdB = int.from_bytes(file_logFile.read(8), "little")
                uint32_timesPlayed = int.from_bytes(file_logFile.read(4), "little")
                uint32_minutesPlayed = int.from_bytes(file_logFile.read(4), "little")
                uint64_firstPlayed = int.from_bytes(file_logFile.read(8), "little")
                uint64_lastPlayed = int.from_bytes(file_logFile.read(8), "little")

                # Print the information. I'm doing this in multiple calls so it isn't as hard to read.
                print(f"Title ID A: {uint64_titleIdA:016X}", end="\n")
                print(f"Unknown A: {uint64_unknownA}", end="\n")
                print(f"Title ID B: {uint64_titleIdB:016X}", end="\n")
                print(f"Times played: {uint32_timesPlayed}", end="\n")
                print(f"Minutes played: {uint32_minutesPlayed}", end="\n")
                print(f"First played: {datetime.datetime.fromtimestamp(uint64_firstPlayed)}", end="\n")
                print(f"Last played: {datetime.datetime.fromtimestamp(uint64_lastPlayed)}", end="\n\n")

    # Maybe handle the rest some other time.
    except FileNotFoundError:
        print("Error opening log save file: Not found.", end="\n\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
