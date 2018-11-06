# mlperf-submission-helper

Usage:

```
git clone https://github.com/bitfort/mlp_compliance
git clone https://github.com/CiscoAI/mlperf-submission-helper

# If you need encryption/decryption:
pip install -r mlperf-submission-helper/requirements.txt

PYTHONPATH=mlp_compliance,mlperf-submission-helper/mlperf_submission_helper \
python mlperf-submission-helper/mlperf_submission_helper/verify_submission.py
```

Cmd options:

```
python verify_submission.py [-h] [--encrypt-key PUBLIC_KEY]
                            [--encrypt-out ENCRYPT_OUT]
                            [--decrypt-key PRIVATE_KEY]
                            [--decrypt-out DECRYPT_OUT]
                            SUBMISSION_ROOT
```
