from unittest.mock import MagicMock

import pytest

from hijack import views


def test_login_with_id(rf, monkeypatch):
    request = rf.get("/")
    acquire_user_view = MagicMock()
    monkeypatch.setattr("hijack.views.acquire_user_view", acquire_user_view)
    with pytest.deprecated_call():
        views.login_with_id(request, 123)
    acquire_user_view.assert_called_once_with(request, 123)


def test_login_with_email(rf, monkeypatch):
    request = rf.get("/")
    acquire_user_view = MagicMock()
    monkeypatch.setattr("hijack.views.acquire_user_view", acquire_user_view)
    with pytest.deprecated_call():
        views.login_with_email(request, "spiderman@averngers.com")
    acquire_user_view.assert_called_once_with(request, "spiderman@averngers.com")


def test_login_with_username(rf, monkeypatch):
    request = rf.get("/")
    acquire_user_view = MagicMock()
    monkeypatch.setattr("hijack.views.acquire_user_view", acquire_user_view)
    with pytest.deprecated_call():
        views.login_with_username(request, "spiderman")
    acquire_user_view.assert_called_once_with(request, "spiderman")


def test_release_hijack(rf, monkeypatch):
    request = rf.get("/")
    release_user_view = MagicMock()
    monkeypatch.setattr("hijack.views.release_user_view", release_user_view)
    with pytest.deprecated_call():
        views.release_hijack(request)
    release_user_view.assert_called_once_with(request)
