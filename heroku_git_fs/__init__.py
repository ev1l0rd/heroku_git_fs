import git
import getpass

class HerokuGitFS:
    def __init__(self, remote_url: str, directory: str, branch: str, keep_history: bool = False):
        """
        Initiate a new gitFS folder.

        :param branch: The branch to push and commit changes to
        :param remote_url: The remote URL for the branch
        :param directory: The directory to clone to
        :param keep_history: If set to True, then the git repository will not be orphaned on each new commit.
        """
        self.remote_url = remote_url
        self.directory = directory
        self.keep_history = keep_history
        self.branch = branch
        self.repo = git.Repo.clone_from(url=remote_url, to_path=directory)
        print('Sucessfully initialized {0} from the git repo'.format(directory))
        self.repo.git.remote(['rm', 'origin'])
        self.repo.git.checkout(['-B', branch])
        print('Checked out branch {0}'.format(self.branch))

    def commit(self, message: str = 'No message given.', username: str = getpass.getuser(), email: str ='dummy@email.com'):
        """
        Create a new commit. If the keep_history attribute is set to False, the branch will be orphaned.

        :param message: The commit message.
        :param username: The name to commit with, defaults to the current user.
        :param email: The email to commit with, defaults to a dummy email.
        """
        if not self.keep_history:
            self.repo.git.checkout(['--orphan', 'temp'])

        self.repo.git.config(['user.name', username])
        self.repo.git.config(['user.email', email])
        self.repo.git.add('-A')
        self.repo.git.commit(['--message', message])

        if not self.keep_history:
            self.repo.git.branch(['-M', 'temp', self.branch])

    def push(self, remote_url=None):
        """
        Push the commit to the remote.

        :param remote_url: The remote URL to push for. Optional. If it is left out/set to None, it will be ignored.
        """
        if remote_url is None:
            remote_url = self.remote_url
        try:
            self.repo.git.push(['--force', remote_url, self.branch])
        except Exception as e:
            raise e

    def update(self, username: str = getpass.getuser(), email: str ='dummy@email.com'):
        """
        Wrapper around commit and push.
        :param username: The name to commit with, defaults to the current user.
        :param email: The email to commit with, defaults to a dummy email.
        """
        self.commit(username=username, email=email)
        self.push()
