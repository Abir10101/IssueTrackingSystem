import pytest
from app import create_app, db
from app.auth.models.user import User


@pytest.fixture
def initiate():
    app = create_app()
    app_context = app.app_context()
    app_context.push()
    db.create_all()

    yield

    db.session.remove()
    db.drop_all()
    app_context.pop()


def test_add_user(initiate):
    user = User()
    user.u_name = "testUser"
    user.u_email = "abcd@gmail.com"
    user.u_password = "asdf"
    assert user.save() == False


def test_user_invalid_email(initiate):
    user = User()
    user.u_name = "testUser"
    user.u_email = "abcdgmail.com"
    user.u_password = "asdf"
    with pytest.raises(ValueError) as err:
        user.save()
    assert err.value.args[0] == 'InvalidEmail'


def test_user_empty_email(initiate):
    user = User()
    user.u_name = "testUser"
    user.u_password = "asdf"
    with pytest.raises(ValueError) as err:
        user.save()
    assert err.value.args[0] == 'InvalidEmail'

    user = User()
    user.u_name = "testUser"
    user.u_email = "  "
    user.u_password = "asdf"
    with pytest.raises(ValueError) as err:
        user.save()
    assert err.value.args[0] == 'InvalidEmail'


def test_user_empty_password(initiate):
    user = User()
    user.u_name = "testUser"
    user.u_email = "abcd@gmail.com"
    with pytest.raises(ValueError) as err:
        user.save()
    assert err.value.args[0] == 'InvalidPassword'

    user = User()
    user.u_name = "testUser"
    user.u_email = "abcd@gmail.com"
    user.u_password = "  "
    with pytest.raises(ValueError) as err:
        user.save()
    assert err.value.args[0] == 'InvalidPassword'


def test_user_empty_name(initiate):
    user = User()
    user.u_email = "abcd@gmail.com"
    user.u_password = "asdf"
    with pytest.raises(ValueError) as err:
        user.save()
    assert err.value.args[0] == 'InvalidName'


def test_duplicate_user(initiate):
    userOne = User()
    userOne.u_name = "testUser"
    userOne.u_email = "abcd@gmail.com"
    userOne.u_password = "asdf"
    userOne.save()

    userTwo = User()
    userTwo.u_name = "testUser"
    userTwo.u_email = "abcd@gmail.com"
    userTwo.u_password = "asdf"

    with pytest.raises(ValueError) as err:
        userTwo.save()

    assert err.value.args[0] == 'UserExists'


def test_email_trailing_space(initiate):
    user = User()
    user.u_name = "testUser"
    user.u_email = "abcd@gmail.com "
    user.u_password = "asdf"
    user.save()
    assert user.u_email == "abcd@gmail.com"
