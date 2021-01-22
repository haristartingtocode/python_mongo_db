"""
    File:       test_bootstrap.py
    Date:       23/11/2020
    Summary:    Script to test the bootstrap server.
"""

from wsgi import app


# pylint: disable=line-too-long

def test_bootstrap_tenant_single_group():
    """
    To test bootstrap server with single group in a tenant.
    :return:

    Example request:
        GET /bootstrap_params/<license_key>/<program_id>/<device_id>/<tenant_id>/<latitude>/<longitude>'
    """

    print('test_bootstrap_tenant_single_group:')

    with app.test_client() as c:
        rv = c.get('/bootstrap_server/activation/AAAA1-BBBB2-CCCC3/SDC/adfasdf23/testtt/30/40')

        assert rv.status_code == 200, f'The error code is {rv.status_code}'

        if rv.status_code == 200:
            json_data = rv.get_json()
            print(rv, json_data)


def test_bootstrap_tenant_multiple_group():
    """
    To test bootstrap server with multiple group in a tenant
    :return:

    Example request:
        GET /bootstrap_params/<license_key>/<machine_id>/<program_id>/<tenant_id>/<latitude>/<longitude>'
    """

    print('test_bootstrap_tenant_multiple_group:')

    with app.test_client() as c:
        rv = c.get('/bootstrap_server/activation/AAAA1-BBBB2-CCCC3/SDC/adfasdf23/df/30/40')

        assert rv.status_code == 200, f'The error code is {rv.status_code}'

        if rv.status_code == 200:
            json_data = rv.get_json()
            print(rv, json_data)


def test_get_expiry_time():
    """
    To test get expiry time

    Example request:

    """
    print('test_get_expiry_time:')

    with app.test_client() as c:
        rv = c.get('/bootstrap_server/validation/SDC/adfasdf23')

        assert rv.status_code == 200, f'The error code is {rv.status_code}'

        if rv.status_code == 200:
            json_data = rv.get_json()
            print(rv, json_data)


if __name__ == '__main__':
    print('----------------------------')
    print('tenant with single group:')
    test_bootstrap_tenant_single_group()
    print('-----------------------------')
    print('tenant with multiple group:')
    test_bootstrap_tenant_multiple_group()
    print('-----------------------------')
    test_get_expiry_time()
    print('-----------------------------')
