report_template = """
Report
======

The experiment was a {judgment}!
Let's do this again, with a bigger budget.
"""


def send_report(result, smtp):
    if result > 0.5:
        judgment = 'big success'
    else:
        judgment = 'total failure'
    report = report_template.format(judgment=judgment)
    smtp.send_message(
        report,
        from_addr='pony@magicpony.com',
        to_addrs=['ferenc@magicpony.com'],
    )


from unittest.mock import Mock

def test_send_report_success():
    smtp = Mock()

    send_report(0.6, smtp)
    assert smtp.send_message.call_count == 1
    pos_args, kw_args = smtp.send_message.call_args
    message = pos_args[0]
    assert 'success' in message

    smtp.reset_mock()

    send_report(0.4, smtp)
    assert smtp.send_message.call_count == 1
    args, kwargs = smtp.send_message.call_args
    message = args[0]
    assert 'failure' in message

