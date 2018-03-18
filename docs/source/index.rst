.. heroku_git_fs documentation master file, created by
   sphinx-quickstart on Fri Mar  9 21:06:04 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

heroku_git_fs
=============

Persistent storage through a git repository for ephemeral filesystems.

Installation can be done with::

	pip install heroku_git_fs

After that the object can be imported by importing it::

	from heroku_git_fs import HerokuGitFS

And then be used either through with statements or simply instantaniated. (with is recommended as this ensures proper cleanup)::

	heroku_git_fs = HerokuGitFS("http://example.io/something.git",
        "storage", "master", False)
	heroku_git_fs.update()
	heroku_git_fs.close()
	
	# or
	with HerokuGitFS("http://example.io/something.git", "storage", 
	     "master", False) as heroku_git_fs:
                 heroku_git_fs.update()

See the :ref:`tutorial` for details.

Index
-----

.. toctree::
   :maxdepth: 2

   modules
   tutorial



Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
