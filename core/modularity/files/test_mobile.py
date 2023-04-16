import pytest
from mobile import MobilePhone


@pytest.fixture
def phone():
    return MobilePhone('Huawei', 5.3, 8)


def test_mobile_is_built(phone: MobilePhone):
    assert isinstance(phone, MobilePhone)
    assert phone.manufacturer == 'Huawei'
    assert phone.screen_size == 5.3
    assert phone.num_cores == 8
    assert not phone.status
    assert len(phone.apps) == 0


def test_mobile_is_switched_on(phone: MobilePhone):
    phone.power_on()
    assert phone.status


def test_mobile_is_switched_off(phone: MobilePhone):
    phone.power_off()
    assert not phone.status


def test_app_is_installed(phone: MobilePhone):
    phone.install_app('Twitter')
    assert 'Twitter' in phone.apps


def test_app_is_not_installed_when_exists(phone: MobilePhone):
    phone.install_app('Twitter')
    phone.install_app('Twitter')
    assert phone.apps.count('Twitter') == 1


def test_app_is_uninstalled(phone: MobilePhone):
    phone.install_app('Twitter')
    phone.uninstall_app('Twitter')
    assert 'Twitter' not in phone.apps


def test_app_is_not_uninstalled_when_not_exists(phone: MobilePhone):
    phone.uninstall_app('Twitter')
    assert 'Twitter' not in phone.apps
