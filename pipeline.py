
"""Usage:
    python pipeline.py --input data.csv --output clean.csv
    python pipeline.py --input data.csv --output results.json --format json --verbose
"""

import argparse
import logging
import sys
from pathlib import Path


logger = logging.getLogger(__name__)


def setup_logging(verbose=False):
    # debgugs 
    level = logging.DEBUG if verbose else logging.INFO


    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)-8s %(message)s",
        datefmt="%H:%M:%S",
    )


def parse_arguments():
    """ command line args"""
    parser = argparse.ArgumentParser(
        description="Data processing pipeline (DS 3500 MP1)."
    )
    parser.add_argument(
        "--input", "-i",
        required=True,
        help="Path to the input file",
    )
    parser.add_argument(
        "--output", "-o",
        required=True,
        help="Path to the output file",
    )
    parser.add_argument(
        "--format",
        choices=["csv", "json"],   # argparse rejects anything else automatically
        default="csv",
        help="Output format (default: csv)",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",       # True if the flag is present, False otherwise
        help="Enable verbose logging",
    )
    return parser.parse_args()


def validate_input(filepath):
    """Check whether the input path exists and is a file."""
    if Path(filepath).is_file():
        logger.info("Input file validated: %s", filepath)
        return True

    logger.error("Input file not found: %s", filepath)
    return False


def main():
    """Main pipeline function."""
    # Parse first: we need args.verbose before logging can be configured.
    args = parse_arguments()
    setup_logging(args.verbose)

    logger.debug(
        "Arguments parsed: input=%s, output=%s, format=%s",
        args.input, args.output, args.format,
    )

    if not validate_input(args.input):
        sys.exit(1)



if __name__ == "__main__":
    main()