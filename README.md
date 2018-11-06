# mlperf-submission-helper

- Usage:

```
git clone https://github.com/bitfort/mlp_compliance
git clone https://github.com/CiscoAI/mlperf-submission-helper

# If you need encryption/decryption:
pip install -r mlperf-submission-helper/requirements.txt

PYTHONPATH=mlp_compliance,mlperf-submission-helper/mlperf_submission_helper \
python mlperf-submission-helper/mlperf_submission_helper/verify_submission.py
```

- Generate keys for encryption and decryption:

```
# you can give any name to your key file.
MLPERF_SUBM_KEY_NAME=mlperf_rsa
ssh-keygen -t rsa -b 1024 -f $MLPERF_SUBM_KEY_NAME -N ''
```

In the generated file, the private key is named `${MLPERF_SUBM_KEY_NAME}`, the public key is named `${MLPERF_SUBM_KEY_NAME}.pub`

- Command line options for `verify_submission.py`:

```
python verify_submission.py [-h] [--encrypt-key PUBLIC_KEY]
                            [--encrypt-out ENCRYPT_OUT]
                            [--decrypt-key PRIVATE_KEY]
                            [--decrypt-out DECRYPT_OUT]
                            SUBMISSION_ROOT
```
