from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client() -> TestClient:
    """Provide a test client with per-test activity state reset."""
    # Arrange: snapshot mutable in-memory state before each test.
    original_activities = deepcopy(activities)

    with TestClient(app) as test_client:
        yield test_client

    # Assert-style cleanup: restore in-memory state for test isolation.
    activities.clear()
    activities.update(original_activities)
