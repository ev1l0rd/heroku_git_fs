.. _tutorial:

Tutorial
========

HerokuGitFS is a way to have a persistent filesystem on ephemeral filesystems or to have a folder that is synchronized to a git repository.

Originally written for Heroku, HerokuGitFS also works without Heroku.

Getting Started
---------------

To start using HerokuGitFS, simply instantaniate the class as follows::

	heroku_git_fs = HerokuGitFS("http://example.io/something.git", 
		"storage", "master", False)

The first parameter is the git clone URL. This URL is used both for the initial clone and to push the database later. If your method requires some form of authorization, you will need to include this in the clone URL.

The second parameter is the folder where the class should clone to. The only requirement is that this folder does not exist, otherwise an error is raised.

The third parameter is the branch to use. Note that this branch should `not` be protected on the remote, as commits are always force pushed.

The final parameter is wether to keep the history or not. By default, HerokuGitFS orphans the current branch and makes a new commit in a new branch and then shoves it over the old branch. This is to reduce clone times when setting up the bot. If you need to keep track of the Git history for some reason, you can set this to True.

You can omit the final parameter, and it will be assumed to be False (so history will be overwritten).

For a shorter overview, refer to :any:`HerokuGitFS.__init__()`

Committing changes
------------------

Changes should be committed whenever the files in the storage folder finish updating. In order to do this, you should call :any:`HerokuGitFS.commit()` and then :any:`HerokuGitFS.push()`. Refer to the example below::

	heroku_git_fs.commit()
	heroku_git_fs.push()

The commit function can optionally take parameters for the message, the author and the email. If these aren't supplied, they are automatically filled for you (username is pulled from the OS).

The push function can optionally take a remote URL if you want to push to a different repository than the one that is cloned from.

In order to reduce code for these steps, there is a wrapper around :any:`HerokuGitFS.commit()` and :any:`HerokuGitFS.push()` called :any:`HerokuGitFS.update()` that will call these two in order for you. It optionally takes the same parameters as the commit function::

	heroku_git_fs.update()

Removing the repository
-----------------------

To properly remove the repository, run the :any:`HerokuGitFS.close()` function. This will try to remove the directory that was set up during init.


with functionality
------------------

HerokuGitFS works properly with..\. well, with statements. By using a with statement, the repository is automatically removed (:any:`HerokuGitFS.close()` is called) when exiting the scope::

	with HerokuGitFS("http://example.io/something.git", 
		"storage", "master", False) as heroku_git_fs:
		# do cool stuff here
	# here the FS will be gone
