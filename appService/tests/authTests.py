import unittest
from unittest.mock import patch, MagicMock

from app import create_app
from app.auth.models.user import User
from app.auth.utils import register


class AuthTests(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()


    def tearDown(self):
        self.app_context.pop()


    @patch('app.auth.utils.User')
    @patch('app.db.session.add')
    @patch('app.db.session.commit')
    def test_register(self, mock_commit, mock_add, mock_model_class):
        mock_model_instance = MagicMock()
        mock_model_class.return_value = mock_model_instance

        result = register("abirmoulick998@gmail.com", "asdf", "Abir")

        mock_model_class.assert_called_once_with()
        mock_add.assert_called_once_with(mock_model_instance)
        mock_commit.assert_called_once()
        self.assertIs(result, mock_model_instance)


if __name__ == '__main__':
    unittest.main()
