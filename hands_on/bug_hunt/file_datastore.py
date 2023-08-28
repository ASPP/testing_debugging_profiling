import os


class FileDatastore:
    """Datastore based on a regular file system.

    Parameters
    ----------
    base_path: str
        Filesystem path at which the data store is based.
    """

    def __init__(self, base_path):
        if not os.path.exists(base_path):
            raise FileNotFoundError(f'Base path {base_path} does not exist')
        if not os.path.isdir(base_path):
            raise NotADirectoryError(f'Base path {base_path} exists but is not a directory')

        self.base_path = base_path

    def open(self, path, mode):
        """ Open a file-like object

        Parameters
        ----------
        path: str
            Path relative to the root of the data store.
        mode: str
            Specifies the mode in which the file is opened.

        Returns
        -------
        IO[Any]
            An open file-like object.
        """
        path = os.path.join(self.base_path, path)
        return open(path, mode)

    def read(self, path):
        """ Read a sequence of bytes from the data store.

        Parameters
        ----------
        path: str
            Path relative to the root of the data store.

        Returns
        -------
        bytes
            The sequence of bytes read from `path`.
        """
        with self.open(path, 'rb') as f:
            data = f.read()
        return data

    def write(self, path, data) -> None:
        """ Write a sequence of bytes to the data store.

        `path` contains the path relative to the root of the data store, including the name
        of the file to be created. If a file already exists at `path`, it is overwritten.

        Intermediate directories that do not exist will be created.

        Parameters
        ----------
        path: str
            Path relative to the root of the data store.
        data: bytes
            Sequence of bytes to write at `path`.
        """
        path = os.path.join(self.base_path, path)
        self.makedirs(os.path.dirname(path))
        with self.open(path, 'wb') as f:
            f.write(data)

    def exists(self, path):
        """ Returns True if the file exists.

        Parameters
        ----------
        path: str
            Path relative to the root of the data store.

        Returns
        -------
        bool
            True if the file exists, false otherwise
        """
        complete_path = os.path.join(self.base_path, path)
        return os.path.exists(complete_path)

    def makedirs(self, path):
        """ Creates the specified directory if needed.

        If the directories already exist, the method does not do anything.

        Parameters
        ----------
        path: str
            Path relative to the root of the data store.
        """
        complete_path = os.path.join(self.base_path, path)
        os.makedirs(complete_path, exist_ok=True)


if __name__ == '__main__':
    data = b'A test! 012'
    datastore = FileDatastore(base_path='./datastore')
    datastore.write('a/mydata.bin', data)

    # This should pass!
    # The code works correctly if `base_path` is an absolute path :-(
    assert os.path.exists('./datastore/a/mydata.bin')
