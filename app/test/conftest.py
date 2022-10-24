import pytest
from app.utils.props_factory import PropsFactory


@pytest.fixture(autouse=True, scope="module")
def props(request):

    props = PropsFactory(request.param)

    yield props

    props.tear_down()
