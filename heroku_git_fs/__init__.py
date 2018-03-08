import git

class HerokuGitFS:
    def __init__(self, remote_url: str, directory: str, keep_history: bool = False):
        """
        :param remote_url:
        :param directory:
        :param keep_history:
        """
        self.remote_url = remote_url
        self.directory = directory
        self.keep_history = keep_history
        self.repo = git.Repo.clone_from(url=remote_url, to_path=directory)
        print(f'Sucessfully initialized {directory} from the git repo')

    def commit(self, *, message="No message given."):
        self.repo.git.add('-A')
        self.repo.git.commit(['--message', message])

    def push(self, branch="master", remote_url=None):
        if remote_url is None:
            remote_url = self.remote_url
        pass

    def update(self):
        self.commit()
        self.update()