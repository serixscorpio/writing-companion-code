import api
import client1
import client2


def test_client1_offset(mocker):
    # `client1` already have a reference to `expensive_calculation`,
    # so patch on `client1`.
    mock = mocker.patch.object(client1, "expensive_calculation", return_value=20)
    assert client1.offset(1) == 21


def test_client2_offset(mocker):
    # `client2` does not have a reference to `expensive_calculation`,
    # so patch on `api`.
    mock = mocker.patch.object(api, "expensive_calculation", return_value=20)
    assert client2.offset(1) == 21
