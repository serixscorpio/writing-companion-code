import client1
import client2


def test_client1_offset(mocker):
    mock = mocker.patch.object(client1, "expensive_calculation", return_value=20)
    assert client1.offset(1) == 21


def test_client2_offset(mocker):
    mock = mocker.patch.object(client2.api, "expensive_calculation", return_value=20)
    assert client2.offset(1) == 21
