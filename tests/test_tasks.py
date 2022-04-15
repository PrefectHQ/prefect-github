from prefect import flow

from prefect_github.tasks import goodbye_prefect_github, hello_prefect_github


def test_hello_prefect_github():
    @flow
    def test_flow():
        return hello_prefect_github()

    flow_state = test_flow()
    task_state = flow_state.result()
    assert task_state.result() == "Hello, prefect-github!"


def goodbye_hello_prefect_github():
    @flow
    def test_flow():
        return goodbye_prefect_github()

    flow_state = test_flow()
    task_state = flow_state.result()
    assert task_state.result() == "Goodbye, prefect-github!"
