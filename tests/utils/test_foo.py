from mock_practice.utils.foo import RemovalService, UploadService, method

import unittest
from unittest import mock


class RmTestCase(unittest.TestCase):

    @mock.patch("mock_practice.utils.foo.os.path")
    @mock.patch("mock_practice.utils.foo.os")
    def test_rm(self, mock_os, mock_path):
        tmpfilepath = "./tmpfile"
        ref = RemovalService()

        mock_path.isfile.return_value = False
        ref.rm(tmpfilepath)
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")

        mock_path.isfile.return_value = True
        ref.rm(tmpfilepath)
        mock_os.remove.assert_called_with(tmpfilepath)


class UploadServiceTestCase(unittest.TestCase):

    def test_upload_complete(self):
        mock_removal_service = mock.create_autospec(RemovalService)
        reference = UploadService(mock_removal_service)
        
        reference.upload_complete("my uploaded file")
        mock_removal_service.rm.assert_called_with("my uploaded file")


class MethodTestCase(unittest.TestCase):

    def test_method(self):
        target = mock.Mock()

        method(target, "value")

        target.apply.assert_called_with("value")