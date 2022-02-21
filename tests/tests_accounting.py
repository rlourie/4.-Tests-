import pytest
import builtins
import mock
from src import accounting


class TestFunctions:
    def test_get_doc_owner_name(self):
        with mock.patch.object(builtins, 'input', lambda _: '11-2'):
            assert accounting.get_doc_owner_name() == 'Геннадий Покемонов'
        with mock.patch.object(builtins, 'input', lambda _: '2207 876234'):
            assert accounting.get_doc_owner_name() == 'Василий Гупкин'
        with mock.patch.object(builtins, 'input', lambda _: '2207 87634'):
            assert accounting.get_doc_owner_name() == None

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
        with mock.patch.object(builtins, 'input', lambda _: '11-2'):
            assert accounting.get_doc_shelf() == '1'
        with mock.patch.object(builtins, 'input', lambda _: '11-3'):
            assert accounting.get_doc_shelf() is None

    def test_new_doc(self):
        with mock.patch.object(builtins, 'input', lambda ____: '15', '2', '3', '4'):
            assert accounting.add_new_doc() == 1
