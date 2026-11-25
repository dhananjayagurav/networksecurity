import subprocess


class S3Sync:
    """Thin wrapper around `aws s3 sync`. Raises if the AWS CLI reports a failure."""

    def _run(self, source: str, destination: str) -> None:
        # List form (no shell): paths with spaces work, and nothing is interpreted by a shell.
        # check=True: a non-zero exit code (bad bucket, no credentials, no network) raises
        # CalledProcessError instead of being silently ignored like os.system did.
        subprocess.run(["aws", "s3", "sync", source, destination], check=True)

    def sync_folder_to_s3(self, folder, aws_bucket_url):
        self._run(folder, aws_bucket_url)

    def sync_folder_from_s3(self, folder, aws_bucket_url):
        self._run(aws_bucket_url, folder)
