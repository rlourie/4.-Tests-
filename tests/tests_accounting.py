import pytest
import unittest
import builtins
import mock
from src import accounting
from unittest.mock import patch


class TestFunctions:
    def test_get_doc_owner_name(self):
        with mock.patch.object(builtins, 'input', lambda _: '11-2'):
            assert accounting.get_doc_owner_name() == 'Геннадий Покемонов'
        with mock.patch.object(builtins, 'input', lambda _: '2207 876234'):
            assert accounting.get_doc_owner_name() == 'Василий Гупкин'
        with mock.patch.object(builtins, 'input', lambda _: '10006'):
            assert accounting.get_doc_owner_name() == 'Аристарх Павлов'
        with mock.patch.object(builtins, 'input', lambda _: '2207 87634'):
            assert accounting.get_doc_owner_name() is None

    def test_get_all_doc_owners_names(self):
        data = []
        for dict in accounting.documents:
            for keys, value in dict.items():
                if keys == "name":
                    data.append(value)
        my_set = set(data)
        assert accounting.get_all_doc_owners_names() == my_set

    def test_add_new_shelf(self):
        with mock.patch.object(builtins, 'input', lambda _: '4'):
            assert accounting.add_new_shelf() == ('4', True)
        with mock.patch.object(builtins, 'input', lambda _: '3'):
            assert accounting.add_new_shelf() == ('3', False)

    def test_delete_doc(self):
        with mock.patch.object(builtins, 'input', lambda _: '11-2'):
            assert accounting.delete_doc() == ('11-2', True)
        with mock.patch.object(builtins, 'input', lambda _: '11-3'):
            assert accounting.delete_doc() is None

    def test_get_doc_shelf(self):
        with mock.patch.object(builtins, 'input', lambda _: '10006'):
            assert accounting.get_doc_shelf() == '2'
        with mock.patch.object(builtins, 'input', lambda _: '115461'):
            assert accounting.get_doc_shelf() is None

    @patch('builtins.input', side_effect=['45678', 'passport', 'Арсений Крылов', '3'])
    def test_add_new_doc(self, mock_input):
        assert accounting.add_new_doc() == '3'
        assert len(accounting.documents) == 4
        assert accounting.documents[3].get("name") == 'Арсений Крылов'
        assert accounting.directories.get("3") == ['45678']
