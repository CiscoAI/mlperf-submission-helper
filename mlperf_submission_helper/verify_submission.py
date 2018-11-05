import argparse
import os

import checks as submission_checks
import constants
import report


def verify_submission(args):
    root_dir = args.root
    public_key = args.public_key
    private_key = args.private_key

    checks = submission_checks.SubmissionChecks()
    checks.verify_dirs_and_files(root_dir)
    checks.verify_metadata()
    checks.compile_results()

    checks.report.print_report()
    checks.report.print_results()


def main():
    parser = argparse.ArgumentParser(description="Verify MLPerf submission.")
    parser.add_argument("root", help="submission root directory")
    parser.add_argument("--encrypt-key", dest="public_key", default=None,
                        help="public key for encrypting log files")
    parser.add_argument("--encrypt-out", dest="encrypt_out", default=None,
                        help="output path for encrypted submission")
    parser.add_argument("--decrypt-key", dest="private_key", default=None,
                        help="private key for decrypting log files")
    parser.add_argument("--decrypt-out", dest="decrypt_out", default=None,
                        help="output path for decrypted submission")
    args = parser.parse_args()

    verify_submission(args)


if __name__ == "__main__":
    main()
